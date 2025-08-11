import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SiteAssess = Transition(label='Site Assess')
PermitObtain = Transition(label='Permit Obtain')
SoilTesting = Transition(label='Soil Testing')
CropSelect = Transition(label='Crop Select')
IrrigationSetup = Transition(label='Irrigation Setup')
DrainageInstall = Transition(label='Drainage Install')
EnergyIntegrate = Transition(label='Energy Integrate')
StaffTrain = Transition(label='Staff Train')
PestControl = Transition(label='Pest Control')
LogisticsPlan = Transition(label='Logistics Plan')
SupplyCoordinate = Transition(label='Supply Coordinate')
DistributionMap = Transition(label='Distribution Map')
CommunityEngage = Transition(label='Community Engage')
MonitoringSetup = Transition(label='Monitoring Setup')
YieldOptimize = Transition(label='Yield Optimize')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SiteAssess, PermitObtain])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[EnergyIntegrate, skip])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[SoilTesting, CropSelect])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[IrrigationSetup, skip])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[DrainageInstall, LogisticsPlan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[SupplyCoordinate, skip])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[DistributionMap, PestControl])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[CommunityEngage, skip])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[MonitoringSetup, YieldOptimize])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[skip, skip])

# Define root model
root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, loop3, xor3, loop4, xor4, loop5, xor5])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)
root.order.add_edge(loop5, xor5)

# Print the root model
print(root)