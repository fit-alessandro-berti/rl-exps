import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define partial order
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

# Define partial order dependencies
root.order.add_edge(site_analysis, infrastructure_setup)
root.order.add_edge(site_analysis, seed_selection)
root.order.add_edge(site_analysis, nutrient_mix)
root.order.add_edge(site_analysis, planting_cycle)
root.order.add_edge(infrastructure_setup, climate_adjust)
root.order.add_edge(infrastructure_setup, growth_monitor)
root.order.add_edge(infrastructure_setup, pest_control)
root.order.add_edge(infrastructure_setup, harvesting_mode)
root.order.add_edge(infrastructure_setup, quality_check)
root.order.add_edge(infrastructure_setup, packaging_phase)
root.order.add_edge(infrastructure_setup, cold_storage)
root.order.add_edge(infrastructure_setup, order_dispatch)
root.order.add_edge(infrastructure_setup, waste_recycling)
root.order.add_edge(infrastructure_setup, system_maintain)
root.order.add_edge(seed_selection, climate_adjust)
root.order.add_edge(seed_selection, growth_monitor)
root.order.add_edge(seed_selection, pest_control)
root.order.add_edge(seed_selection, harvesting_mode)
root.order.add_edge(seed_selection, quality_check)
root.order.add_edge(seed_selection, packaging_phase)
root.order.add_edge(seed_selection, cold_storage)
root.order.add_edge(seed_selection, order_dispatch)
root.order.add_edge(seed_selection, waste_recycling)
root.order.add_edge(seed_selection, system_maintain)
root.order.add_edge(nutrient_mix, climate_adjust)
root.order.add_edge(nutrient_mix, growth_monitor)
root.order.add_edge(nutrient_mix, pest_control)
root.order.add_edge(nutrient_mix, harvesting_mode)
root.order.add_edge(nutrient_mix, quality_check)
root.order.add_edge(nutrient_mix, packaging_phase)
root.order.add_edge(nutrient_mix, cold_storage)
root.order.add_edge(nutrient_mix, order_dispatch)
root.order.add_edge(nutrient_mix, waste_recycling)
root.order.add_edge(nutrient_mix, system_maintain)
root.order.add_edge(planting_cycle, climate_adjust)
root.order.add_edge(planting_cycle, growth_monitor)
root.order.add_edge(planting_cycle, pest_control)
root.order.add_edge(planting_cycle, harvesting_mode)
root.order.add_edge(planting_cycle, quality_check)
root.order.add_edge(planting_cycle, packaging_phase)
root.order.add_edge(planting_cycle, cold_storage)
root.order.add_edge(planting_cycle, order_dispatch)
root.order.add_edge(planting_cycle, waste_recycling)
root.order.add_edge(planting_cycle, system_maintain)
root.order.add_edge(climate_adjust, growth_monitor)
root.order.add_edge(climate_adjust, pest_control)
root.order.add_edge(climate_adjust, harvesting_mode)
root.order.add_edge(climate_adjust, quality_check)
root.order.add_edge(climate_adjust, packaging_phase)
root.order.add_edge(climate_adjust, cold_storage)
root.order.add_edge(climate_adjust, order_dispatch)
root.order.add_edge(climate_adjust, waste_recycling)
root.order.add_edge(climate_adjust, system_maintain)
root.order.add_edge(growth_monitor, pest_control)
root.order.add_edge(growth_monitor, harvesting_mode)
root.order.add_edge(growth_monitor, quality_check)
root.order.add_edge(growth_monitor, packaging_phase)
root.order.add_edge(growth_monitor, cold_storage)
root.order.add_edge(growth_monitor, order_dispatch)
root.order.add_edge(growth_monitor, waste_recycling)
root.order.add_edge(growth_monitor, system_maintain)
root.order.add_edge(pest_control, harvesting_mode)
root.order.add_edge(pest_control, quality_check)
root.order.add_edge(pest_control, packaging_phase)
root.order.add_edge(pest_control, cold_storage)
root.order.add_edge(pest_control, order_dispatch)
root.order.add_edge(pest_control, waste_recycling)
root.order.add_edge(pest_control, system_maintain)
root.order.add_edge(harvesting_mode, quality_check)
root.order.add_edge(harvesting_mode, packaging_phase)
root.order.add_edge(harvesting_mode, cold_storage)
root.order.add_edge(harvesting_mode, order_dispatch)
root.order.add_edge(harvesting_mode, waste_recycling)
root.order.add_edge(harvesting_mode, system_maintain)
root.order.add_edge(quality_check, packaging_phase)
root.order.add_edge(quality_check, cold_storage)
root.order.add_edge(quality_check, order_dispatch)
root.order.add_edge(quality_check, waste_recycling)
root.order.add_edge(quality_check, system_maintain)
root.order.add_edge(packaging_phase, cold_storage)
root.order.add_edge(packaging_phase, order_dispatch)
root.order.add_edge(packaging_phase, waste_recycling)
root.order.add_edge(packaging_phase, system_maintain)
root.order.add_edge(cold_storage, order_dispatch)
root.order.add_edge(cold_storage, waste_recycling)
root.order.add_edge(cold_storage, system_maintain)
root.order.add_edge(order_dispatch, waste_recycling)
root.order.add_edge(order_dispatch, system_maintain)
root.order.add_edge(waste_recycling, system_maintain)

print(root)