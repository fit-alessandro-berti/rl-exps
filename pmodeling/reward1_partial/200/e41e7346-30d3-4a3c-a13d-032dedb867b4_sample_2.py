import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (if any)
skip = SilentTransition()

# Define the loop structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Seed_Select, Nutrient_Mix, Climate_Setup, Light_Adjust, CO2_Control, Humidity_Tune, Growth_Monitor, Pest_Detect, Harvest_Plan
])

# Define the XOR structure
xor = OperatorPOWL(operator=Operator.XOR, children=[
    Produce_Sort, Pack_Biodeg, Drone_Dispatch, Waste_Recycle, Compost_Create
])

# Define the root node with the defined transitions and loop
root = StrictPartialOrder(nodes=[loop, xor])

# Add the order dependencies between nodes
root.order.add_edge(loop, xor)

# Return the root POWL model
return root