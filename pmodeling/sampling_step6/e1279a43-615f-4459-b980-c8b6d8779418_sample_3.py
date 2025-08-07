import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL nodes
site_analysis = Transition(label='Site Analysis')
infrastructure_setup = Transition(label='Infrastructure Setup')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
planting_cycle = Transition(label='Planting Cycle')
climate_adjust = Transition(label='Climate Adjust')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvesting_mode = Transition(label='Harvesting Mode')
quality_check = Transition(label='Quality Check')
packaging_phase = Transition(label='Packaging Phase')
cold_storage = Transition(label='Cold Storage')
order_dispatch = Transition(label='Order Dispatch')
waste_recycling = Transition(label='Waste Recycling')
system_maintain = Transition(label='System Maintain')

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    infrastructure_setup,
    seed_selection,
    nutrient_mix,
    planting_cycle,
    climate_adjust,
    growth_monitor,
    pest_control,
    harvesting_mode,
    quality_check,
    packaging_phase,
    cold_storage,
    order_dispatch,
    waste_recycling,
    system_maintain
])

# Since there are no dependencies specified in the problem, we assume all activities are concurrent
# This means there are no edges in the order set

# Print the root of the POWL model
print(root)