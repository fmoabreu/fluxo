# Copyright (C) 2010-2014 Simula Research Laboratory
#
# This file is part of CBCFLOW.
#
# CBCFLOW is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CBCFLOW is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with CBCFLOW. If not, see <http://www.gnu.org/licenses/>.

"""Utility functions and classes shared between scheme implementations."""

from .ics import *
from .bcs import *
from .timestepping import *
from .rhsgenerator import RhsGenerator
from .spaces import NSSpacePool, NSSpacePoolMixed, NSSpacePoolSegregated, NSSpacePoolSplit
from .solver_creation import create_solver
#from .unassembledmatrix import UnassembledMatrix

__all__ = [k for k,v in globals().items()
           if hasattr(v, "__module__")
           and __package__ in v.__module__]
