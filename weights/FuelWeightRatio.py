import numpy as np  
from openmdao.api import ExplicitComponent


class FuelWeightRatio(ExplicitComponent):




    def setup(self):
        self.add_input('R')
        self.add_input('SFC')
        self.add_input('LD')
        self.add_input('V')


        self.add_output('Wfr')

        self.declare_partials('Wfr', 'V')
        self.declare_partials('Wfr', 'LD')


    def compute(self, inputs, outputs):
  
        R=inputs['R']
        SFC = inputs['SFC']
        LD = inputs['LD']
        V = inputs['V']
     

        outputs['Wfr'] = 1-np.exp(-1/LD*R*SFC/V)
        
    def compute_partials(self, inputs, partials):
   
        R=inputs['R']
        SFC = inputs['SFC']
        LD = inputs['LD']
        V = inputs['V']
        

        partials['Wfr', 'V'] = -1/LD*R*SFC/V**2*np.exp(-1/LD*R*SFC/V)
        partials['Wfr', 'LD'] = -R*SFC/LD**2/V*np.exp(-1/LD*R*SFC/V)
