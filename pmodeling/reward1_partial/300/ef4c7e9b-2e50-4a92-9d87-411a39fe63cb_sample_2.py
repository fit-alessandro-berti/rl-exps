import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
environment_setup = Transition(label='Environment Setup')
pest_scan = Transition(label='Pest Scan')
light_control = Transition(label='Light Control')
growth_monitor = Transition(label='Growth Monitor')
water_cycle = Transition(label='Water Cycle')
air_quality = Transition(label='Air Quality')
robotic_harvest = Transition(label='Robotic Harvest')
quality_check = Transition(label='Quality Check')
data_logging = Transition(label='Data Logging')
packaging = Transition(label='Packaging')
waste_sort = Transition(label='Waste Sort')
energy_audit = Transition(label='Energy Audit')
retail_sync = Transition(label='Retail Sync')

# Define nodes and connections
seed_selection_node = StrictPartialOrder(nodes=[seed_selection])
nutrient_mix_node = StrictPartialOrder(nodes=[nutrient_mix])
environment_setup_node = StrictPartialOrder(nodes=[environment_setup])
pest_scan_node = StrictPartialOrder(nodes=[pest_scan])
light_control_node = StrictPartialOrder(nodes=[light_control])
growth_monitor_node = StrictPartialOrder(nodes=[growth_monitor])
water_cycle_node = StrictPartialOrder(nodes=[water_cycle])
air_quality_node = StrictPartialOrder(nodes=[air_quality])
robotic_harvest_node = StrictPartialOrder(nodes=[robotic_harvest])
quality_check_node = StrictPartialOrder(nodes=[quality_check])
data_logging_node = StrictPartialOrder(nodes=[data_logging])
packaging_node = StrictPartialOrder(nodes=[packaging])
waste_sort_node = StrictPartialOrder(nodes=[waste_sort])
energy_audit_node = StrictPartialOrder(nodes=[energy_audit])
retail_sync_node = StrictPartialOrder(nodes=[retail_sync])

# Connect nodes based on process flow
seed_selection_node.order.add_edge(seed_selection, nutrient_mix)
nutrient_mix_node.order.add_edge(nutrient_mix, environment_setup)
environment_setup_node.order.add_edge(environment_setup, pest_scan)
pest_scan_node.order.add_edge(pest_scan, light_control)
light_control_node.order.add_edge(light_control, growth_monitor)
growth_monitor_node.order.add_edge(growth_monitor, water_cycle)
water_cycle_node.order.add_edge(water_cycle, air_quality)
air_quality_node.order.add_edge(air_quality, robotic_harvest)
robotic_harvest_node.order.add_edge(robotic_harvest, quality_check)
quality_check_node.order.add_edge(quality_check, data_logging)
data_logging_node.order.add_edge(data_logging, packaging)
packaging_node.order.add_edge(packaging, waste_sort)
waste_sort_node.order.add_edge(waste_sort, energy_audit)
energy_audit_node.order.add_edge(energy_audit, retail_sync)

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    seed_selection_node,
    nutrient_mix_node,
    environment_setup_node,
    pest_scan_node,
    light_control_node,
    growth_monitor_node,
    water_cycle_node,
    air_quality_node,
    robotic_harvest_node,
    quality_check_node,
    data_logging_node,
    packaging_node,
    waste_sort_node,
    energy_audit_node,
    retail_sync_node
])