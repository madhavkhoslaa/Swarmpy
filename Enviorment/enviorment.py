import numpy as np
from Agents import robot

class Enviorment():
    def __init__(self, dimensions, shape):
        """
        Creates an enviorment for agents to spawn and move across the enviorment
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
        position= robot_object.position
        pass
    def check_position(self, position):
        """Returns a bool if an agent is present at the position or not"""
        pass

