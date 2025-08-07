import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
seed_selection    = Transition(label='Seed Selection')
nutrient_setup    = Transition(label='Nutrient Setup')
growth_monitoring = Transition(label='Growth Monitoring')
climate_adjust    = Transition(label='Climate Adjust')
pest_control      = Transition(label='Pest Control')
water_recirculate = Transition(label='Water Recirculate')
light_calibration = Transition(label='Light Calibration')
robotic_harvest   = Transition(label='Robotic Harvest')
quality_inspect   = Transition(label='Quality Inspect')
waste_process     = Transition(label='Waste Process')
energy_reuse      = Transition(label='Energy Reuse')
inventory_update  = Transition(label='Inventory Update')
demand_forecast   = Transition(label='Demand Forecast')
order_dispatch    = Transition(label='Order Dispatch')
community_event   = Transition(label='Community Event')
feedback_collect  = Transition(label='Feedback Collect')
data_analyze      = Transition(label='Data Analyze')

# Build the core growth cycle partial order
growth_cycle = StrictPartialOrder(nodes=[
    nutrient_setup,
    growth_monitoring,
    climate_adjust,
    pest_control,
    water_recirculate,
    light_calibration,
    robotic_harvest,
    quality_inspect,
    waste_process,
    energy_reuse
])
# Define the partial order dependencies
growth_cycle.order.add_edge(nutrient_setup, growth_monitoring)
growth_cycle.order.add_edge(growth_monitoring, climate_adjust)
growth_cycle.order.add_edge(growth_monitoring, pest_control)
growth_cycle.order.add_edge(climate_adjust, water_recirculate)
growth_cycle.order.add_edge(climate_adjust, light_calibration)
growth_cycle.order.add_edge(pest_control, water_recirculate)
growth_cycle.order.add_edge(pest_control, light_calibration)
growth_cycle.order.add_edge(water_recirculate, robotic_harvest)
growth_cycle.order.add_edge(light_calibration, robotic_harvest)
growth_cycle.order.add_edge(robotic_harvest, quality_inspect)
growth_cycle.order.add_edge(quality_inspect, waste_process)
growth_cycle.order.add_edge(quality_inspect, energy_reuse)

# Loop for continuous monitoring and adjustments
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_cycle, growth_cycle])

# Build the full process as a partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    monitor_loop,
    inventory_update,
    demand_forecast,
    order_dispatch,
    community_event,
    feedback_collect,
    data_analyze
])
# Define the control‐flow dependencies
root.order.add_edge(seed_selection, monitor_loop)
root.order.add_edge(monitor_loop, inventory_update)
root.order.add_edge(monitor_loop, demand_forecast)
root.order.add_edge(demand_forecast, order_dispatch)
root.order.add_edge(order_dispatch, community_event)
root.order.add_edge(community_event, feedback_collect)
root.order.add_edge(feedback_collect, data_analyze)

# Print the root model for verification
print(root)