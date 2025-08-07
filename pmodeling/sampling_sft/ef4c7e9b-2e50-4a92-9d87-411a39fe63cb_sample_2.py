import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
seed_selection   = Transition(label='Seed Selection')
nutrient_mix     = Transition(label='Nutrient Mix')
env_setup        = Transition(label='Environment Setup')
pest_scan        = Transition(label='Pest Scan')
light_control    = Transition(label='Light Control')
water_cycle      = Transition(label='Water Cycle')
air_quality      = Transition(label='Air Quality')
growth_monitor   = Transition(label='Growth Monitor')
robotic_harvest  = Transition(label='Robotic Harvest')
quality_check    = Transition(label='Quality Check')
data_logging     = Transition(label='Data Logging')
packaging        = Transition(label='Packaging')
waste_sort       = Transition(label='Waste Sort')
energy_audit     = Transition(label='Energy Audit')
retail_sync      = Transition(label='Retail Sync')

# Silent transition for loop exit
skip = SilentTransition()

# Loop body: Pest Scan -> Light Control -> Water Cycle -> Air Quality -> Growth Monitor
loop_body = StrictPartialOrder(nodes=[
    pest_scan, light_control, water_cycle, air_quality, growth_monitor
])
loop_body.order.add_edge(pest_scan, light_control)
loop_body.order.add_edge(light_control, water_cycle)
loop_body.order.add_edge(water_cycle, air_quality)
loop_body.order.add_edge(air_quality, growth_monitor)

# Loop: Environment Setup, then optionally execute loop_body repeatedly, then exit
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[env_setup, loop_body]
)

# After harvest, do Quality Check -> Data Logging -> Packaging -> Waste Sort -> Energy Audit -> Retail Sync
post_harvest = StrictPartialOrder(nodes=[
    quality_check, data_logging, packaging, waste_sort, energy_audit, retail_sync
])
post_harvest.order.add_edge(quality_check, data_logging)
post_harvest.order.add_edge(data_logging, packaging)
post_harvest.order.add_edge(packaging, waste_sort)
post_harvest.order.add_edge(waste_sort, energy_audit)
post_harvest.order.add_edge(energy_audit, retail_sync)

# Root partial order: Seed Selection -> Nutrient Mix -> loop -> post_harvest
root = StrictPartialOrder(nodes=[
    seed_selection, nutrient_mix, loop, post_harvest
])
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, loop)
root.order.add_edge(loop, post_harvest)