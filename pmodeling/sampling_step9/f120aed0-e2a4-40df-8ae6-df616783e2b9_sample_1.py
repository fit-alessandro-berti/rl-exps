import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, RackDesign, SystemSetup, ClimateCalibrate, NutrientPrep, CropSelect, SeedGerminate, SensorDeploy, PestControl, HarvestAutomate, QualityCheck, PackProduce, DataAnalyze, EngageCommunity, LogisticsPlan])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)