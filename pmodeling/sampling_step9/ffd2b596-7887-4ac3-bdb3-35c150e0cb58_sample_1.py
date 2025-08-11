import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SensorCalibrate, MotorAssembly])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[FrameBuild, SoftwareInstall])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[AlgorithmTune, BatteryIntegrate])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[SignalTest, DurabilityCheck])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[FlightSimulate, QualityInspect])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[ComplianceReview, PackagingPrep])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[LogisticsPlan, ClientFeedback])

# Define the XOR nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop6, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[loop7, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, loop3)
root.order.add_edge(xor4, loop4)
root.order.add_edge(xor5, loop5)
root.order.add_edge(xor6, loop6)
root.order.add_edge(xor7, loop7)