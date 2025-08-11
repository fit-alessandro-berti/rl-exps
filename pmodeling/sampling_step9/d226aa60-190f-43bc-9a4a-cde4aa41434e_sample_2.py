import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[auto_plant, nutrient_mix])
xor = OperatorPOWL(operator=Operator.XOR, children=[pest_inspect, skip])

# Define root
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)