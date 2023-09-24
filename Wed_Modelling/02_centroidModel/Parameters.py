class Parameters:
    def __init__(self):
        #### time parameters ####
        self.T = 24                                # Time
        self.N = 3000                              # Number of timesteps
              
        #### geometry parameters ####
        self.dt = self.T/(self.N - 1)              # timestep
        self.r_max = 1                             # Maximum radius
        self.k = 0.5                               # Cell growth rate
        self.F0 = 0.01                             # Force scaling
        self.alpha = 3                             # Cell stiffness
        self.sigma = 0.7                           # Cell-cell distance optimality factor
        
       