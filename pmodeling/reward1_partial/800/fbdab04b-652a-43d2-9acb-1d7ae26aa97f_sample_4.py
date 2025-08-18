import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
ClientConsult = Transition(label='Client Consult')
SpecAnalysis = Transition(label='Spec Analysis')
ModuleSelect = Transition(label='Module Select')
ComponentOrder = Transition(label='Component Order')
PartsInspect = Transition(label='Parts Inspect')
FrameAssemble = Transition(label='Frame Assemble')
SensorInstall = Transition(label='Sensor Install')
MotorAttach = Transition(label='Motor Attach')
WiringConnect = Transition(label='Wiring Connect')
SoftwareUpload = Transition(label='Software Upload')
CalibrationTest = Transition(label='Calibration Test')
FlightSimulate = Transition(label='Flight Simulate')
QualityReview = Transition(label='Quality Review')
UserTrain = Transition(label='User Train')
RemoteSetup = Transition(label='Remote Setup')
FeedbackCollect = Transition(label='Feedback Collect')
SupportSchedule = Transition(label='Support Schedule')

skip = SilentTransition()

# Define the process flow
client_flow = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[ClientConsult, SpecAnalysis, ModuleSelect, ComponentOrder, PartsInspect, FrameAssemble, SensorInstall, MotorAttach, WiringConnect, SoftwareUpload, CalibrationTest, FlightSimulate, QualityReview, UserTrain, RemoteSetup, FeedbackCollect, SupportSchedule])

# Define the root of the process
root = StrictPartialOrder(nodes=[client_flow])
root.order.add_edge(client_flow, client_flow)

# Print the root
print(root)