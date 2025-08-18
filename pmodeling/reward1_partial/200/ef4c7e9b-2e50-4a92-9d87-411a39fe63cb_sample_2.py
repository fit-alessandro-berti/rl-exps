import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define silent transitions
skip = SilentTransition()

# Define loops
water_cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_cycle])
energy_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit])

# Define XOR
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging, waste_sort])

# Define the root process
root = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, environment_setup, pest_scan, light_control, growth_monitor, water_cycle_loop, energy_audit_loop, xor])
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, environment_setup)
root.order.add_edge(environment_setup, pest_scan)
root.order.add_edge(pest_scan, light_control)
root.order.add_edge(light_control, growth_monitor)
root.order.add_edge(growth_monitor, water_cycle_loop)
root.order.add_edge(water_cycle_loop, energy_audit_loop)
root.order.add_edge(energy_audit_loop, xor)
root.order.add_edge(xor, packaging)
root.order.add_edge(xor, waste_sort)

print(root)