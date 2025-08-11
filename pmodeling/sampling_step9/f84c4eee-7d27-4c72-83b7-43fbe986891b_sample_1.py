import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loop nodes
frameAssemblyLoop = OperatorPOWL(operator=Operator.LOOP, children=[FrameAssembly, CircuitTesting])
sensorMountingLoop = OperatorPOWL(operator=Operator.LOOP, children=[SensorMounting, WiringHarness, CircuitTesting])
flightTestingLoop = OperatorPOWL(operator=Operator.LOOP, children=[FlightTesting, DataLogging, PerformanceTuning])
firmwareUpdateLoop = OperatorPOWL(operator=Operator.LOOP, children=[FirmwareUpdate, RemoteMonitoring])

# Define XOR nodes
initialCalibrationXOR = OperatorPOWL(operator=Operator.XOR, children=[InitialCalibration, skip])
softwareIntegrationXOR = OperatorPOWL(operator=Operator.XOR, children=[SoftwareIntegration, skip])

# Define root
root = StrictPartialOrder(nodes=[ComponentSourcing, frameAssemblyLoop, sensorMountingLoop, flightTestingLoop, firmwareUpdateLoop, initialCalibrationXOR, softwareIntegrationXOR, PackagingPrep, CustomLabeling, DocumentationPrint, QualityReview, ClientTraining, RemoteMonitoring, FirmwareUpdate])
root.order.add_edge(ComponentSourcing, frameAssemblyLoop)
root.order.add_edge(ComponentSourcing, sensorMountingLoop)
root.order.add_edge(frameAssemblyLoop, CircuitTesting)
root.order.add_edge(sensorMountingLoop, CircuitTesting)
root.order.add_edge(flightTestingLoop, DataLogging)
root.order.add_edge(flightTestingLoop, PerformanceTuning)
root.order.add_edge(firmwareUpdateLoop, RemoteMonitoring)
root.order.add_edge(initialCalibrationXOR, skip)
root.order.add_edge(softwareIntegrationXOR, skip)
root.order.add_edge(PackagingPrep, CustomLabeling)
root.order.add_edge(PackagingPrep, DocumentationPrint)
root.order.add_edge(QualityReview, ClientTraining)
root.order.add_edge(QualityReview, RemoteMonitoring)
root.order.add_edge(QualityReview, FirmwareUpdate)