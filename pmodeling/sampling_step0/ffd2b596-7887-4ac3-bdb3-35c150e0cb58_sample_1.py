import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
ComponentSourcing = Transition(label='Component Sourcing')
SensorCalibrate = Transition(label='Sensor Calibrate')
MotorAssembly = Transition(label='Motor Assembly')
FrameBuild = Transition(label='Frame Build')
SoftwareInstall = Transition(label='Software Install')
AlgorithmTune = Transition(label='Algorithm Tune')
BatteryIntegrate = Transition(label='Battery Integrate')
SignalTest = Transition(label='Signal Test')
DurabilityCheck = Transition(label='Durability Check')
FlightSimulate = Transition(label='Flight Simulate')
QualityInspect = Transition(label='Quality Inspect')
ComplianceReview = Transition(label='Compliance Review')
PackagingPrep = Transition(label='Packaging Prep')
LogisticsPlan = Transition(label='Logistics Plan')
ClientFeedback = Transition(label='Client Feedback')

# Define silent transitions
skip = SilentTransition()

# Define the process flow
# Step 1: Component Sourcing
# Step 2: Sensor Calibrate
# Step 3: Motor Assembly
# Step 4: Frame Build
# Step 5: Software Install
# Step 6: Algorithm Tune
# Step 7: Battery Integrate
# Step 8: Signal Test
# Step 9: Durability Check
# Step 10: Flight Simulate
# Step 11: Quality Inspect
# Step 12: Compliance Review
# Step 13: Packaging Prep
# Step 14: Logistics Plan
# Step 15: Client Feedback

# Create the POWL model
root = StrictPartialOrder()

# Exclusive choices
root.add_transition(SensorCalibrate)
root.add_transition(MotorAssembly)
root.add_transition(FrameBuild)
root.add_transition(SoftwareInstall)
root.add_transition(AlgorithmTune)
root.add_transition(BatteryIntegrate)
root.add_transition(SignalTest)
root.add_transition(DurabilityCheck)
root.add_transition(FlightSimulate)
root.add_transition(QualityInspect)
root.add_transition(ComplianceReview)
root.add_transition(PackagingPrep)
root.add_transition(LogisticsPlan)
root.add_transition(ClientFeedback)

# Loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[DurabilityCheck, SignalTest])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[QualityInspect, ComplianceReview])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[PackagingPrep, LogisticsPlan])

# Exclusive choice for step 9
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])

# Exclusive choice for step 10
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])

# Exclusive choice for step 11
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])

# Add transitions to the POWL model
root.add_transition(FlightSimulate)
root.add_transition(xor1)
root.add_transition(xor2)
root.add_transition(xor3)
root.add_transition(ClientFeedback)

# Add edges to the POWL model
root.add_edge(FlightSimulate, xor1)
root.add_edge(FlightSimulate, xor2)
root.add_edge(FlightSimulate, xor3)
root.add_edge(xor1, xor2)
root.add_edge(xor1, xor3)
root.add_edge(xor2, xor3)
root.add_edge(xor3, ClientFeedback)

# Print the POWL model
print(root)