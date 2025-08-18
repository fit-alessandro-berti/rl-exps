import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, light_adjust, co2_control, humidity_tune])
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_detect, harvest_plan, produce_sort, pack_biodeg, drone_dispatch])
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle, compost_create])

root = StrictPartialOrder(nodes=[seed_select, nutrient_mix, climate_loop, growth_loop, waste_loop, cycle_review])
root.order.add_edge(seed_select, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_loop)
root.order.add_edge(climate_loop, growth_loop)
root.order.add_edge(growth_loop, waste_loop)
root.order.add_edge(waste_loop, cycle_review)