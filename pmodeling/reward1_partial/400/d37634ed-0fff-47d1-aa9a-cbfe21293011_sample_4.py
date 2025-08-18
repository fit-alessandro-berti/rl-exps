import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
env_check = Transition(label='Environment Check')
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

# Define the loop for waste biomass processing
biomass_loop = OperatorPOWL(operator=Operator.LOOP, children=[biomass_process, compost_create, energy_recover])

# Define the partial order for the main process
main_process = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, env_check, planting_setup, growth_monitoring, pest_control, automated_harvest, quality_inspect, packaging_prep, order_fulfill, local_delivery, waste_collect, biomass_loop])
main_process.order.add_edge(seed_selection, nutrient_mix)
main_process.order.add_edge(nutrient_mix, env_check)
main_process.order.add_edge(env_check, planting_setup)
main_process.order.add_edge(planting_setup, growth_monitoring)
main_process.order.add_edge(growth_monitoring, pest_control)
main_process.order.add_edge(pest_control, automated_harvest)
main_process.order.add_edge(automated_harvest, quality_inspect)
main_process.order.add_edge(quality_inspect, packaging_prep)
main_process.order.add_edge(packaging_prep, order_fulfill)
main_process.order.add_edge(order_fulfill, local_delivery)
main_process.order.add_edge(local_delivery, waste_collect)
main_process.order.add_edge(waste_collect, biomass_loop)

# Define the exclusive choice for regulation review and community engagement
regulation_choice = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, community_engage])

# Define the root node with the exclusive choice
root = StrictPartialOrder(nodes=[main_process, regulation_choice])
root.order.add_edge(main_process, regulation_choice)

# Print the root node
print(root)