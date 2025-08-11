import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop for monitoring setup and yield optimization
loop = OperatorPOWL(operator=Operator.LOOP, children=[MonitoringSetup, YieldOptimize])

# Define the XOR for staff training and pest control
xor = OperatorPOWL(operator=Operator.XOR, children=[StaffTrain, PestControl])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[SiteAssess, PermitObtain, SoilTesting, CropSelect, IrrigationSetup, DrainageInstall, EnergyIntegrate, xor, loop])
root.order.add_edge(SiteAssess, PermitObtain)
root.order.add_edge(PermitObtain, SoilTesting)
root.order.add_edge(SoilTesting, CropSelect)
root.order.add_edge(CropSelect, IrrigationSetup)
root.order.add_edge(IrrigationSetup, DrainageInstall)
root.order.add_edge(DrainageInstall, EnergyIntegrate)
root.order.add_edge(EnergyIntegrate, xor)
root.order.add_edge(xor, loop)