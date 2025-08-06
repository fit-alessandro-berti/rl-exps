import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transition for the 'skip' activity
skip = SilentTransition()

# Define the loop for the 'light control' and 'water cycle' activities
light_loop = OperatorPOWL(operator=Operator.LOOP, children=[light_control, water_cycle])
water_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_control, light_control])

# Define the XOR for the 'quality check' and 'robotic harvest' activities
xor = OperatorPOWL(operator=Operator.XOR, children=[quality_check, robotic_harvest])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[environment_setup, nutrient_mix, light_loop, water_loop, pest_scan, air_quality, xor, seed_selection, data_logging, packaging, waste_sort, energy_audit, retail_sync])

# Define the order between the nodes
root.order.add_edge(environment_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, environment_setup)
root.order.add_edge(environment_setup, light_loop)
root.order.add_edge(light_loop, environment_setup)
root.order.add_edge(environment_setup, water_loop)
root.order.add_edge(water_loop, environment_setup)
root.order.add_edge(pest_scan, light_loop)
root.order.add_edge(light_loop, pest_scan)
root.order.add_edge(pest_scan, water_loop)
root.order.add_edge(water_loop, pest_scan)
root.order.add_edge(air_quality, light_loop)
root.order.add_edge(light_loop, air_quality)
root.order.add_edge(air_quality, water_loop)
root.order.add_edge(water_loop, air_quality)
root.order.add_edge(light_loop, xor)
root.order.add_edge(xor, light_loop)
root.order.add_edge(light_loop, quality_check)
root.order.add_edge(quality_check, light_loop)
root.order.add_edge(light_loop, robotic_harvest)
root.order.add_edge(robotic_harvest, light_loop)
root.order.add_edge(robotic_harvest, data_logging)
root.order.add_edge(data_logging, robotic_harvest)
root.order.add_edge(data_logging, packaging)
root.order.add_edge(packaging, data_logging)
root.order.add_edge(packaging, waste_sort)
root.order.add_edge(waste_sort, packaging)
root.order.add_edge(waste_sort, energy_audit)
root.order.add_edge(energy_audit, waste_sort)
root.order.add_edge(energy_audit, retail_sync)
root.order.add_edge(retail_sync, energy_audit)
root.order.add_edge(retail_sync, seed_selection)
root.order.add_edge(seed_selection, retail_sync)

# Return the root of the POWL model
return root