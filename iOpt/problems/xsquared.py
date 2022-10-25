from abc import ABC, abstractmethod
import numpy as np
from iOpt.trial import Point
from iOpt.trial import FunctionValue
from iOpt.trial import Trial
from iOpt.Problem import Problem
import math


class XSquared(Problem):
    """Base class for optimization problems"""
    def __init__(self,
				 dimension: int):
		self.dimension = dimension
        self.numberOfFloatVariables = dimension

        self.floatVariableNames: np.ndarray(shape = (1), dtype = str) = [] #?

        self.lowerBoundOfFloatVariables = np.ndarray(shape = (dimension), dtype = np.double) 
		self.lowerBoundOfFloatVariables.fill(-1)
        self.upperBoundOfFloatVariables = np.ndarray(shape = (dimension), dtype = np.double)
		self.upperBoundOfFloatVariables.fill(1)
		
        self.knownOptimum = np.ndarray(shape = (1), dtype = Trial)
		self.knownOptimum[0].point.floatVariables =  np.ndarray(shape = (dimension), dtype = np.double)
		self.knownOptimum[0].point.floatVariables.fill(0)
		self.knownOptimum[0].functionValues = np.ndarray(shape = (1), dtype = np.double)
		self.knownOptimum[0].functionValues[0].value = 0
		
    
    def Calculate(self, point: Point, functionValue: FunctionValue) -> FunctionValue:
		sum: np.double = 0
		for i in point.floatVariables.size
			sum += point.floatVariables[i]*point.floatVariables[i]
			
		functionValue.value = sum
		return functionValue
        """
        Compute selected function at given point.
        For any new problem that inherits from :class:`Problem`, this method should be replaced.
        :return: Calculated function value."""
        pass

