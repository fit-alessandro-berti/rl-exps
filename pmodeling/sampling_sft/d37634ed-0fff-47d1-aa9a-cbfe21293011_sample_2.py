import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed = Transition(label='Seed Selection')
nutrient = Transition(label='Nutrient Mix')
env_check = Transition(label='Environment Check')
plant = Transition(label='Planting Setup')
growth = Transition(label='Growth Monitoring')
pest = Transition(label='Pest Control')
harvest = Transition(label='Automated Harvest')
inspect = Transition(label='Quality Inspect')
pack = Transition(label='Packaging Prep')
order = Transition(label='Order Fulfill')
delivery = Transition(label='Local Delivery')
waste_collect = Transition(label='Waste Collect')
biomass = Transition(label='Biomass Process')
compost = Transition(label='Compost Create')
energy = Transition(label='Energy Recover')
regulation = Transition(label='Regulation Review')
community = Transition(label='Community Engage')

# Loop for continuous growth monitoring and pest control
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth, pest])

# Build the partial order
root = StrictPartialOrder(nodes=[
    seed, nutrient, env_check, plant,
    growth_loop, harvest, inspect, pack,
    order, delivery,
    waste_collect, biomass, compost, energy,
    regulation, community
])

# Define the control-flow edges
root.order.add_edge(seed, nutrient)
root.order.add_edge(nutrient, env_check)
root.order.add_edge(env_check, plant)
root.order.add_edge(plant, growth_loop)
root.order.add_edge(growth_loop, harvest)
root.order.add_edge(harvest, inspect)
root.order.add_edge(inspect, pack)
root.order.add_edge(pack, order)
root.order.add_edge(order, delivery)

root.order.add_edge(order, waste_collect)
root.order.add_edge(waste_collect, biomass)
root.order.add_edge(biomass, compost)
root.order.add_edge(compost, energy)

root.order.add_edge(waste_collect, regulation)
root.order.add_edge(regulation, community)

# Final note: ensure all loops are in the same order
root.order.add_edge(growth_loop, growth)
root.order.add_edge(pest, growth_loop)

print(root)