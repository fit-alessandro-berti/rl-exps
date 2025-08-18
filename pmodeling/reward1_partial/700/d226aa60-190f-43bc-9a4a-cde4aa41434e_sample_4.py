import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop for sensor check and data analyze
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_check, data_analyze])

# Define the choice between nutrient mix and auto plant
nutrient_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, auto_plant])

# Define the loop for water adjust and light control
water_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_adjust, light_control])

# Define the loop for humidity monitor and pest inspect
humidity_loop = OperatorPOWL(operator=Operator.LOOP, children=[humidity_monitor, pest_inspect])

# Define the loop for growth forecast and harvest plan
forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_forecast, harvest_plan])

# Define the loop for rapid cool and quality grade
cool_loop = OperatorPOWL(operator=Operator.LOOP, children=[rapid_cool, quality_grade])

# Define the loop for eco package and logistics prep
package_loop = OperatorPOWL(operator=Operator.LOOP, children=[eco_package, logistics_prep])

# Define the loop for feedback collect and system maintain
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_collect, system_maintain])

# Define the root
root = StrictPartialOrder(nodes=[seed_select, trend_analyze, nutrient_choice, sensor_loop, water_loop, humidity_loop, forecast_loop, cool_loop, package_loop, feedback_loop])
root.order.add_edge(seed_select, trend_analyze)
root.order.add_edge(trend_analyze, nutrient_choice)
root.order.add_edge(nutrient_choice, sensor_loop)
root.order.add_edge(sensor_loop, water_loop)
root.order.add_edge(water_loop, humidity_loop)
root.order.add_edge(humidity_loop, forecast_loop)
root.order.add_edge(forecast_loop, cool_loop)
root.order.add_edge(cool_loop, package_loop)
root.order.add_edge(package_loop, feedback_loop)
root.order.add_edge(feedback_loop, seed_select)