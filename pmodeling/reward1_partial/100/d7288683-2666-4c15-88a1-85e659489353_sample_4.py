import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Define the workflow structure
# Step 1: Component sourcing, frame assembly, motor installation, sensor mounting, wiring setup, firmware upload, AI module
step1 = OperatorPOWL(operator=Operator.XOR, children=[ComponentSourcing, FrameAssembly, MotorInstallation, SensorMounting, WiringSetup, FirmwareUpload, AI_Module])

# Step 2: Calibration phase, stress testing
step2 = OperatorPOWL(operator=Operator.LOOP, children=[CalibrationPhase, StressTesting])

# Step 3: Flight simulation, pattern adjustment
step3 = OperatorPOWL(operator=Operator.XOR, children=[FlightSimulation, PatternAdjustment])

# Step 4: Quality inspection, compliance check
step4 = OperatorPOWL(operator=Operator.XOR, children=[QualityInspect, ComplianceCheck])

# Step 5: Packaging final
step5 = PackagingFinal

# Step 6: Delivery setup
step6 = DeliverySetup

# Root node with all steps
root = StrictPartialOrder(nodes=[step1, step2, step3, step4, step5, step6])

# Establish dependencies between steps
root.order.add_edge(step1, step2)
root.order.add_edge(step1, step3)
root.order.add_edge(step2, step4)
root.order.add_edge(step3, step4)
root.order.add_edge(step4, step5)
root.order.add_edge(step5, step6)

# Print the root node for verification
print(root)