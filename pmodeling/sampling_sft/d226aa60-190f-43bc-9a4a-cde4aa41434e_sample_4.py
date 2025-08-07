import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
seed_select       = Transition(label='Seed Select')
trend_analyze      = Transition(label='Trend Analyze')
nutrient_mix       = Transition(label='Nutrient Mix')
auto_plant         = Transition(label='Auto Plant')
sensor_check       = Transition(label='Sensor Check')
data_analyze       = Transition(label='Data Analyze')
water_adjust       = Transition(label='Water Adjust')
light_control      = Transition(label='Light Control')
humidity_monitor   = Transition(label='Humidity Monitor')
pest_inspect       = Transition(label='Pest Inspect')
growth_forecast    = Transition(label='Growth Forecast')
harvest_plan       = Transition(label='Harvest Plan')
rapid_cool         = Transition(label='Rapid Cool')
quality_grade      = Transition(label='Quality Grade')
eco_package        = Transition(label='Eco Package')
logistics_prep     = Transition(label='Logistics Prep')
feedback_collect   = Transition(label='Feedback Collect')
system_maintain    = Transition(label='System Maintain')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    seed_select, trend_analyze, nutrient_mix,
    auto_plant, sensor_check, data_analyze,
    water_adjust, light_control, humidity_monitor,
    pest_inspect, growth_forecast, harvest_plan,
    rapid_cool, quality_grade, eco_package,
    logistics_prep, feedback_collect, system_maintain
])

# Add sequential dependencies
root.order.add_edge(seed_select, trend_analyze)
root.order.add_edge(trend_analyze, nutrient_mix)
root.order.add_edge(nutrient_mix, auto_plant)

# Plant and check start in parallel
root.order.add_edge(auto_plant, sensor_check)
root.order.add_edge(auto_plant, data_analyze)

# Continuous monitoring
root.order.add_edge(sensor_check, data_analyze)
root.order.add_edge(data_analyze, water_adjust)
root.order.add_edge(data_analyze, light_control)
root.order.add_edge(data_analyze, humidity_monitor)
root.order.add_edge(data_analyze, pest_inspect)

# Growth forecasting and harvest planning
root.order.add_edge(pest_inspect, growth_forecast)
root.order.add_edge(growth_forecast, harvest_plan)

# Harvest sequence
root.order.add_edge(harvest_plan, rapid_cool)
root.order.add_edge(harvest_plan, quality_grade)
root.order.add_edge(rapid_cool, eco_package)
root.order.add_edge(quality_grade, eco_package)

# Post‐harvest logistics and feedback
root.order.add_edge(eco_package, logistics_prep)
root.order.add_edge(logistics_prep, feedback_collect)

# Maintenance can start anytime after harvest
root.order.add_edge(feedback_collect, system_maintain)