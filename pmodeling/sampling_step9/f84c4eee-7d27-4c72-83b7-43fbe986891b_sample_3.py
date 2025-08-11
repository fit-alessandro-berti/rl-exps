import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
ComponentSourcing = Transition(label='Component Sourcing')
FrameAssembly = Transition(label='Frame Assembly')
SensorMounting = Transition(label='Sensor Mounting')
WiringHarness = Transition(label='Wiring Harness')
CircuitTesting = Transition(label='Circuit Testing')
FirmwareLoading = Transition(label='Firmware Loading')
InitialCalibration = Transition(label='Initial Calibration')
SoftwareIntegration = Transition(label='Software Integration')
FlightTesting = Transition(label='Flight Testing')
DataLogging = Transition(label='Data Logging')
PerformanceTuning = Transition(label='Performance Tuning')
PackagingPrep = Transition(label='Packaging Prep')
CustomLabeling = Transition(label='Custom Labeling')
DocumentationPrint = Transition(label='Documentation Print')
QualityReview = Transition(label='Quality Review')
ClientTraining = Transition(label='Client Training')
RemoteMonitoring = Transition(label='Remote Monitoring')
FirmwareUpdate = Transition(label='Firmware Update')

# Define silent transitions
skip = SilentTransition()

# Define loop for drone assembly and calibration
loop = OperatorPOWL(operator=Operator.LOOP, children=[FrameAssembly, CircuitTesting, FirmwareLoading, InitialCalibration])

# Define exclusive choice for software integration and flight testing
xor = OperatorPOWL(operator=Operator.XOR, children=[SoftwareIntegration, FlightTesting])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Add additional edges for other activities
root.order.add_edge(ComponentSourcing, loop)
root.order.add_edge(SensorMounting, loop)
root.order.add_edge(WiringHarness, loop)
root.order.add_edge(InitialCalibration, loop)
root.order.add_edge(FirmwareLoading, loop)
root.order.add_edge(SoftwareIntegration, xor)
root.order.add_edge(FlightTesting, xor)
root.order.add_edge(DataLogging, xor)
root.order.add_edge(PerformanceTuning, xor)
root.order.add_edge(PackagingPrep, xor)
root.order.add_edge(CustomLabeling, xor)
root.order.add_edge(DocumentationPrint, xor)
root.order.add_edge(QualityReview, xor)
root.order.add_edge(ClientTraining, xor)
root.order.add_edge(RemoteMonitoring, xor)
root.order.add_edge(FirmwareUpdate, xor)