#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#
#            SIMULATION STOP            #
#.......................................#
time.stop_time               =   86400     # Max (simulated) time to evolve
time.max_step                =   -1          # Max number of time steps

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#
#         TIME STEP COMPUTATION         #
#.......................................#
time.fixed_dt         =   0.5        # Use this constant dt if > 0
time.cfl              =   0.95       # CFL factor

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#
#            INPUT AND OUTPUT           #
#.......................................#
io.KE_int = -1
io.line_plot_int = 1
time.plot_interval            =  1000       # Steps between plot files
time.checkpoint_interval      =  1000       # Steps between checkpoint files
io.restart_file = "chk48000"

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#
#               PHYSICS                 #
#.......................................#
incflo.gravity        =  0.0  0.0 -9.81  # Gravitational force (3D)
incflo.density        =  1.0             # Reference density 

incflo.use_godunov = 1
transport.viscosity = 0.0
transport.laminar_prandtl = 0.7
transport.turbulent_prandtl = 0.3333
turbulence.model = Smagorinsky
Smagorinsky_coeffs.Cs = 0.135

incflo.physics = ABL
ICNS.source_terms = BoussinesqBuoyancy CoriolisForcing GeostrophicForcing
BoussinesqBuoyancy.reference_temperature = 290.0
CoriolisForcing.east_vector = 1.0 0.0 0.0
CoriolisForcing.north_vector = 0.0 1.0 0.0
CoriolisForcing.latitude = 90.0
CoriolisForcing.rotational_time_period = 125663.706143592
GeostrophicForcing.rotational_time_period = 125663.706143592
GeostrophicForcing.geostrophic_wind = 10.0 0.0 0.0
incflo.velocity = 10.0 0.0 0.0

ABL.temperature_heights = 0.0 2000.0
ABL.temperature_values = 290.0 296.0
ABL.perturb_temperature = true
ABL.cutoff_height = 50.0
ABL.perturb_velocity = true
ABL.perturb_ref_height = 50.0
ABL.Uperiods = 4.0
ABL.Vperiods = 4.0
ABL.deltaU = 1.0
ABL.deltaV = 1.0

ABL.kappa = .41
ABL.surface_roughness_z0 = 0.01

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#
#        ADAPTIVE MESH REFINEMENT       #
#.......................................#
amr.n_cell              = 288 288 192    # Grid cells at coarsest AMRlevel
amr.max_level           = 0           # Max AMR level in hierarchy 
tagging.static_refinement = false
tagging.static_refinement_def = static_box.txt 

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨#
#              GEOMETRY                 #
#.......................................#
geometry.prob_lo        =   0.       0.     0.  # Lo corner coordinates
geometry.prob_hi        =   3000.  3000.  2000.  # Hi corner coordinates
geometry.is_periodic    =   1   1   0   # Periodicity x y z (0/1)

# Boundary conditions
zlo.type =   "wall_model"
zlo.temperature_type = "fixed_gradient"
zlo.temperature = 0.0

zhi.type =   "slip_wall"
zhi.temperature_type = "fixed_gradient"
zhi.temperature = 0.003 

incflo.verbose          =   0          

# MLMG settings
nodal_proj.mg_rtol = 1.0e-6
nodal_proj.mg_atol = 1.0e-12
mac_proj.mg_rtol = 1.0e-6
mac_proj.mg_atol = 1.0e-12
diffusion.mg_rtol = 1.0e-6
diffusion.mg_atol = 1.0e-12
diffusion_temperature.mg_rtol = 1.0e-10
diffusion_temperature.mg_atol = 1.0e-13