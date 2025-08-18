import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
ComponentSourcing = Transition(label='Component Sourcing')
FrameAssembly = Transition(label='Frame Assembly')
MotorInstallation = Transition(label='Motor Installation')
SensorMounting = Transition(label='Sensor Mounting')
WiringSetup = Transition(label='Wiring Setup')
FirmwareUpload = Transition(label='Firmware Upload')
AI_Module = Transition(label='AI Module')
CalibrationPhase = Transition(label='Calibration Phase')
StressTesting = Transition(label='Stress Testing')
FlightSimulation = Transition(label='Flight Simulation')
PatternAdjustment = Transition(label='Pattern Adjustment')
QualityInspect = Transition(label='Quality Inspect')
ComplianceCheck = Transition(label='Compliance Check')
PackagingFinal = Transition(label='Packaging Final')
DeliverySetup = Transition(label='Delivery Setup')

# Define the partial order
root = StrictPartialOrder(nodes=[ComponentSourcing, FrameAssembly, MotorInstallation, SensorMounting, WiringSetup, FirmwareUpload, AI_Module, CalibrationPhase, StressTesting, FlightSimulation, PatternAdjustment, QualityInspect, ComplianceCheck, PackagingFinal, DeliverySetup])

# Define the order between nodes
root.order.add_edge(ComponentSourcing, FrameAssembly)
root.order.add_edge(FrameAssembly, MotorInstallation)
root.order.add_edge(MotorInstallation, SensorMounting)
root.order.add_edge(SensorMounting, WiringSetup)
root.order.add_edge(WiringSetup, FirmwareUpload)
root.order.add_edge(FirmwareUpload, AI_Module)
root.order.add_edge(AI_Module, CalibrationPhase)
root.order.add_edge(CalibrationPhase, StressTesting)
root.order.add_edge(StressTesting, FlightSimulation)
root.order.add_edge(FlightSimulation, PatternAdjustment)
root.order.add_edge(PatternAdjustment, QualityInspect)
root.order.add_edge(QualityInspect, ComplianceCheck)
root.order.add_edge(ComplianceCheck, PackagingFinal)
root.order.add_edge(PackagingFinal, DeliverySetup)

print(root)