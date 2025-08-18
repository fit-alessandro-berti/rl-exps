import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) as objects
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

# Define the loop for the calibration phase
loop_CalibrationPhase = OperatorPOWL(operator=Operator.LOOP, children=[CalibrationPhase, StressTesting, FlightSimulation, PatternAdjustment, QualityInspect, ComplianceCheck, PackagingFinal])

# Define the exclusive choice for the final quality inspection and compliance check
xor_FinalCheck = OperatorPOWL(operator=Operator.XOR, children=[DeliverySetup, SilentTransition()])

# Create the root POWL model
root = StrictPartialOrder(nodes=[ComponentSourcing, FrameAssembly, MotorInstallation, SensorMounting, WiringSetup, FirmwareUpload, AI_Module, loop_CalibrationPhase, xor_FinalCheck])
root.order.add_edge(ComponentSourcing, FrameAssembly)
root.order.add_edge(FrameAssembly, MotorInstallation)
root.order.add_edge(MotorInstallation, SensorMounting)
root.order.add_edge(SensorMounting, WiringSetup)
root.order.add_edge(WiringSetup, FirmwareUpload)
root.order.add_edge(FirmwareUpload, AI_Module)
root.order.add_edge(AI_Module, loop_CalibrationPhase)
root.order.add_edge(loop_CalibrationPhase, xor_FinalCheck)

# Print the root POWL model
print(root)