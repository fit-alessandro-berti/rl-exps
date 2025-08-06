import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
seed_select = Transition(label='Seed Select')
trend_analyze = Transition(label='Trend Analyze')
nutrient_mix = Transition(label='Nutrient Mix')
auto_plant = Transition(label='Auto Plant')
sensor_check = Transition(label='Sensor Check')
data_analyze = Transition(label='Data Analyze')
water_adjust = Transition(label='Water Adjust')
light_control = Transition(label='Light Control')
humidity_monitor = Transition(label='Humidity Monitor')
pest_inspect = Transition(label='Pest Inspect')
growth_forecast = Transition(label='Growth Forecast')
harvest_plan = Transition(label='Harvest Plan')
rapid_cool = Transition(label='Rapid Cool')
quality_grade = Transition(label='Quality Grade')
eco_package = Transition(label='Eco Package')
logistics_prep = Transition(label='Logistics Prep')
feedback_collect = Transition(label='Feedback Collect')
system_maintain = Transition(label='System Maintain')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, sensor_check, data_analyze, water_adjust, light_control, humidity_monitor, pest_inspect, growth_forecast, harvest_plan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[rapid_cool, quality_grade, eco_package])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[logistics_prep, feedback_collect, system_maintain])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])

root = StrictPartialOrder(nodes=[seed_select, trend_analyze, xor1, xor2, xor3])
root.order.add_edge(seed_select, trend_analyze)
root.order.add_edge(trend_analyze, xor1)
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, loop3)
root.order.add_edge(loop1, data_analyze)
root.order.add_edge(loop2, quality_grade)
root.order.add_edge(loop3, feedback_collect)

print(root)