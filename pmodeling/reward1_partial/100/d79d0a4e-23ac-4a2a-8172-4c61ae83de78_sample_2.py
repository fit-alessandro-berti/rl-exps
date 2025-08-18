import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the POWL model structure
# Start with Spec Review and Component Pick as the initial nodes
root = StrictPartialOrder(nodes=[SpecReview, ComponentPick])

# Add transitions and dependencies as per the described process
root.order.add_edge(SpecReview, ComponentPick)
root.order.add_edge(ComponentPick, FrameBuild)
root.order.add_edge(FrameBuild, MotorMount)
root.order.add_edge(MotorMount, SensorFit)
root.order.add_edge(SensorFit, WiringSetup)
root.order.add_edge(WiringSetup, SoftwareLoad)
root.order.add_edge(SoftwareLoad, CalibrationTest)
root.order.add_edge(CalibrationTest, StressCheck)
root.order.add_edge(StressCheck, FirmwareFlash)
root.order.add_edge(FirmwareFlash, FeedbackLoop)
root.order.add_edge(FeedbackLoop, PackagePrep)
root.order.add_edge(PackagePrep, DocCompile)
root.order.add_edge(DocCompile, ShipArrange)
root.order.add_edge(ShipArrange, RemoteSetup)

# The RemoteSetup node is not dependent on any other node, so it can be placed at the end
root.order.add_edge(RemoteSetup, None)

print(root)