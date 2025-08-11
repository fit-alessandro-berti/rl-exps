import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, DesignLayout, SensorDeploy, CropSelect, SystemInstall, EnergySetup, WaterCycle, PestControl, RegulatoryCheck, StaffTraining, DataConfigure, SupplyPlan, HarvestSchedule, QualityAudit, MarketLaunch, FeedbackLoop])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)