from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Analysis = Transition(label='Site Analysis')
Design_Layout = Transition(label='Design Layout')
Module_Assembly = Transition(label='Module Assembly')
Climate_Setup = Transition(label='Climate Setup')
Sensor_Install = Transition(label='Sensor Install')
Water_Testing = Transition(label='Water Testing')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Selection = Transition(label='Seed Selection')
Planting_Phase = Transition(label='Planting Phase')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Yield_Audit = Transition(label='Yield Audit')
Packaging_Prep = Transition(label='Packaging Prep')
Market_Delivery = Transition(label='Market Delivery')
Waste_Recycling = Transition(label='Waste Recycling')

# Define silent transitions
skip = SilentTransition()

# Define loop and choice nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, Pest_Control])
choice = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Plan, skip])
loop_choice = OperatorPOWL(operator=Operator.LOOP, children=[loop, choice])

# Define partial order
root = StrictPartialOrder(nodes=[Site_Analysis, Design_Layout, Module_Assembly, Climate_Setup, Sensor_Install, Water_Testing, Nutrient_Mix, Seed_Selection, Planting_Phase, loop_choice, Yield_Audit, Packaging_Prep, Market_Delivery, Waste_Recycling])
root.order.add_edge(Site_Analysis, Design_Layout)
root.order.add_edge(Design_Layout, Module_Assembly)
root.order.add_edge(Module_Assembly, Climate_Setup)
root.order.add_edge(Climate_Setup, Sensor_Install)
root.order.add_edge(Sensor_Install, Water_Testing)
root.order.add_edge(Water_Testing, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Seed_Selection)
root.order.add_edge(Seed_Selection, Planting_Phase)
root.order.add_edge(Planting_Phase, Growth_Monitor)
root.order.add_edge(Growth_Monitor, Pest_Control)
root.order.add_edge(Pest_Control, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Yield_Audit)
root.order.add_edge(Yield_Audit, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Market_Delivery)
root.order.add_edge(Market_Delivery, Waste_Recycling)

# Print the result
print(root)