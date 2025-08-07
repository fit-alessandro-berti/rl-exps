import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_selection   = Transition(label='Seed Selection')
nutrient_mix     = Transition(label='Nutrient Mix')
environment_check= Transition(label='Environment Check')
planting_setup   = Transition(label='Planting Setup')
growth_monitor   = Transition(label='Growth Monitoring')
pest_control     = Transition(label='Pest Control')
automated_harvest= Transition(label='Automated Harvest')
quality_inspect  = Transition(label='Quality Inspect')
packaging_prep   = Transition(label='Packaging Prep')
order_fulfill    = Transition(label='Order Fulfill')
local_delivery   = Transition(label='Local Delivery')
waste_collect    = Transition(label='Waste Collect')
biomass_process  = Transition(label='Biomass Process')
compost_create   = Transition(label='Compost Create')
energy_recover   = Transition(label='Energy Recover')
regulation_review= Transition(label='Regulation Review')
community_engage = Transition(label='Community Engage')

# Loop for continuous growth monitoring & pest control
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_control])

# Concurrent preparation of all outputs (delivery, waste, energy)
concurrent_outputs = StrictPartialOrder(nodes=[
    local_delivery,
    waste_collect,
    energy_recover
])
# No edges => all three run concurrently

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    nutrient_mix,
    environment_check,
    planting_setup,
    monitor_loop,
    quality_inspect,
    packaging_prep,
    order_fulfill,
    concurrent_outputs,
    regulation_review,
    community_engage
])

# Sequential dependencies
root.order.add_edge(seed_selection,    nutrient_mix)
root.order.add_edge(nutrient_mix,      environment_check)
root.order.add_edge(environment_check, planting_setup)
root.order.add_edge(planting_setup,    monitor_loop)
root.order.add_edge(monitor_loop,      quality_inspect)
root.order.add_edge(quality_inspect,   packaging_prep)
root.order.add_edge(packaging_prep,    order_fulfill)
root.order.add_edge(order_fulfill,     local_delivery)
root.order.add_edge(order_fulfill,     waste_collect)
root.order.add_edge(order_fulfill,     energy_recover)
root.order.add_edge(order_fulfill,     regulation_review)
root.order.add_edge(order_fulfill,     community_engage)