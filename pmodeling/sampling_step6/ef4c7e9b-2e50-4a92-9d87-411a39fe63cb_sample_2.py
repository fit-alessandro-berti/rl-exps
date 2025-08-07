import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process as a StrictPartialOrder
root = StrictPartialOrder(nodes=[
    seed_selection, nutrient_mix, environment_setup, pest_scan, light_control, growth_monitor,
    water_cycle, air_quality, robotic_harvest, quality_check, data_logging, packaging, waste_sort,
    energy_audit, retail_sync
])

# Define the dependencies between activities
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(seed_selection, environment_setup)
root.order.add_edge(seed_selection, pest_scan)
root.order.add_edge(nutrient_mix, environment_setup)
root.order.add_edge(nutrient_mix, pest_scan)
root.order.add_edge(environment_setup, light_control)
root.order.add_edge(environment_setup, air_quality)
root.order.add_edge(pest_scan, light_control)
root.order.add_edge(pest_scan, air_quality)
root.order.add_edge(light_control, water_cycle)
root.order.add_edge(air_quality, water_cycle)
root.order.add_edge(water_cycle, growth_monitor)
root.order.add_edge(growth_monitor, robotic_harvest)
root.order.add_edge(growth_monitor, quality_check)
root.order.add_edge(growth_monitor, data_logging)
root.order.add_edge(growth_monitor, waste_sort)
root.order.add_edge(growth_monitor, energy_audit)
root.order.add_edge(growth_monitor, retail_sync)

# Now, 'root' contains the POWL model for the urban vertical farming process.