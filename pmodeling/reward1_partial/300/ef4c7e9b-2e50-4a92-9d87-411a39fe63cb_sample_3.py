import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the loop nodes
water_cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_cycle])
air_quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[air_quality])

# Define the exclusive choices
pest_scan_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, SilentTransition()])
light_control_choice = OperatorPOWL(operator=Operator.XOR, children=[light_control, SilentTransition()])

# Define the partial order
root = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, environment_setup, pest_scan_choice, light_control_choice, growth_monitor, water_cycle_loop, air_quality_loop, robotic_harvest, quality_check, data_logging, packaging, waste_sort, energy_audit, retail_sync])

# Define the order dependencies
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, environment_setup)
root.order.add_edge(environment_setup, pest_scan_choice)
root.order.add_edge(pest_scan_choice, light_control_choice)
root.order.add_edge(light_control_choice, growth_monitor)
root.order.add_edge(growth_monitor, water_cycle_loop)
root.order.add_edge(water_cycle_loop, air_quality_loop)
root.order.add_edge(air_quality_loop, robotic_harvest)
root.order.add_edge(robotic_harvest, quality_check)
root.order.add_edge(quality_check, data_logging)
root.order.add_edge(data_logging, packaging)
root.order.add_edge(packaging, waste_sort)
root.order.add_edge(waste_sort, energy_audit)
root.order.add_edge(energy_audit, retail_sync)

# Print the result
print(root)