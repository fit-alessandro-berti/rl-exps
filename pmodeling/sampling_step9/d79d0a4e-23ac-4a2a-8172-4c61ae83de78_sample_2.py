import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
SpecReview = Transition(label='Spec Review')
ComponentPick = Transition(label='Component Pick')
FrameBuild = Transition(label='Frame Build')
MotorMount = Transition(label='Motor Mount')
SensorFit = Transition(label='Sensor Fit')
WiringSetup = Transition(label='Wiring Setup')
SoftwareLoad = Transition(label='Software Load')
CalibrationTest = Transition(label='Calibration Test')
StressCheck = Transition(label='Stress Check')
FirmwareFlash = Transition(label='Firmware Flash')
FeedbackLoop = Transition(label='Feedback Loop')
PackagePrep = Transition(label='Package Prep')
DocCompile = Transition(label='Doc Compile')
ShipArrange = Transition(label='Ship Arrange')
RemoteSetup = Transition(label='Remote Setup')

# Define the silent transition
skip = SilentTransition()

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[CalibrationTest, StressCheck])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[FeedbackLoop])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[FirmwareFlash])

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[RemoteSetup, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[SpecReview, ComponentPick, FrameBuild, MotorMount, SensorFit, WiringSetup, SoftwareLoad, loop1, loop2, loop3, xor, PackagePrep, DocCompile, ShipArrange])
root.order.add_edge(SpecReview, ComponentPick)
root.order.add_edge(ComponentPick, FrameBuild)
root.order.add_edge(FrameBuild, MotorMount)
root.order.add_edge(MotorMount, SensorFit)
root.order.add_edge(SensorFit, WiringSetup)
root.order.add_edge(WiringSetup, SoftwareLoad)
root.order.add_edge(SoftwareLoad, loop1)
root.order.add_edge(loop1, CalibrationTest)
root.order.add_edge(loop1, StressCheck)
root.order.add_edge(StressCheck, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, FeedbackLoop)
root.order.add_edge(FeedbackLoop, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, FirmwareFlash)
root.order.add_edge(loop3, loop2)
root.order.add_edge(loop2, xor)
root.order.add_edge(xor, PackagePrep)
root.order.add_edge(PackagePrep, DocCompile)
root.order.add_edge(DocCompile, ShipArrange)

print(root)