import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SeedSelect = Transition(label='Seed Select')
TrendAnalyze = Transition(label='Trend Analyze')
NutrientMix = Transition(label='Nutrient Mix')
AutoPlant = Transition(label='Auto Plant')
SensorCheck = Transition(label='Sensor Check')
DataAnalyze = Transition(label='Data Analyze')
WaterAdjust = Transition(label='Water Adjust')
LightControl = Transition(label='Light Control')
HumidityMonitor = Transition(label='Humidity Monitor')
PestInspect = Transition(label='Pest Inspect')
GrowthForecast = Transition(label='Growth Forecast')
HarvestPlan = Transition(label='Harvest Plan')
RapidCool = Transition(label='Rapid Cool')
QualityGrade = Transition(label='Quality Grade')
EcoPackage = Transition(label='Eco Package')
LogisticsPrep = Transition(label='Logistics Prep')
FeedbackCollect = Transition(label='Feedback Collect')
SystemMaintain = Transition(label='System Maintain')

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[SensorCheck, DataAnalyze, WaterAdjust, LightControl, HumidityMonitor, PestInspect, GrowthForecast, HarvestPlan, RapidCool, QualityGrade, EcoPackage, LogisticsPrep, FeedbackCollect, SystemMaintain])
xor = OperatorPOWL(operator=Operator.XOR, children=[SeedSelect, TrendAnalyze, NutrientMix, AutoPlant])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)