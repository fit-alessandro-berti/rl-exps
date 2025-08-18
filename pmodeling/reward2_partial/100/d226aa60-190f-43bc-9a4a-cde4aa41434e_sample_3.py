import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with exact names
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

# Define the workflow
root = StrictPartialOrder(nodes=[
    SeedSelect, TrendAnalyze, NutrientMix, AutoPlant, SensorCheck,
    DataAnalyze, WaterAdjust, LightControl, HumidityMonitor, PestInspect,
    GrowthForecast, HarvestPlan, RapidCool, QualityGrade, EcoPackage,
    LogisticsPrep, FeedbackCollect, SystemMaintain
])

# Define dependencies between transitions (POWL order)
root.order.add_edge(SeedSelect, TrendAnalyze)
root.order.add_edge(TrendAnalyze, NutrientMix)
root.order.add_edge(NutrientMix, AutoPlant)
root.order.add_edge(AutoPlant, SensorCheck)
root.order.add_edge(SensorCheck, DataAnalyze)
root.order.add_edge(DataAnalyze, WaterAdjust)
root.order.add_edge(WaterAdjust, LightControl)
root.order.add_edge(LightControl, HumidityMonitor)
root.order.add_edge(HumidityMonitor, PestInspect)
root.order.add_edge(PestInspect, GrowthForecast)
root.order.add_edge(GrowthForecast, HarvestPlan)
root.order.add_edge(HarvestPlan, RapidCool)
root.order.add_edge(RapidCool, QualityGrade)
root.order.add_edge(QualityGrade, EcoPackage)
root.order.add_edge(EcoPackage, LogisticsPrep)
root.order.add_edge(LogisticsPrep, FeedbackCollect)
root.order.add_edge(FeedbackCollect, SystemMaintain)