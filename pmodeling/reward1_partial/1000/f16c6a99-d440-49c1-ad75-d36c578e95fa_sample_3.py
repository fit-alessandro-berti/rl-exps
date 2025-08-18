import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
SensorDeploy = Transition(label='Sensor Deploy')
CropSelect = Transition(label='Crop Select')
SystemInstall = Transition(label='System Install')
EnergySetup = Transition(label='Energy Setup')
WaterCycle = Transition(label='Water Cycle')
PestControl = Transition(label='Pest Control')
RegulatoryCheck = Transition(label='Regulatory Check')
StaffTraining = Transition(label='Staff Training')
DataConfigure = Transition(label='Data Configure')
SupplyPlan = Transition(label='Supply Plan')
HarvestSchedule = Transition(label='Harvest Schedule')
QualityAudit = Transition(label='Quality Audit')
MarketLaunch = Transition(label='Market Launch')
FeedbackLoop = Transition(label='Feedback Loop')

# Define the partial order
root = StrictPartialOrder(nodes=[SiteSurvey, DesignLayout, SensorDeploy, CropSelect, SystemInstall, EnergySetup, WaterCycle, PestControl, RegulatoryCheck, StaffTraining, DataConfigure, SupplyPlan, HarvestSchedule, QualityAudit, MarketLaunch, FeedbackLoop])

# Define the dependencies
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, SensorDeploy)
root.order.add_edge(SensorDeploy, CropSelect)
root.order.add_edge(CropSelect, SystemInstall)
root.order.add_edge(SystemInstall, EnergySetup)
root.order.add_edge(EnergySetup, WaterCycle)
root.order.add_edge(WaterCycle, PestControl)
root.order.add_edge(PestControl, RegulatoryCheck)
root.order.add_edge(RegulatoryCheck, StaffTraining)
root.order.add_edge(StaffTraining, DataConfigure)
root.order.add_edge(DataConfigure, SupplyPlan)
root.order.add_edge(SupplyPlan, HarvestSchedule)
root.order.add_edge(HarvestSchedule, QualityAudit)
root.order.add_edge(QualityAudit, MarketLaunch)
root.order.add_edge(MarketLaunch, FeedbackLoop)