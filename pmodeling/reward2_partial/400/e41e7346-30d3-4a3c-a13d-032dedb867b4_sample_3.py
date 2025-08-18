import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the process
Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Setup = Transition(label='Climate Setup')
Light_Adjust = Transition(label='Light Adjust')
CO2_Control = Transition(label='CO2 Control')
Humidity_Tune = Transition(label='Humidity Tune')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Detect = Transition(label='Pest Detect')
Harvest_Plan = Transition(label='Harvest Plan')
Produce_Sort = Transition(label='Produce Sort')
Pack_Biodeg = Transition(label='Pack Biodeg')
Drone_Dispatch = Transition(label='Drone Dispatch')
Waste_Recycle = Transition(label='Waste Recycle')
Compost_Create = Transition(label='Compost Create')
Cycle_Review = Transition(label='Cycle Review')

# Define the partial order model
root = StrictPartialOrder(nodes=[Seed_Select, Nutrient_Mix, Climate_Setup, Light_Adjust, CO2_Control, Humidity_Tune, Growth_Monitor, Pest_Detect, Harvest_Plan, Produce_Sort, Pack_Biodeg, Drone_Dispatch, Waste_Recycle, Compost_Create, Cycle_Review])

# Define the dependencies between transitions
root.order.add_edge(Seed_Select, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Climate_Setup)
root.order.add_edge(Climate_Setup, Light_Adjust)
root.order.add_edge(Light_Adjust, CO2_Control)
root.order.add_edge(CO2_Control, Humidity_Tune)
root.order.add_edge(Humidity_Tune, Growth_Monitor)
root.order.add_edge(Growth_Monitor, Pest_Detect)
root.order.add_edge(Pest_Detect, Harvest_Plan)
root.order.add_edge(Harvest_Plan, Produce_Sort)
root.order.add_edge(Produce_Sort, Pack_Biodeg)
root.order.add_edge(Pack_Biodeg, Drone_Dispatch)
root.order.add_edge(Drone_Dispatch, Waste_Recycle)
root.order.add_edge(Waste_Recycle, Compost_Create)
root.order.add_edge(Compost_Create, Cycle_Review)

# The final result is saved in the variable 'root'