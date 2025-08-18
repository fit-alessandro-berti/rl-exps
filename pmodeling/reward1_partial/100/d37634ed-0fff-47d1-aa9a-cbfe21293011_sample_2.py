from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
env_check = Transition(label='Environment Check')
plant_setup = Transition(label='Planting Setup')
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

# Define operators for exclusive choice and loop
xor_operator = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, env_check])
loop_operator = OperatorPOWL(operator=Operator.LOOP, children=[plant_setup, growth_monitoring, pest_control, automated_harvest, quality_inspect])

# Define the root Partial Order
root = StrictPartialOrder(nodes=[seed_selection, xor_operator, loop_operator, packaging_prep, order_fulfill, local_delivery, waste_collect, biomass_process, compost_create, energy_recover, regulation_review, community_engage])

# Add dependencies between nodes
root.order.add_edge(seed_selection, xor_operator)
root.order.add_edge(seed_selection, loop_operator)
root.order.add_edge(xor_operator, packaging_prep)
root.order.add_edge(loop_operator, packaging_prep)
root.order.add_edge(packaging_prep, order_fulfill)
root.order.add_edge(order_fulfill, local_delivery)
root.order.add_edge(local_delivery, waste_collect)
root.order.add_edge(waste_collect, biomass_process)
root.order.add_edge(biomass_process, compost_create)
root.order.add_edge(compost_create, energy_recover)
root.order.add_edge(energy_recover, regulation_review)
root.order.add_edge(regulation_review, community_engage)
root.order.add_edge(community_engage, seed_selection)

print(root)