import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Define the loop for the growth cycle
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, environment_setup, pest_scan, light_control, growth_monitor, water_cycle, air_quality, robotic_harvest, quality_check, data_logging, packaging, waste_sort, energy_audit, retail_sync])

# Define the XOR for the post-harvest activities
post_harvest_xor = OperatorPOWL(operator=Operator.XOR, children=[retail_sync, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[growth_loop, post_harvest_xor])
root.order.add_edge(growth_loop, post_harvest_xor)