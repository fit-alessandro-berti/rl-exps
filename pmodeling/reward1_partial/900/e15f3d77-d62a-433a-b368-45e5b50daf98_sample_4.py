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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    GatherSpecs,
    AdaptDesign,
    SourceParts,
    ComponentTest,
    AssembleFrame,
    InstallFirmware,
    CalibrateSensors,
    StressTest,
    FlightSimulate,
    ValidateBattery,
    CheckAccuracy,
    PackageUnits,
    CreateManuals,
    ShipDrones,
    CollectFeedback
])

# Define the partial order dependencies
root.order.add_edge(GatherSpecs, AdaptDesign)
root.order.add_edge(AdaptDesign, SourceParts)
root.order.add_edge(SourceParts, ComponentTest)
root.order.add_edge(ComponentTest, AssembleFrame)
root.order.add_edge(AssembleFrame, InstallFirmware)
root.order.add_edge(InstallFirmware, CalibrateSensors)
root.order.add_edge(CalibrateSensors, StressTest)
root.order.add_edge(StressTest, FlightSimulate)
root.order.add_edge(FlightSimulate, ValidateBattery)
root.order.add_edge(ValidateBattery, CheckAccuracy)
root.order.add_edge(CheckAccuracy, PackageUnits)
root.order.add_edge(PackageUnits, CreateManuals)
root.order.add_edge(CreateManuals, ShipDrones)
root.order.add_edge(ShipDrones, CollectFeedback)

# Print the POWL model
print(root)