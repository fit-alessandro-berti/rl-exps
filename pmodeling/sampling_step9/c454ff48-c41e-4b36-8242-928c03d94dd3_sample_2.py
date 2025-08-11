import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteAssess, PermitObtain, SoilTesting, CropSelect, IrrigationSetup, DrainageInstall, EnergyIntegrate, StaffTrain, PestControl, LogisticsPlan, SupplyCoordinate, DistributionMap, CommunityEngage, MonitoringSetup, YieldOptimize])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)