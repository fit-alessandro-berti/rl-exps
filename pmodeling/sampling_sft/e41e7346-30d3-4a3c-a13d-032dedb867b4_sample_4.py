import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
seed_select   = Transition(label='Seed Select')
nutrient_mix  = Transition(label='Nutrient Mix')
climate_setup = Transition(label='Climate Setup')
light_adjust  = Transition(label='Light Adjust')
co2_control   = Transition(label='CO2 Control')
humidity_tune = Transition(label='Humidity Tune')
growth_monitor= Transition(label='Growth Monitor')
pest_detect   = Transition(label='Pest Detect')
harvest_plan  = Transition(label='Harvest Plan')
produce_sort  = Transition(label='Produce Sort')
pack_biodeg   = Transition(label='Pack Biodeg')
drone_dispatch= Transition(label='Drone Dispatch')
waste_recycle = Transition(label='Waste Recycle')
compost_create= Transition(label='Compost Create')
cycle_review  = Transition(label='Cycle Review')

# Build the loop body: Pest Detect -> Harvest Plan -> Produce Sort -> Pack Biodeg -> Drone Dispatch -> Waste Recycle
body = StrictPartialOrder(nodes=[pest_detect, harvest_plan, produce_sort, pack_biodeg, drone_dispatch, waste_recycle])
body.order.add_edge(pest_detect, harvest_plan)
body.order.add_edge(harvest_plan, produce_sort)
body.order.add_edge(produce_sort, pack_biodeg)
body.order.add_edge(pack_biodeg, drone_dispatch)
body.order.add_edge(drone_dispatch, waste_recycle)

# LOOP: Climate Setup -> Light Adjust -> CO2 Control -> Humidity Tune -> Growth Monitor -> body
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, light_adjust, co2_control, humidity_tune, growth_monitor, body])

# Assemble the top-level partial order
root = StrictPartialOrder(nodes=[loop, compost_create, cycle_review])
root.order.add_edge(loop, compost_create)
root.order.add_edge(loop, cycle_review)

# Print the root model for verification
print(root)