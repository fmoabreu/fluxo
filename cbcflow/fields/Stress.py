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

from cbcpost import get_grad_space, Field
from dolfin import Function, Constant, grad, Identity
from cbcflow.fields.DynamicViscosity import DynamicViscosity

class Stress(Field):

    def add_fields(self):
        return [DynamicViscosity()]

    def before_first_compute(self, get):
        u = get("Velocity")

        if self.params.expr2function == "assemble":
            V = get_grad_space(u, family="DG", degree=0)
        else:
            V = get_grad_space(u)

        self._function = Function(V, name=self.name)

    def compute(self, get):
        u = get("Velocity")
        p = get("Pressure")
        mu = get("DynamicViscosity")
        if isinstance(mu, (float, int)):
            mu = Constant(mu)

        expr = mu*(grad(u) + grad(u).T) - p*Identity(len(u))

        return self.expr2function(expr, self._function)
