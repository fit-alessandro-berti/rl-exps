import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[ClimateScan, ModuleSetup])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[CropChoice, NutrientFeed])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[PestControl, EnergyAudit])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[WasteCycle, GrowthTrack])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[DemandPlan, CommunityLink])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[RegulationCheck, SupplySync])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[SystemUpgrade, DataBackup])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[SiteSurvey, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, skip])

root = StrictPartialOrder(nodes=[xor1, xor2, loop1, loop2, loop3, loop4, loop5, loop6, loop7])
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop2, loop4)
root.order.add_edge(loop3, loop5)
root.order.add_edge(loop4, loop6)
root.order.add_edge(loop5, loop7)
root.order.add_edge(loop6, xor2)
root.order.add_edge(loop7, xor2)

print(root)