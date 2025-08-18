import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SiteSurvey = Transition(label='Site Survey')
LightMapping = Transition(label='Light Mapping')
WaterTesting = Transition(label='Water Testing')
DesignModules = Transition(label='Design Modules')
IoTSetup = Transition(label='IoT Setup')
SensorCalibration = Transition(label='Sensor Calibration')
NutrientMix = Transition(label='Nutrient Mix')
ClimateControl = Transition(label='Climate Control')
RegulatoryCheck = Transition(label='Regulatory Check')
CommunityMeet = Transition(label='Community Meet')
EnergyAudit = Transition(label='Energy Audit')
StaffTraining = Transition(label='Staff Training')
Installation = Transition(label='Installation')
SystemTesting = Transition(label='System Testing')
YieldAnalysis = Transition(label='Yield Analysis')
ResourceAudit = Transition(label='Resource Audit')
ImpactReview = Transition(label='Impact Review')

# Define exclusive choice for regulatory check and energy audit
xor = OperatorPOWL(operator=Operator.XOR, children=[RegulatoryCheck, EnergyAudit])

# Define loop for staff training and system testing
loop = OperatorPOWL(operator=Operator.LOOP, children=[StaffTraining, SystemTesting])

# Define strict partial order with dependencies
root = StrictPartialOrder(nodes=[SiteSurvey, LightMapping, WaterTesting, DesignModules, IoTSetup, SensorCalibration, NutrientMix, ClimateControl, xor, CommunityMeet, EnergyAudit, StaffTraining, Installation, SystemTesting, YieldAnalysis, ResourceAudit, ImpactReview])
root.order.add_edge(SiteSurvey, LightMapping)
root.order.add_edge(LightMapping, WaterTesting)
root.order.add_edge(WaterTesting, DesignModules)
root.order.add_edge(DesignModules, IoTSetup)
root.order.add_edge(IoTSetup, SensorCalibration)
root.order.add_edge(SensorCalibration, NutrientMix)
root.order.add_edge(NutrientMix, ClimateControl)
root.order.add_edge(ClimateControl, xor)
root.order.add_edge(xor, CommunityMeet)
root.order.add_edge(CommunityMeet, EnergyAudit)
root.order.add_edge(EnergyAudit, StaffTraining)
root.order.add_edge(StaffTraining, SystemTesting)
root.order.add_edge(SystemTesting, Installation)
root.order.add_edge(Installation, SystemTesting)
root.order.add_edge(SystemTesting, YieldAnalysis)
root.order.add_edge(YieldAnalysis, ResourceAudit)
root.order.add_edge(ResourceAudit, ImpactReview)