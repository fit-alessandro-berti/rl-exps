import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
environment_check = Transition(label='Environment Check')
planting_setup = Transition(label='Planting Setup')
growth_monitoring = Transition(label='Growth Monitoring')
pest_control = Transition(label='Pest Control')
automated_harvest = Transition(label='Automated Harvest')
quality_inspect = Transition(label='Quality Inspect')
packaging_prep = Transition(label='Packaging Prep')
order_fulfill = Transition(label='Order Fulfill')
local_delivery = Transition(label='Local Delivery')
waste_collect = Transition(label='Waste Collect')
biomass_process = Transition(label='Biomass Process')
compost_create = Transition(label='Compost Create')
energy_recover = Transition(label='Energy Recover')
regulation_review = Transition(label='Regulation Review')
community_engage = Transition(label='Community Engage')

skip = SilentTransition()

loop_seed = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, nutrient_mix, environment_check, planting_setup, growth_monitoring, pest_control])
loop_harvest = OperatorPOWL(operator=Operator.LOOP, children=[automated_harvest, quality_inspect, packaging_prep, order_fulfill])
loop_delivery = OperatorPOWL(operator=Operator.LOOP, children=[local_delivery, waste_collect, biomass_process, compost_create, energy_recover])
loop_review = OperatorPOWL(operator=Operator.LOOP, children=[regulation_review, community_engage])

xor_harvest_delivery = OperatorPOWL(operator=Operator.XOR, children=[loop_harvest, loop_delivery])
xor_harvest_review = OperatorPOWL(operator=Operator.XOR, children=[loop_harvest, loop_review])
xor_delivery_review = OperatorPOWL(operator=Operator.XOR, children=[loop_delivery, loop_review])

root = StrictPartialOrder(nodes=[loop_seed, xor_harvest_delivery, xor_harvest_review, xor_delivery_review])
root.order.add_edge(loop_seed, xor_harvest_delivery)
root.order.add_edge(loop_seed, xor_harvest_review)
root.order.add_edge(loop_seed, xor_delivery_review)
root.order.add_edge(xor_harvest_delivery, xor_harvest_review)
root.order.add_edge(xor_harvest_delivery, xor_delivery_review)
root.order.add_edge(xor_harvest_review, xor_delivery_review)