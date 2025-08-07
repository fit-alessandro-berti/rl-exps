import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
seed_selection      = Transition(label='Seed Selection')
nutrient_mix        = Transition(label='Nutrient Mix')
env_check           = Transition(label='Environment Check')
planting_setup      = Transition(label='Planting Setup')
growth_monitoring   = Transition(label='Growth Monitoring')
pest_control        = Transition(label='Pest Control')
automated_harvest   = Transition(label='Automated Harvest')
quality_inspect     = Transition(label='Quality Inspect')
packaging_prep      = Transition(label='Packaging Prep')
order_fulfill       = Transition(label='Order Fulfill')
local_delivery      = Transition(label='Local Delivery')
waste_collect       = Transition(label='Waste Collect')
biomass_process     = Transition(label='Biomass Process')
compost_create      = Transition(label='Compost Create')
energy_recover      = Transition(label='Energy Recover')
regulation_review   = Transition(label='Regulation Review')
community_engage    = Transition(label='Community Engage')

# Define the inner loop body (growing cycle)
inner_loop = StrictPartialOrder(nodes=[
    growth_monitoring, pest_control, automated_harvest, quality_inspect
])
inner_loop.order.add_edge(growth_monitoring, pest_control)
inner_loop.order.add_edge(pest_control, automated_harvest)
inner_loop.order.add_edge(automated_harvest, quality_inspect)

# LOOP: after each planting setup, do the inner loop and then optionally do community engage
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[planting_setup, inner_loop, community_engage]
)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    seed_selection, nutrient_mix, env_check, loop,
    packaging_prep, order_fulfill, local_delivery,
    waste_collect, biomass_process, compost_create,
    energy_recover, regulation_review
])

# Define the control‐flow dependencies
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, env_check)
root.order.add_edge(env_check, loop)

# After the loop, the sequence continues through packaging, fulfillment, delivery, and waste handling
root.order.add_edge(loop, packaging_prep)
root.order.add_edge(packaging_prep, order_fulfill)
root.order.add_edge(order_fulfill, local_delivery)
root.order.add_edge(local_delivery, waste_collect)

# Waste processing and energy recovery happen after waste collection
root.order.add_edge(waste_collect, biomass_process)
root.order.add_edge(biomass_process, compost_create)
root.order.add_edge(biomass_process, energy_recover)

# Finally, review regulations and engage community after all other steps
root.order.add_edge(compost_create, regulation_review)
root.order.add_edge(energy_recover, regulation_review)
root.order.add_edge(regulation_review, community_engage)