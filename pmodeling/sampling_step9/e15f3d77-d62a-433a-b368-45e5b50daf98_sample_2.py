import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

GatherSpecs = Transition(label='Gather Specs')
AdaptDesign = Transition(label='Adapt Design')
SourceParts = Transition(label='Source Parts')
ComponentTest = Transition(label='Component Test')
AssembleFrame = Transition(label='Assemble Frame')
InstallFirmware = Transition(label='Install Firmware')
CalibrateSensors = Transition(label='Calibrate Sensors')
StressTest = Transition(label='Stress Test')
FlightSimulate = Transition(label='Flight Simulate')
ValidateBattery = Transition(label='Validate Battery')
CheckAccuracy = Transition(label='Check Accuracy')
PackageUnits = Transition(label='Package Units')
CreateManuals = Transition(label='Create Manuals')
ShipDrones = Transition(label='Ship Drones')
CollectFeedback = Transition(label='Collect Feedback')

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[SourceParts, ComponentTest, AssembleFrame, InstallFirmware, CalibrateSensors])
xor = OperatorPOWL(operator=Operator.XOR, children=[StressTest, FlightSimulate, ValidateBattery, CheckAccuracy])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[PackageUnits, CreateManuals])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ShipDrones, CollectFeedback])

root = StrictPartialOrder(nodes=[loop, xor, xor2, loop2])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, loop2)
root.order.add_edge(loop2, xor2)