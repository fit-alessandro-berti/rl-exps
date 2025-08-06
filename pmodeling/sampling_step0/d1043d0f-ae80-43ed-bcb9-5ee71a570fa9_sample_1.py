import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Env_Analysis = Transition(label='Env Analysis')
Module_Design = Transition(label='Module Design')
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Setup = Transition(label='Climate Setup')
LED_Install = Transition(label='LED Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
Pest_Control = Transition(label='Pest Control')
Waste_Recycle = Transition(label='Waste Recycle')
Hydro_Test = Transition(label='Hydro Test')
Staff_Train = Transition(label='Staff Train')
Yield_Forecast = Transition(label='Yield Forecast')
Market_Plan = Transition(label='Market Plan')
Data_Review = Transition(label='Data Review')
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Module_Design, Seed_Selection, Nutrient_Mix, Climate_Setup, LED_Install, Sensor_Deploy, Pest_Control, Waste_Recycle, Hydro_Test, Staff_Train, Yield_Forecast, Market_Plan, Data_Review])
xor = OperatorPOWL(operator=Operator.XOR, children=[Site_Survey, Env_Analysis, loop])
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, loop)