import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial.distance import cdist
import matplotlib as mpl
import matplotlib.cm as cm
from Parameters import Parameters
from matplotlib.animation import FuncAnimation




class Tissue(Parameters):
    def __init__(self):
        Parameters.__init__(self)
        
    def initialConditions(self):
        
        self.xy = np.array([[-0.5,-0.5], [0.5,-0.5], [0,0.5]])
        self.r = np.array([0.8, 0.9, 0.75])
        self.nofCells = len(self.r)
        self.t = 0
        self.r0 = self.r
        self.t0 = np.zeros(self.nofCells)
        self.Data = []
        self.dist = cdist(self.xy, self.xy)
        
    def radiusGrowth(self):
        self.r_old = self.r
        self.r = self.r_max - np.exp(-self.k*(self.t-self.t0))*(self.r_max - self.r0)
        
    def divisionProbability(self, r):
        c = 100/self.r_max
        y = 0.95*self.r_max
        r_min = 0.9*self.r_max
        b = (1 + np.exp(c*(self.r_max-y)))*(1 + np.exp(c*(r_min-y)))/(np.exp(c*(r_min-y)) - np.exp(c*(self.r_max-y)))
        a = -b/(1 + np.exp(c*(r_min-y)))
        P = a+b/(1 + np.exp(c*(r-y)))

        return np.maximum(0,P)
    
    def cellDivision(self):
        P0 = self.divisionProbability(self.r_old)       
        P = self.divisionProbability(self.r)

        Prob = (P-P0)/(1-P0)
        Prob[self.r_old == self.r0] = P[self.r_old == self.r0]

        # Choose where division will randomly occur
        random_numbers = np.random.rand(self.nofCells)
        indices = np.where(random_numbers < Prob)

        # New radius based on the area of the mother cell being two times that of the daughter cells
        # Use volume in 3D instead
        r_new = self.r[indices]/2**(1/2)

        # Distance between the two daughter cells
        dist = np.random.normal((self.r[indices] - r_new)/2, 0.1*(self.r[indices] - r_new)/2)

        # Angles of cell division
        angle = np.random.rand(len(indices))*2*np.pi

        # Displacement vectors
        dx = dist*np.cos(angle)
        dy = dist*np.sin(angle)

        # Displacement
        dxy = np.array([dx,dy]).T
        xy1 = self.xy[indices] + dxy
        xy2 = self.xy[indices] - dxy

        # Change x-y-position to new value and add new cell to array
        self.xy[indices] = xy1
        self.xy = np.append(self.xy, xy2, axis=0)

        # Update radii and include radii for new cells
        self.r[indices] = r_new
        self.r = np.append(self.r, r_new)

        # Change initial radius to value directly after division and include new cells to array
        self.r0[indices] = r_new
        self.r0 = np.append(self.r0, r_new)

        # Change initial radius to value directly after division and include new cells to array
        self.t0[indices] = self.t
        self.t0 = np.append(self.t0, self.t0[indices])
    
        # Change new number of cells
        self.nofCells = len(self.r)

    def displacement(self):
        self.dist = cdist(self.xy, self.xy)
        x = self.xy[:,0]
        y = self.xy[:,1]

        # Pairwise sum of radii and difference of coordinates
        r_pairwise = self.r + self.r[:,None]
        x_pairwise = x - x[:,None]
        y_pairwise = y - y[:,None]

        # Absolute values of forces according to Morse potential
        F = self.F0*2*self.alpha*(np.exp(-self.alpha*(self.dist-r_pairwise*self.sigma)) - np.exp(-2*self.alpha*(self.dist-r_pairwise*self.sigma)))
        F[self.dist > r_pairwise] = 0

        # Fill distance matrix with inf on diagonal
        dist = self.dist*1
        np.fill_diagonal(dist, np.inf)

        # x- and y-direction of forces
        Fx = F*(x_pairwise)/dist
        Fy = F*(y_pairwise)/dist

        # Sum of all forces acting on each cell as a vector
        Force = np.array([np.sum(Fx, axis=1), np.sum(Fy, axis=1)]).T
        
        self.xy = self.xy + self.dt*Force# + 0.1*np.random.normal(0, self.dt**(1/2), self.xy.shape)
                                      
    def cellPlot(self, size = 2, alphaValue=0.3,xLimVector=[-10,10],yLimVector=[-10,10]):        
                
    
        #### plot cell nuclei ####
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111, aspect='equal')
        ax1.scatter(self.xy[:,0],self.xy[:,1], color='k', s=size, zorder=2)
      
        #### plot cells as circle  ####
        for i in range(self.nofCells):
            (xPosition,yPosition)=self.xy[i]
            radius=self.r[i]
            ax1.add_patch(plt.Circle((xPosition,yPosition), radius,alpha=alphaValue))
            
        plt.xlim(xLimVector)
        plt.ylim(yLimVector)
        plt.axis('off')

    def collectData(self):
        self.Data.append([self.xy,self.r])
        return

    def saveData(self, directory = ''):
        # Save all parameters in .txt file
        with open(directory + 'Parameters.txt', 'w') as f:
            f.write(''.join(["%s = %s\n" % (k,v) for k,v in self.__dict__.items() if not hasattr(v, '__iter__')]))

        # Save plot of geometry
        plt.figure()
        self.cellPlot()
        plt.savefig(directory + 'tissue.png', transparent = True) 
        plt.savefig(directory + 'tissue.pdf', transparent = True)   

        df = pd.DataFrame()
        df['x-Position'] = self.xy[:,0]
        df['y-Position'] = self.xy[:,1]
        df['Radius'] = self.r
        df.to_csv(directory + 'Data.csv', index = False)

    def evolution(self, T = 0):
        if T == 0:
            T = self.T       
        N = int(T/self.dt)

        if not hasattr(self, 'xy'):
            self.initialConditions()
        
        for i in range(N):
            self.t += self.dt
            self.radiusGrowth()
            self.cellDivision()
            self.displacement()
            self.collectData()