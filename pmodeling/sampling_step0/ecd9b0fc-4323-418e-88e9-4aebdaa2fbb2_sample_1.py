import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Site_Survey = Transition(label='Site Survey')
Structure_Check = Transition(label='Structure Check')
Hydroponic_Install = Transition(label='Hydroponic Install')
Lighting_Setup = Transition(label='Lighting Setup')
Climate_Control = Transition(label='Climate Control')
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Water_Recycling = Transition(label='Water Recycling')
Sensor_Deploy = Transition(label='Sensor Deploy')
Pest_Control = Transition(label='Pest Control')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Plan = Transition(label='Harvest Plan')
Packaging_Prep = Transition(label='Packaging Prep')
Delivery_Route = Transition(label='Delivery Route')
Data_Analysis = Transition(label='Data Analysis')
Yield_Forecast = Transition(label='Yield Forecast')

# Define the silent activities
skip = SilentTransition()

# Define the process
loop = OperatorPOWL(operator=Operator.LOOP, children=[Climate_Control, Pest_Control, Growth_Monitor])
xor = OperatorPOWL(operator=Operator.XOR, children=[Sensor_Deploy, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Packaging_Prep, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Delivery_Route, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Data_Analysis, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Yield_Forecast, skip])
root = StrictPartialOrder(nodes=[Site_Survey, Structure_Check, Hydroponic_Install, Lighting_Setup, loop, xor, Nutrient_Mix, Water_Recycling, xor2, Harvest_Plan, xor3, xor4, xor5])
root.order.add_edge(Site_Survey, Structure_Check)
root.order.add_edge(Structure_Check, Hydroponic_Install)
root.order.add_edge(Hydroponic_Install, Lighting_Setup)
root.order.add_edge(Lighting_Setup, Climate_Control)
root.order.add_edge(Climate_Control, Pest_Control)
root.order.add_edge(Pest_Control, Growth_Monitor)
root.order.add_edge(Growth_Monitor, loop)
root.order.add_edge(Climate_Control, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Water_Recycling)
root.order.add_edge(Water_Recycling, xor)
root.order.add_edge(Sensor_Deploy, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Delivery_Route)
root.order.add_edge(Delivery_Route, Data_Analysis)
root.order.add_edge(Data_Analysis, Yield_Forecast)

# Print the root
print(root)