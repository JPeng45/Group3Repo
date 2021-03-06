#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

from openmdao.api import ExplicitComponent


class Thrust(ExplicitComponent):

    def initialize(self):
        self.options.declare('e', types=float)

    def setup(self):
        self.add_input('throttle')
        self.add_input('avaliable_thrust')
        self.add_output('thrust')

        self.declare_partials('CDi', 'CL')
        self.declare_partials('CDi', 'AR')

    def compute(self, inputs, outputs):
        throttle=inputs['throttle']
        a_thrust=inputs['avaliable_thrust']

        #outputs['thrust'] = (throttle * a_thrust)
    
    
    def Thrust(self, inputs, outputs):
        comp = PowerCombinationComp(
            shape=shape,
            out_name='thrust',
            powers_dict=dict(
                throttle=1.,
                available_thrust=1.,
            ),
        )

    def compute_partials(self, inputs, partials):
        e = self.options['e']

        throttle=inputs['throttle']
        a_thrust=inputs['sealevel_thrust']

        partials['thrust', 'throttle'] = a_thrust
        partials['thrust', 'avaliable_thrust'] = throttle

