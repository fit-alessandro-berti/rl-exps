from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) in the process
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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    ComponentSourcing,
    FrameAssembly,
    SensorMounting,
    WiringHarness,
    CircuitTesting,
    FirmwareLoading,
    InitialCalibration,
    SoftwareIntegration,
    FlightTesting,
    DataLogging,
    PerformanceTuning,
    PackagingPrep,
    CustomLabeling,
    DocumentationPrint,
    QualityReview,
    ClientTraining,
    RemoteMonitoring,
    FirmwareUpdate
])

# Define the dependencies (partial order)
root.order.add_edge(ComponentSourcing, FrameAssembly)
root.order.add_edge(FrameAssembly, SensorMounting)
root.order.add_edge(SensorMounting, WiringHarness)
root.order.add_edge(WiringHarness, CircuitTesting)
root.order.add_edge(CircuitTesting, FirmwareLoading)
root.order.add_edge(FirmwareLoading, InitialCalibration)
root.order.add_edge(InitialCalibration, SoftwareIntegration)
root.order.add_edge(SoftwareIntegration, FlightTesting)
root.order.add_edge(FlightTesting, DataLogging)
root.order.add_edge(DataLogging, PerformanceTuning)
root.order.add_edge(PerformanceTuning, PackagingPrep)
root.order.add_edge(PackagingPrep, CustomLabeling)
root.order.add_edge(CustomLabeling, DocumentationPrint)
root.order.add_edge(DocumentationPrint, QualityReview)
root.order.add_edge(QualityReview, ClientTraining)
root.order.add_edge(ClientTraining, RemoteMonitoring)
root.order.add_edge(RemoteMonitoring, FirmwareUpdate)

print(root)