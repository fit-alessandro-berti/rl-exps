import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control-flow operators
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, environment_check])
planting_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[planting_setup, growth_monitoring, pest_control])
quality_inspect_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, packaging_prep, order_fulfill])
local_delivery_loop = OperatorPOWL(operator=Operator.LOOP, children=[local_delivery, waste_collect, biomass_process])
compost_create_loop = OperatorPOWL(operator=Operator.LOOP, children=[compost_create, energy_recover])
regulation_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulation_review, community_engage])

# Define the partial order
root = StrictPartialOrder(nodes=[seed_selection, nutrient_mix_loop, planting_setup_loop, quality_inspect_loop, local_delivery_loop, compost_create_loop, regulation_review_loop])
root.order.add_edge(seed_selection, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, planting_setup_loop)
root.order.add_edge(planting_setup_loop, quality_inspect_loop)
root.order.add_edge(quality_inspect_loop, local_delivery_loop)
root.order.add_edge(local_delivery_loop, compost_create_loop)
root.order.add_edge(compost_create_loop, regulation_review_loop)