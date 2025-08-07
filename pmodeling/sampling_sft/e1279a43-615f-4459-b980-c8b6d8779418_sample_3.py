import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_analysis      = Transition(label='Site Analysis')
infra_setup        = Transition(label='Infrastructure Setup')
seed_selection     = Transition(label='Seed Selection')
nutrient_mix       = Transition(label='Nutrient Mix')
planting_cycle     = Transition(label='Planting Cycle')
climate_adjust     = Transition(label='Climate Adjust')
growth_monitor     = Transition(label='Growth Monitor')
pest_control       = Transition(label='Pest Control')
harvesting_mode    = Transition(label='Harvesting Mode')
quality_check      = Transition(label='Quality Check')
packaging_phase    = Transition(label='Packaging Phase')
cold_storage       = Transition(label='Cold Storage')
order_dispatch     = Transition(label='Order Dispatch')
waste_recycling    = Transition(label='Waste Recycling')
system_maintain    = Transition(label='System Maintain')

# Define the monitoring & control loop: monitor then adjust, repeated
monitor_control_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, pest_control]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    infra_setup,
    seed_selection,
    nutrient_mix,
    planting_cycle,
    climate_adjust,
    monitor_control_loop,
    harvesting_mode,
    quality_check,
    packaging_phase,
    cold_storage,
    order_dispatch,
    waste_recycling,
    system_maintain
])

# Add the control-flow edges
root.order.add_edge(site_analysis,   infra_setup)
root.order.add_edge(infra_setup,     seed_selection)
root.order.add_edge(seed_selection,  nutrient_mix)
root.order.add_edge(nutrient_mix,    planting_cycle)
root.order.add_edge(planting_cycle,  climate_adjust)
root.order.add_edge(climate_adjust,  monitor_control_loop)
root.order.add_edge(monitor_control_loop, harvesting_mode)
root.order.add_edge(harvesting_mode, quality_check)
root.order.add_edge(quality_check,   packaging_phase)
root.order.add_edge(packaging_phase, cold_storage)
root.order.add_edge(cold_storage,    order_dispatch)
root.order.add_edge(order_dispatch,  waste_recycling)
root.order.add_edge(waste_recycling, system_maintain)