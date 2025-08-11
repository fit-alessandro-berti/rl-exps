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
growth_cycle = OperatorPOWL(operator=Operator.LOOP, children=[
    nutrient_mix,
    environment_setup,
    pest_scan,
    light_control,
    growth_monitor,
    water_cycle,
    air_quality,
    robotic_harvest,
    quality_check,
    data_logging
])

# Define the sequential activities after the growth cycle
post_growth_activities = OperatorPOWL(operator=Operator.XOR, children=[
    packaging,
    waste_sort,
    energy_audit,
    retail_sync
])

# Define the root POWL model
root = StrictPartialOrder(nodes=[growth_cycle, post_growth_activities])
root.order.add_edge(growth_cycle, post_growth_activities)

# Print the POWL model
print(root)