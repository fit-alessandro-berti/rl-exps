import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_selection   = Transition(label='Seed Selection')
nutrient_mix     = Transition(label='Nutrient Mix')
environment_setup = Transition(label='Environment Setup')
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

# Define the growth cycle as a partial order
growth_cycle = StrictPartialOrder(nodes=[
    environment_setup,
    pest_scan,
    light_control,
    growth_monitor,
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

# Define the overall process as a loop:
# 1. Execute the growth cycle
# 2. Optionally do retail sync and exit, otherwise repeat from Environment Setup
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_cycle, retail_sync]
)

# Build the root partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    nutrient_mix,
    loop
])

# Add dependencies
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, loop)

print(root)