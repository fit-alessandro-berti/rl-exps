from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_analysis = Transition(label='Site Analysis')
infrastructure_setup = Transition(label='Infrastructure Setup')
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    infrastructure_setup,
    seed_selection,
    nutrient_mix,
    planting_cycle,
    climate_adjust,
    growth_monitor,
    pest_control,
    harvesting_mode,
    quality_check,
    packaging_phase,
    cold_storage,
    order_dispatch,
    waste_recycling,
    system_maintain
])

# Define the order
root.order.add_edge(site_analysis, infrastructure_setup)
root.order.add_edge(infrastructure_setup, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, planting_cycle)
root.order.add_edge(planting_cycle, climate_adjust)
root.order.add_edge(climate_adjust, growth_monitor)
root.order.add_edge(growth_monitor, pest_control)
root.order.add_edge(pest_control, harvesting_mode)
root.order.add_edge(harvesting_mode, quality_check)
root.order.add_edge(quality_check, packaging_phase)
root.order.add_edge(packaging_phase, cold_storage)
root.order.add_edge(cold_storage, order_dispatch)
root.order.add_edge(order_dispatch, waste_recycling)
root.order.add_edge(waste_recycling, system_maintain)

# Return the root
print(root)