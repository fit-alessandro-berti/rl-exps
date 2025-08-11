import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define sub-processes
subProcess1 = OperatorPOWL(operator=Operator.XOR, children=[SiteAssess, PermitObtain])
subProcess2 = OperatorPOWL(operator=Operator.XOR, children=[SoilTesting, CropSelect])
subProcess3 = OperatorPOWL(operator=Operator.XOR, children=[IrrigationSetup, DrainageInstall])
subProcess4 = OperatorPOWL(operator=Operator.XOR, children=[EnergyIntegrate, StaffTrain])
subProcess5 = OperatorPOWL(operator=Operator.XOR, children=[PestControl, LogisticsPlan])
subProcess6 = OperatorPOWL(operator=Operator.XOR, children=[SupplyCoordinate, DistributionMap])
subProcess7 = OperatorPOWL(operator=Operator.XOR, children=[CommunityEngage, MonitoringSetup])
subProcess8 = OperatorPOWL(operator=Operator.XOR, children=[YieldOptimize, skip])

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[subProcess1, subProcess2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[subProcess3, subProcess4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[subProcess5, subProcess6])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[subProcess7, subProcess8])

# Define root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop1)

print(root)