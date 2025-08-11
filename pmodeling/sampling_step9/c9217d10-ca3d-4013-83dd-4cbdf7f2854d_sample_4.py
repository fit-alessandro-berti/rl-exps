import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
ClimateStudy = Transition(label='Climate Study')
DesignLayout = Transition(label='Design Layout')
SystemInstall = Transition(label='System Install')
CropSelect = Transition(label='Crop Select')
NutrientPlan = Transition(label='Nutrient Plan')
SensorSetup = Transition(label='Sensor Setup')
AutomationTest = Transition(label='Automation Test')
StaffTrain = Transition(label='Staff Train')
ComplianceCheck = Transition(label='Compliance Check')
MarketingSync = Transition(label='Marketing Sync')
DataMonitor = Transition(label='Data Monitor')
YieldAnalyze = Transition(label='Yield Analyze')
SupplyChain = Transition(label='Supply Chain')
CustomerEngage = Transition(label='Customer Engage')
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, ClimateStudy, DesignLayout, SystemInstall, CropSelect, NutrientPlan, SensorSetup, AutomationTest, StaffTrain, ComplianceCheck, MarketingSync, DataMonitor, YieldAnalyze, SupplyChain, CustomerEngage])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)