import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Setup = Transition(label='Sensor Setup')
Env_Monitor = Transition(label='Env Monitor')
Growth_Scan = Transition(label='Growth Scan')
Pest_Control = Transition(label='Pest Control')
Water_Cycle = Transition(label='Water Cycle')
Harvest_Robo = Transition(label='Harvest Robo')
Yield_Assess = Transition(label='Yield Assess')
Waste_Process = Transition(label='Waste Process')
Energy_Sync = Transition(label='Energy Sync')
Pack_Biodeg = Transition(label='Pack Biodeg')
Market_Track = Transition(label='Market Track')
Order_Align = Transition(label='Order Align')
Logistics_Plan = Transition(label='Logistics Plan')
Feedback_Loop = Transition(label='Feedback Loop')

# Define the partial order
root = StrictPartialOrder(nodes=[Seed_Select, Nutrient_Mix, Sensor_Setup, Env_Monitor, Growth_Scan, Pest_Control, Water_Cycle, Harvest_Robo, Yield_Assess, Waste_Process, Energy_Sync, Pack_Biodeg, Market_Track, Order_Align, Logistics_Plan, Feedback_Loop])

# Define the partial order dependencies
root.order.add_edge(Seed_Select, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Sensor_Setup)
root.order.add_edge(Sensor_Setup, Env_Monitor)
root.order.add_edge(Env_Monitor, Growth_Scan)
root.order.add_edge(Growth_Scan, Pest_Control)
root.order.add_edge(Pest_Control, Water_Cycle)
root.order.add_edge(Water_Cycle, Harvest_Robo)
root.order.add_edge(Harvest_Robo, Yield_Assess)
root.order.add_edge(Yield_Assess, Waste_Process)
root.order.add_edge(Waste_Process, Energy_Sync)
root.order.add_edge(Energy_Sync, Pack_Biodeg)
root.order.add_edge(Pack_Biodeg, Market_Track)
root.order.add_edge(Market_Track, Order_Align)
root.order.add_edge(Order_Align, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Feedback_Loop)

# Print the final result
print(root)