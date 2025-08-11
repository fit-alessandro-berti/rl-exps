import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SensorSetup = Transition(label='Sensor Setup')
DataCapture = Transition(label='Data Capture')
NutrientMix = Transition(label='Nutrient Mix')
CropRotate = Transition(label='Crop Rotate')
WasteCollect = Transition(label='Waste Collect')
CompostProcess = Transition(label='Compost Process')
DroneDispatch = Transition(label='Drone Dispatch')
PestControl = Transition(label='Pest Control')
PollinationRun = Transition(label='Pollination Run')
VolunteerAssign = Transition(label='Volunteer Assign')
FeedbackGather = Transition(label='Feedback Gather')
ModelUpdate = Transition(label='Model Update')
YieldForecast = Transition(label='Yield Forecast')
WaterAdjust = Transition(label='Water Adjust')
ReportGenerate = Transition(label='Report Generate')
ResourceAudit = Transition(label='Resource Audit')
ScheduleSync = Transition(label='Schedule Sync')

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[DataCapture, NutrientMix, CropRotate, WasteCollect, CompostProcess, DroneDispatch, PestControl, PollinationRun, VolunteerAssign, FeedbackGather, ModelUpdate, YieldForecast, WaterAdjust, ReportGenerate, ResourceAudit, ScheduleSync])

xor = OperatorPOWL(operator=Operator.XOR, children=[loop, skip])

root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, loop)