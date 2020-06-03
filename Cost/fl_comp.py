from openmdao.api import ExplicitComponent


class FlyawayComp(ExplicitComponent):

    #def initialize(self):
        #self.options.declare('Q', types=float)
        #self.options.declare('Tinlet', types=float)
        #self.options.declare('EN', types=float)
        #self.options.declare('sealevel_thrust', types=float)
        #self.options.declare('mass_flow_rate', types=float)


    def setup(self):
        self.add_input('We')
        self.add_input('V')

        self.add_input('Q')
        self.add_input('Tinlet')
        self.add_input('EN')
        self.add_input('sealevel_thrust')
        self.add_input('mass_flow_rate')

        self.add_output('Flyaway')

        self.declare_partials('Flyaway', 'We')
        self.declare_partials('Flyaway', 'V')
        

    def compute(self, inputs, outputs):
        #Q = self.options['Q']
        #Tinlet = self.options['Tinlet']
        #EN = self.options['EN']
        #Tmax = self.options['sealevel_thrust']
        #Mmax = self.options['mass_flow_rate']
        EN=inputs['EN']
        Tinlet=inputs['Tinlet']
        Q = inputs['Q']
        We = inputs['We']
        V = inputs['V']
        Tmax = inputs['sealevel_thrust']
        Mmax = inputs['mass_flow_rate']

        outputs['Flyaway'] = 1.25*(7.37*We**0.82*V**0.484*Q**0.641*108+0.133*7.37*We**0.82*V**0.484*Q**0.641*98+3112*(0.043*Tmax+243.25*Mmax+0.969*Tinlet-2228)*EN+22.1*We**0.921*V**0.621*Q**0.799)

    def compute_partials(self, inputs, partials):
        #Q = self.options['Q']
        #Tinlet = self.options['Tinlet']
        #EN = self.options['EN']
        #Tmax = self.options['sealevel_thrust']
        #Mmax = self.options['mass_flow_rate']
        EN=inputs['EN']
        Tinlet=inputs['Tinlet']
        Q = inputs['Q']
        We = inputs['We']
        V = inputs['V']
        Tmax = inputs['sealevel_thrust']
        Mmax = inputs['mass_flow_rate']
        

        partials['Flyaway', 'We'] =25.4426*Q**0.799*V**0.621/We**0.079+914.321*Q**0.641*V**0.484/We**0.18 
        partials['Flyaway', 'V'] = 17.1551*Q**0.799*We**0.921/V**0.379+539.672*Q**0.641*We**0.82/V**0.516