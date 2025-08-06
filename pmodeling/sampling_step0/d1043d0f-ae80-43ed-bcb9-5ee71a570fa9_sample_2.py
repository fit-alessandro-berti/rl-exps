import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loops
loop_site = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Env_Analysis, Module_Design, Seed_Selection, Nutrient_Mix, Climate_Setup, LED_Install, Sensor_Deploy, Pest_Control, Waste_Recycle, Hydro_Test, Staff_Train, Yield_Forecast, Market_Plan, Data_Review])
loop_site.order.add_edge(Site_Survey, Env_Analysis)
loop_site.order.add_edge(Env_Analysis, Module_Design)
loop_site.order.add_edge(Module_Design, Seed_Selection)
loop_site.order.add_edge(Seed_Selection, Nutrient_Mix)
loop_site.order.add_edge(Nutrient_Mix, Climate_Setup)
loop_site.order.add_edge(Climate_Setup, LED_Install)
loop_site.order.add_edge(LED_Install, Sensor_Deploy)
loop_site.order.add_edge(Sensor_Deploy, Pest_Control)
loop_site.order.add_edge(Pest_Control, Waste_Recycle)
loop_site.order.add_edge(Waste_Recycle, Hydro_Test)
loop_site.order.add_edge(Hydro_Test, Staff_Train)
loop_site.order.add_edge(Staff_Train, Yield_Forecast)
loop_site.order.add_edge(Yield_Forecast, Market_Plan)
loop_site.order.add_edge(Market_Plan, Data_Review)

# Define xor
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])

# Define root
root = StrictPartialOrder(nodes=[loop_site, xor])
root.order.add_edge(loop_site, xor)