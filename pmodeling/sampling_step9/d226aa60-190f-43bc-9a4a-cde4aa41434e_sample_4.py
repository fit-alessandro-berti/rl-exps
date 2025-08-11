import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Seed_Select = Transition(label='Seed Select')
Trend_Analyze = Transition(label='Trend Analyze')
Nutrient_Mix = Transition(label='Nutrient Mix')
Auto_Plant = Transition(label='Auto Plant')
Sensor_Check = Transition(label='Sensor Check')
Data_Analyze = Transition(label='Data Analyze')
Water_Adjust = Transition(label='Water Adjust')
Light_Control = Transition(label='Light Control')
Humidity_Monitor = Transition(label='Humidity Monitor')
Pest_Inspect = Transition(label='Pest Inspect')
Growth_Forecast = Transition(label='Growth Forecast')
Harvest_Plan = Transition(label='Harvest Plan')
Rapid_Cool = Transition(label='Rapid Cool')
Quality_Grade = Transition(label='Quality Grade')
Eco_Package = Transition(label='Eco Package')
Logistics_Prep = Transition(label='Logistics Prep')
Feedback_Collect = Transition(label='Feedback Collect')
System_Maintain = Transition(label='System Maintain')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Seed_Select, Trend_Analyze])
xor = OperatorPOWL(operator=Operator.XOR, children=[Nutrient_Mix, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)