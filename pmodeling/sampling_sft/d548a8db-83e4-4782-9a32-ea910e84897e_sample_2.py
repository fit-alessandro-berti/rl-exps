import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_selection = Transition(label='Seed Selection')
nutrient_setup = Transition(label='Nutrient Setup')
growth_monitoring = Transition(label='Growth Monitoring')
climate_adjust = Transition(label='Climate Adjust')
pest_control = Transition(label='Pest Control')
water_recirculate = Transition(label='Water Recirculate')
light_calibration = Transition(label='Light Calibration')
robotic_harvest = Transition(label='Robotic Harvest')
quality_inspect = Transition(label='Quality Inspect')
waste_process = Transition(label='Waste Process')
energy_reuse = Transition(label='Energy Reuse')
inventory_update = Transition(label='Inventory Update')
demand_forecast = Transition(label='Demand Forecast')
order_dispatch = Transition(label='Order Dispatch')
community_event = Transition(label='Community Event')
feedback_collect = Transition(label='Feedback Collect')
data_analyze = Transition(label='Data Analyze')

# Define the main production loop: Growth Monitoring -> Climate Adjust -> Pest Control -> Water Recirculate -> Light Calibration
production_loop = StrictPartialOrder(nodes=[
    growth_monitoring, climate_adjust, pest_control, water_recirculate, light_calibration
])
production_loop.order.add_edge(growth_monitoring, climate_adjust)
production_loop.order.add_edge(climate_adjust, pest_control)
production_loop.order.add_edge(pest_control, water_recirculate)
production_loop.order.add_edge(water_recirculate, light_calibration)

# Define the repeatable post-harvest loop: Robotic Harvest -> Quality Inspect -> Waste Process -> Energy Reuse
harvest_loop = StrictPartialOrder(nodes=[
    robotic_harvest, quality_inspect, waste_process, energy_reuse
])
harvest_loop.order.add_edge(robotic_harvest, quality_inspect)
harvest_loop.order.add_edge(quality_inspect, waste_process)
harvest_loop.order.add_edge(waste_process, energy_reuse)

# Define the loop: Production Loop, then optionally Harvest Loop repeated until exit
main_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[production_loop, harvest_loop]
)

# Assemble the overall process: initial setup, main production loop, demand forecast, order dispatch, community event, feedback collect, data analyze
root = StrictPartialOrder(nodes=[
    seed_selection, nutrient_setup, main_loop, demand_forecast, order_dispatch,
    community_event, feedback_collect, data_analyze
])
root.order.add_edge(seed_selection, nutrient_setup)
root.order.add_edge(nutrient_setup, main_loop)
root.order.add_edge(main_loop, demand_forecast)
root.order.add_edge(demand_forecast, order_dispatch)
root.order.add_edge(order_dispatch, community_event)
root.order.add_edge(community_event, feedback_collect)
root.order.add_edge(feedback_collect, data_analyze)