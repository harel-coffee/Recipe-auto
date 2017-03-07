# -*- coding: utf-8 -*-

"""
Copyright 2016 Walter José

This file is part of the RECIPE Algorithm.

The RECIPE is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

RECIPE is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. See http://www.gnu.org/licenses/.

"""

import load_method as load

#Ignoring the warnings:
import warnings
warnings.filterwarnings("ignore")

def load_pipeline(mlAlgorithm):

	"""Uses scikit-learn's make pipeline to generate a new pipeline to be evaluated.
	
	Parameters
	----------
	mlAlgorithm: string
		A string the contains the pipeline generated by the grammar based GP
	"""

	pipeline=[]

	steps_list = mlAlgorithm.strip().split('#')

	for steps in steps_list:
		temporary_method=load.load_method(steps)
		pipeline.append(temporary_method)

	return pipeline