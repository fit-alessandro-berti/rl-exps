import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
SiteSurvey = Transition(label='Site Survey')
ClimateScan = Transition(label='Climate Scan')
ModuleSetup = Transition(label='Module Setup')
CropChoice = Transition(label='Crop Choice')
NutrientFeed = Transition(label='Nutrient Feed')
PestControl = Transition(label='Pest Control')
EnergyAudit = Transition(label='Energy Audit')
WasteCycle = Transition(label='Waste Cycle')
GrowthTrack = Transition(label='Growth Track')
DemandPlan = Transition(label='Demand Plan')
CommunityLink = Transition(label='Community Link')
RegulationCheck = Transition(label='Regulation Check')
SupplySync = Transition(label='Supply Sync')
SystemUpgrade = Transition(label='System Upgrade')
DataBackup = Transition(label='Data Backup')

# Define silent activities
Skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, ClimateScan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ModuleSetup, CropChoice])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[NutrientFeed, PestControl])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[EnergyAudit, WasteCycle])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[GrowthTrack, DemandPlan])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[CommunityLink, RegulationCheck])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[SupplySync, SystemUpgrade])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[DataBackup, Skip])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])

# Define the partial order
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, loop1)

# Print the result
print(root)