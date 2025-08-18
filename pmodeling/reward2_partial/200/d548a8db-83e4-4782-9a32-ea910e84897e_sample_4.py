import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

root = StrictPartialOrder(nodes=[
    seed_selection, nutrient_setup, growth_monitoring, climate_adjust, pest_control,
    water_recirculate, light_calibration, robotic_harvest, quality_inspect, waste_process,
    energy_reuse, inventory_update, demand_forecast, order_dispatch, community_event,
    feedback_collect, data_analyze
])

# Define dependencies between activities
root.order.add_edge(seed_selection, nutrient_setup)
root.order.add_edge(nutrient_setup, growth_monitoring)
root.order.add_edge(growth_monitoring, climate_adjust)
root.order.add_edge(climate_adjust, pest_control)
root.order.add_edge(pest_control, water_recirculate)
root.order.add_edge(water_recirculate, light_calibration)
root.order.add_edge(light_calibration, robotic_harvest)
root.order.add_edge(robotic_harvest, quality_inspect)
root.order.add_edge(quality_inspect, waste_process)
root.order.add_edge(waste_process, energy_reuse)
root.order.add_edge(energy_reuse, inventory_update)
root.order.add_edge(inventory_update, demand_forecast)
root.order.add_edge(demand_forecast, order_dispatch)
root.order.add_edge(order_dispatch, community_event)
root.order.add_edge(community_event, feedback_collect)
root.order.add_edge(feedback_collect, data_analyze)