import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the loop for biomass processing
biomass_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_collect, biomass_process, compost_create, energy_recover])

# Define the XOR for quality inspection and packaging preparation
xor_inspect_pack = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, packaging_prep])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, environment_check, planting_setup, growth_monitoring, pest_control, automated_harvest, xor_inspect_pack, order_fulfill, local_delivery, biomass_loop, regulation_review, community_engage])

# Add the dependencies
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, environment_check)
root.order.add_edge(environment_check, planting_setup)
root.order.add_edge(planting_setup, growth_monitoring)
root.order.add_edge(growth_monitoring, pest_control)
root.order.add_edge(pest_control, automated_harvest)
root.order.add_edge(automated_harvest, xor_inspect_pack)
root.order.add_edge(xor_inspect_pack, order_fulfill)
root.order.add_edge(order_fulfill, local_delivery)
root.order.add_edge(local_delivery, biomass_loop)
root.order.add_edge(biomass_loop, regulation_review)
root.order.add_edge(regulation_review, community_engage)

print(root)