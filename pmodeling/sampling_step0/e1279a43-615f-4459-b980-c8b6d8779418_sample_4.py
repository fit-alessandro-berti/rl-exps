import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_analysis = Transition(label='Site Analysis')
infra_setup = Transition(label='Infrastructure Setup')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
planting_cycle = Transition(label='Planting Cycle')
climate_adjust = Transition(label='Climate Adjust')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvesting_mode = Transition(label='Harvesting Mode')
quality_check = Transition(label='Quality Check')
packaging_phase = Transition(label='Packaging Phase')
cold_storage = Transition(label='Cold Storage')
order_dispatch = Transition(label='Order Dispatch')
waste_recycling = Transition(label='Waste Recycling')
system_maintain = Transition(label='System Maintain')

# Define the loop for the plant growth cycle
plant_growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_control])

# Define the XOR for the production stages
production_stages_xor = OperatorPOWL(operator=Operator.XOR, children=[harvesting_mode, quality_check])

# Define the XOR for the packaging and cold storage
packaging_cold_storage_xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_phase, cold_storage])

# Define the XOR for the order dispatch and waste recycling
order_dispatch_waste_recycling_xor = OperatorPOWL(operator=Operator.XOR, children=[order_dispatch, waste_recycling])

# Define the XOR for the system maintenance and waste recycling
system_maintain_waste_recycling_xor = OperatorPOWL(operator=Operator.XOR, children=[system_maintain, waste_recycling])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    site_analysis,
    infra_setup,
    seed_selection,
    nutrient_mix,
    planting_cycle,
    climate_adjust,
    plant_growth_loop,
    production_stages_xor,
    packaging_cold_storage_xor,
    order_dispatch_waste_recycling_xor,
    system_maintain_waste_recycling_xor
])

# Add the dependencies
root.order.add_edge(site_analysis, infra_setup)
root.order.add_edge(infra_setup, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, planting_cycle)
root.order.add_edge(planting_cycle, climate_adjust)
root.order.add_edge(climate_adjust, plant_growth_loop)
root.order.add_edge(plant_growth_loop, production_stages_xor)
root.order.add_edge(production_stages_xor, packaging_cold_storage_xor)
root.order.add_edge(packaging_cold_storage_xor, order_dispatch_waste_recycling_xor)
root.order.add_edge(order_dispatch_waste_recycling_xor, system_maintain_waste_recycling_xor)

print(root)