import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL transitions
seed_select = Transition(label='Seed Select')
nutrient_mix = Transition(label='Nutrient Mix')
climate_setup = Transition(label='Climate Setup')
light_adjust = Transition(label='Light Adjust')
co2_control = Transition(label='CO2 Control')
humidity_tune = Transition(label='Humidity Tune')
growth_monitor = Transition(label='Growth Monitor')
pest_detect = Transition(label='Pest Detect')
harvest_plan = Transition(label='Harvest Plan')
produce_sort = Transition(label='Produce Sort')
pack_biodeg = Transition(label='Pack Biodeg')
drone_dispatch = Transition(label='Drone Dispatch')
waste_recycle = Transition(label='Waste Recycle')
compost_create = Transition(label='Compost Create')
cycle_review = Transition(label='Cycle Review')

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[pest_detect, harvest_plan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[light_adjust, co2_control, humidity_tune])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[produce_sort, pack_biodeg, drone_dispatch])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, compost_create])
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, xor2])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[seed_select, nutrient_mix, loop])
root = StrictPartialOrder(nodes=[xor5, xor1, xor3, xor4, cycle_review])

# Define the dependencies between the nodes
root.order.add_edge(xor5, cycle_review)
root.order.add_edge(xor5, xor1)
root.order.add_edge(xor5, xor3)
root.order.add_edge(xor5, xor4)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, cycle_review)
root.order.add_edge(xor4, cycle_review)
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_setup)
root.order.add_edge(climate_setup, xor2)
root.order.add_edge(xor2, loop)

# Print the root model
print(root)