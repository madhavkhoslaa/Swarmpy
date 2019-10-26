import numpy as np

class Enviorment():
    def __init__(self, dimensions, shape):
        """
        Inputs: Dimensions as string. Dimensions can be 1D, 2D, 3D
        shape: The Bounds for the dimension. (64, 64) for a 2D dimension creates a matrix of same size
        """
        assert isinstance(dimensions, str)
        assert isinstance(shape, [tuple, list])
        self.dimensions= dimensions
        self.shape= shape
        self.Enviorment= np.zeros(shape= self.shape)
        #self maxagents= spaces in an array

    def spawn(self, robot_object):
        position= rob
