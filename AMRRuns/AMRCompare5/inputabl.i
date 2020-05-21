
#---------------------------------------#
#            SIMULATION STOP            #
#---------------------------------------#
time.stop_time                 = 20000.0                        # Max (simulated) time to evolve
time.max_step                  = 40000                          # Max number of time steps

#---------------------------------------#
#         TIME STEP COMPUTATION         #
#---------------------------------------#
time.fixed_dt                  = 0.5                            # Use this constant dt if > 0
time.cfl                       = 0.95                           # CFL factor

#---------------------------------------#
#            INPUT AND OUTPUT           #
#---------------------------------------#
time.plot_interval             = 1000                           # Steps between plot files
time.checkpoint_interval       = 1000                           # Steps between checkpoint files
io.KE_int                      = 1                              
io.line_plot_int               = 1                              

#---------------------------------------#
#               PHYSICS                 #
#---------------------------------------#
incflo.gravity                 = 0.0 0.0 -9.81                  # Gravitational force (3D)
incflo.density                 = 1.22                           # Reference density
transport.viscosity            = 1.8375e-05                     
transport.laminar_prandtl      = 0.7                            
transport.turbulent_prandtl    = 0.3333                         
turbulence.model               = Smagorinsky                    
Smagorinsky_coeffs.Cs          = 0.135                          

# ABL forcing
ICNS.source_terms              = BoussinesqBuoyancy CoriolisForcing ABLForcing 
BoussinesqBuoyancy.reference_temperature = 288.15                         
ABLForcing.abl_forcing_height  = 57.19                          
incflo.velocity                = 4.70059422901 3.93463008353 0.0 

ABL.temperature_heights        = 1050.0 1150.0 1920.0           
ABL.temperature_values         = 288.15 296.15 296.9            
ABL.kappa                      = 0.4                            
ABL.surface_roughness_z0       = 0.0001                         
# Coriolis forcing
CoriolisForcing.latitude       = 55.49                          
CoriolisForcing.east_vector    = 1.0 0.0 0.0                    
CoriolisForcing.north_vector   = 0.0 1.0 0.0                    
CoriolisForcing.rotational_time_period = 86164.0900027                  
incflo.use_godunov             = 1                              
incflo.physics                 = ABL                            

#---------------------------------------#
#        ADAPTIVE MESH REFINEMENT       #
#---------------------------------------#
amr.n_cell                     = 128 128 160                    # Grid cells at coarsest AMRlevel
amr.max_level                  = 0                              # Max AMR level in hierarchy

#---------------------------------------#
#              GEOMETRY                 #
#---------------------------------------#
geometry.prob_lo               = 0.0 0.0 0.0                    # Lo corner coordinates
geometry.prob_hi               = 1536.0 1536.0 1920.0           # Hi corner coordinates
geometry.is_periodic           = 1 1 0                          # Periodicity x y z (0/1)

# Boundary conditions
zlo.type                       =   "wall_model"
zlo.temperature_type           = "fixed_gradient"
zlo.temperature                = 0.0
zhi.type                       =   "slip_wall"
zhi.temperature_type           = "fixed_gradient"
zhi.temperature                = 0.003 # tracer is used to specify potential temperature gradient


#---------------------------------------#
#              VERBOSITY                #
#---------------------------------------#
incflo.verbose                 = 3                              # incflo.level

#---------------------------------------#
#              DEBUGGING                #
#---------------------------------------#
#possible debugging parameters
amrex.fpe_trap_invalid         = 0                              # Trap NaNs
diffusion.mg_verbose           = 0                              
diffusion.mg_cg_verbose        = 0                              
#diffusion.mg_rtol              = 1e-06                          
#diffusion.mg_atol              = 1e-08                          
#mac_proj.mg_rtol               = 1e-06                          
#mac_proj.mg_atol               = 1e-08                          
#nodal_proj.mg_verbose          = 0                              
#nodal_proj.mg_rtol             = 1e-06                          
#nodal_proj.mg_atol             = 1e-08                          
