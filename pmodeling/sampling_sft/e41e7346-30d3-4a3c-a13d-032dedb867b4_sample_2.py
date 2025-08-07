import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_select     = Transition(label='Seed Select')
nutrient_mix    = Transition(label='Nutrient Mix')
climate_setup   = Transition(label='Climate Setup')
light_adjust    = Transition(label='Light Adjust')
co2_control     = Transition(label='CO2 Control')
humidity_tune   = Transition(label='Humidity Tune')
growth_monitor  = Transition(label='Growth Monitor')
pest_detect     = Transition(label='Pest Detect')
harvest_plan    = Transition(label='Harvest Plan')
produce_sort    = Transition(label='Produce Sort')
pack_biodeg     = Transition(label='Pack Biodeg')
drone_dispatch  = Transition(label='Drone Dispatch')
waste_recycle   = Transition(label='Waste Recycle')
compost_create  = Transition(label='Compost Create')
cycle_review    = Transition(label='Cycle Review')

# Define the growth monitoring & pest detection sub-process as a partial order
monitoring_po = StrictPartialOrder(nodes=[growth_monitor, pest_detect])
# No additional order edges needed since they are concurrent

# Define the waste recycling & compost creation sub-process as a strict partial order
recycling_po = StrictPartialOrder(nodes=[waste_recycle, compost_create])
recycling_po.order.add_edge(waste_recycle, compost_create)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    seed_select,
    nutrient_mix,
    climate_setup,
    light_adjust,
    co2_control,
    humidity_tune,
    monitoring_po,
    harvest_plan,
    produce_sort,
    pack_biodeg,
    drone_dispatch,
    recycling_po,
    cycle_review
])

# Define the control‐flow dependencies
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_setup)
root.order.add_edge(climate_setup, light_adjust)
root.order.add_edge(light_adjust, co2_control)
root.order.add_edge(co2_control, humidity_tune)
root.order.add_edge(humidity_tune, monitoring_po)
root.order.add_edge(monitoring_po, harvest_plan)
root.order.add_edge(harvest_plan, produce_sort)
root.order.add_edge(produce_sort, pack_biodeg)
root.order.add_edge(pack_biodeg, drone_dispatch)
root.order.add_edge(drone_dispatch, recycling_po)
root.order.add_edge(recycling_po, compost_create)
root.order.add_edge(compost_create, cycle_review)