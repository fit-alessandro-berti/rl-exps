import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
activities = ['Seed Select', 'Trend Analyze', 'Nutrient Mix', 'Auto Plant', 'Sensor Check', 'Data Analyze', 'Water Adjust', 'Light Control', 'Humidity Monitor', 'Pest Inspect', 'Growth Forecast', 'Harvest Plan', 'Rapid Cool', 'Quality Grade', 'Eco Package', 'Logistics Prep', 'Feedback Collect', 'System Maintain']
transitions = [Transition(label=activity) for activity in activities]

# Define the process flow
seed_select = transitions[0]
trend_analyze = transitions[1]
nutrient_mix = transitions[2]
auto_plant = transitions[3]
sensor_check = transitions[4]
data_analyze = transitions[5]
water_adjust = transitions[6]
light_control = transitions[7]
humidity_monitor = transitions[8]
pest_inspect = transitions[9]
growth_forecast = transitions[10]
harvest_plan = transitions[11]
rapid_cool = transitions[12]
quality_grade = transitions[13]
eco_package = transitions[14]
logistics_prep = transitions[15]
feedback_collect = transitions[16]
system_maintain = transitions[17]

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[trend_analyze, nutrient_mix])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[auto_plant, sensor_check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, water_adjust])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[light_control, humidity_monitor])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[pest_inspect, growth_forecast])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, rapid_cool])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[quality_grade, eco_package])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[logistics_prep, feedback_collect])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[system_maintain, seed_select])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[xor1, xor2])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[xor3, xor4])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[xor5, xor6])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[xor7, xor8])
xor14 = OperatorPOWL(operator=Operator.XOR, children=[xor9, xor10])
xor15 = OperatorPOWL(operator=Operator.XOR, children=[xor11, xor12])
xor16 = OperatorPOWL(operator=Operator.XOR, children=[xor13, xor14])
xor17 = OperatorPOWL(operator=Operator.XOR, children=[xor15, xor16])
xor18 = OperatorPOWL(operator=Operator.XOR, children=[xor17, seed_select])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, xor11, xor12, xor13, xor14, xor15, xor16, xor17, xor18])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, xor11)
root.order.add_edge(xor11, xor12)
root.order.add_edge(xor12, xor13)
root.order.add_edge(xor13, xor14)
root.order.add_edge(xor14, xor15)
root.order.add_edge(xor15, xor16)
root.order.add_edge(xor16, xor17)
root.order.add_edge(xor17, xor18)
root.order.add_edge(xor18, xor1)

print(root)