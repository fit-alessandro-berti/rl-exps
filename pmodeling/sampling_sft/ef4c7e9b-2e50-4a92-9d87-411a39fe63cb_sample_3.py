import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
seed_selection   = Transition(label='Seed Selection')
nutrient_mix     = Transition(label='Nutrient Mix')
environment_setup= Transition(label='Environment Setup')
pest_scan        = Transition(label='Pest Scan')
light_control    = Transition(label='Light Control')
growth_monitor   = Transition(label='Growth Monitor')
water_cycle      = Transition(label='Water Cycle')
air_quality      = Transition(label='Air Quality')
robotic_harvest  = Transition(label='Robotic Harvest')
quality_check    = Transition(label='Quality Check')
data_logging     = Transition(label='Data Logging')
packaging        = Transition(label='Packaging')
waste_sort       = Transition(label='Waste Sort')
energy_audit     = Transition(label='Energy Audit')
retail_sync      = Transition(label='Retail Sync')

# Build the loop body for one cycle: Pest Scan -> Light Control -> Growth Monitor
body = StrictPartialOrder(nodes=[pest_scan, light_control, growth_monitor])
body.order.add_edge(pest_scan, light_control)
body.order.add_edge(light_control, growth_monitor)

# Define the loop: do Environment Setup, then optionally repeat the body
loop = OperatorPOWL(operator=Operator.LOOP, children=[environment_setup, body])

# Assemble the full partial‐order workflow
root = StrictPartialOrder(nodes=[
    loop,  # do Environment Setup, then optionally repeat Pest Scan -> Light Control -> Growth Monitor
    water_cycle,
    air_quality,
    robotic_harvest,
    quality_check,
    data_logging,
    packaging,
    waste_sort,
    energy_audit,
    retail_sync
])

# Sequential dependencies within the loop body
root.order.add_edge(loop, water_cycle)
root.order.add_edge(water_cycle, air_quality)
root.order.add_edge(air_quality, robotic_harvest)
root.order.add_edge(robotic_harvest, quality_check)
root.order.add_edge(quality_check, data_logging)
root.order.add_edge(data_logging, packaging)
root.order.add_edge(packaging, waste_sort)
root.order.add_edge(waste_sort, energy_audit)
root.order.add_edge(energy_audit, retail_sync)