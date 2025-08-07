import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    seed_selection, nutrient_mix, environment_check, planting_setup, growth_monitoring, pest_control, automated_harvest,
    quality_inspect, packaging_prep, order_fulfill, local_delivery, waste_collect, biomass_process, compost_create,
    energy_recover, regulation_review, community_engage
])

# Define the flow of activities
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, environment_check)
root.order.add_edge(environment_check, planting_setup)
root.order.add_edge(planting_setup, growth_monitoring)
root.order.add_edge(growth_monitoring, pest_control)
root.order.add_edge(pest_control, automated_harvest)
root.order.add_edge(automated_harvest, quality_inspect)
root.order.add_edge(quality_inspect, packaging_prep)
root.order.add_edge(packaging_prep, order_fulfill)
root.order.add_edge(order_fulfill, local_delivery)
root.order.add_edge(local_delivery, waste_collect)
root.order.add_edge(waste_collect, biomass_process)
root.order.add_edge(biomass_process, compost_create)
root.order.add_edge(compost_create, energy_recover)
root.order.add_edge(energy_recover, regulation_review)
root.order.add_edge(regulation_review, community_engage)