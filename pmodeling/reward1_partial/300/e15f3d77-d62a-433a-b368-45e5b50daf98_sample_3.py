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

root = StrictPartialOrder(nodes=[
    GatherSpecs, AdaptDesign, SourceParts, ComponentTest, AssembleFrame, InstallFirmware,
    CalibrateSensors, StressTest, FlightSimulate, ValidateBattery, CheckAccuracy, PackageUnits,
    CreateManuals, ShipDrones, CollectFeedback
])