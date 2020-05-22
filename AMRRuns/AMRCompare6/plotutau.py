#!/usr/bin/env python
#

from pylab import *

# Load AMR results
AMRutau = loadtxt('utau.dat')
dt      = 0.5
AMRt    = dt*linspace(0,40000,40001)


# Load Nalu results
NALUutau = loadtxt('../../NaluRun/Utauprof.dat')

print("AMR-wind avg utau  = %f"%mean(AMRutau[30000:]))
print("NALU-wind avg utau = %f"%mean(NALUutau[30000:,1]))

figure(figsize=(6,4), facecolor='white', dpi=150)
plot(AMRt, AMRutau, 'b', label='AMR-wind')
plot(NALUutau[:,0], NALUutau[:,1], 'r', label='Nalu-wind')
ylim([0.15, 0.20])
xlabel('Time [s]')
ylabel('Utau')
legend()
tight_layout()
savefig('utaucomparison.png')
#show()
