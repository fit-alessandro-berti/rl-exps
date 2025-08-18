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

# Define partial order
root = StrictPartialOrder(nodes=[SiteAssess, PermitObtain, SoilTesting, CropSelect, IrrigationSetup, DrainageInstall, EnergyIntegrate, StaffTrain, PestControl, LogisticsPlan, SupplyCoordinate, DistributionMap, CommunityEngage, MonitoringSetup, YieldOptimize])

# Define dependencies
root.order.add_edge(SiteAssess, PermitObtain)
root.order.add_edge(PermitObtain, SoilTesting)
root.order.add_edge(SoilTesting, CropSelect)
root.order.add_edge(CropSelect, IrrigationSetup)
root.order.add_edge(IrrigationSetup, DrainageInstall)
root.order.add_edge(DrainageInstall, EnergyIntegrate)
root.order.add_edge(EnergyIntegrate, StaffTrain)
root.order.add_edge(StaffTrain, PestControl)
root.order.add_edge(PestControl, LogisticsPlan)
root.order.add_edge(LogisticsPlan, SupplyCoordinate)
root.order.add_edge(SupplyCoordinate, DistributionMap)
root.order.add_edge(DistributionMap, CommunityEngage)
root.order.add_edge(CommunityEngage, MonitoringSetup)
root.order.add_edge(MonitoringSetup, YieldOptimize)