import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, light_adjust, co2_control, humidity_tune, growth_monitor, pest_detect])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, produce_sort])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pack_biodeg, drone_dispatch])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, compost_create])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[cycle_review])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)

# Add the initial and final transitions
root.order.add_edge(root, seed_select)
root.order.add_edge(xor1, nutrient_mix)
root.order.add_edge(xor2, nutrient_mix)
root.order.add_edge(xor3, nutrient_mix)
root.order.add_edge(xor4, nutrient_mix)
root.order.add_edge(xor1, drone_dispatch)
root.order.add_edge(xor2, drone_dispatch)
root.order.add_edge(xor3, drone_dispatch)
root.order.add_edge(xor4, drone_dispatch)
root.order.add_edge(drone_dispatch, cycle_review)