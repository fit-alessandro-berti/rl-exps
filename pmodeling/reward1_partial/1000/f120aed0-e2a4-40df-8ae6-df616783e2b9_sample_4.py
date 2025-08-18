import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
SiteSurvey = Transition(label='Site Survey')
RackDesign = Transition(label='Rack Design')
SystemSetup = Transition(label='System Setup')
ClimateCalibrate = Transition(label='Climate Calibrate')
NutrientPrep = Transition(label='Nutrient Prep')
CropSelect = Transition(label='Crop Select')
SeedGerminate = Transition(label='Seed Germinate')
SensorDeploy = Transition(label='Sensor Deploy')
PestControl = Transition(label='Pest Control')
HarvestAutomate = Transition(label='Harvest Automate')
QualityCheck = Transition(label='Quality Check')
PackProduce = Transition(label='Pack Produce')
DataAnalyze = Transition(label='Data Analyze')
EngageCommunity = Transition(label='Engage Community')
LogisticsPlan = Transition(label='Logistics Plan')

root = StrictPartialOrder(nodes=[SiteSurvey, RackDesign, SystemSetup, ClimateCalibrate, NutrientPrep, CropSelect, SeedGerminate, SensorDeploy, PestControl, HarvestAutomate, QualityCheck, PackProduce, DataAnalyze, EngageCommunity, LogisticsPlan])

# Define the partial order dependencies
root.order.add_edge(SiteSurvey, RackDesign)
root.order.add_edge(RackDesign, SystemSetup)
root.order.add_edge(SystemSetup, ClimateCalibrate)
root.order.add_edge(ClimateCalibrate, NutrientPrep)
root.order.add_edge(NutrientPrep, CropSelect)
root.order.add_edge(CropSelect, SeedGerminate)
root.order.add_edge(SeedGerminate, SensorDeploy)
root.order.add_edge(SensorDeploy, PestControl)
root.order.add_edge(PestControl, HarvestAutomate)
root.order.add_edge(HarvestAutomate, QualityCheck)
root.order.add_edge(QualityCheck, PackProduce)
root.order.add_edge(PackProduce, DataAnalyze)
root.order.add_edge(DataAnalyze, EngageCommunity)
root.order.add_edge(EngageCommunity, LogisticsPlan)

# Print the POWL model
print(root)