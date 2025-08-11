import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[ComplianceCheck, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[SupplyChain, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[CustomerEngage, skip])

# Define the loop node for monitoring data
loop = OperatorPOWL(operator=Operator.LOOP, children=[DataMonitor, YieldAnalyze])

# Define the root POWL model
root = StrictPartialOrder(nodes=[SiteSurvey, ClimateStudy, DesignLayout, SystemInstall, CropSelect, NutrientPlan, SensorSetup, AutomationTest, StaffTrain, xor1, xor2, xor3, loop])
root.order.add_edge(SiteSurvey, ClimateStudy)
root.order.add_edge(ClimateStudy, DesignLayout)
root.order.add_edge(DesignLayout, SystemInstall)
root.order.add_edge(SystemInstall, CropSelect)
root.order.add_edge(CropSelect, NutrientPlan)
root.order.add_edge(NutrientPlan, SensorSetup)
root.order.add_edge(SensorSetup, AutomationTest)
root.order.add_edge(AutomationTest, StaffTrain)
root.order.add_edge(StaffTrain, xor1)
root.order.add_edge(ComplianceCheck, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(SupplyChain, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(CustomerEngage, xor3)
root.order.add_edge(xor3, loop)
root.order.add_edge(loop, DataMonitor)
root.order.add_edge(DataMonitor, YieldAnalyze)
root.order.add_edge(YieldAnalyze, loop)

# Print the root POWL model
print(root)