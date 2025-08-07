import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
env_setup = Transition(label='Environment Setup')
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

# Define the loop body: Growth Monitor -> Water Cycle -> Air Quality
growth_loop_body = StrictPartialOrder(nodes=[growth_monitor, water_cycle, air_quality])
growth_loop_body.order.add_edge(growth_monitor, water_cycle)
growth_loop_body.order.add_edge(water_cycle, air_quality)

# Loop operator: repeat the body until exit
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_loop_body, Transition(label='exit')])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    seed_selection, nutrient_mix, env_setup, pest_scan, light_control,
    growth_loop, quality_check, data_logging, packaging,
    waste_sort, energy_audit, retail_sync
])

# Define the control-flow dependencies
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, env_setup)
root.order.add_edge(env_setup, pest_scan)
root.order.add_edge(pest_scan, light_control)
root.order.add_edge(light_control, growth_loop)
root.order.add_edge(growth_loop, quality_check)
root.order.add_edge(quality_check, data_logging)
root.order.add_edge(data_logging, packaging)
root.order.add_edge(packaging, waste_sort)
root.order.add_edge(waste_sort, energy_audit)
root.order.add_edge(energy_audit, retail_sync)

print(root)