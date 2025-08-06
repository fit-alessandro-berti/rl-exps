import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
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

# Define the control flow
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, light_adjust, co2_control, humidity_tune])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_detect])
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_loop])
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, produce_sort, pack_biodeg, drone_dispatch])
cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle_review, waste_recycle, compost_create])

# Define the partial order
root = StrictPartialOrder(nodes=[seed_select, nutrient_mix, climate_loop, monitor_loop, harvest_loop, cycle_loop])
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_loop)
root.order.add_edge(climate_loop, monitor_loop)
root.order.add_edge(monitor_loop, harvest_loop)
root.order.add_edge(harvest_loop, cycle_loop)
root.order.add_edge(cycle_loop, seed_select)

print(root)