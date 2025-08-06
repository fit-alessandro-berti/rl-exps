import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
GatherSpecs = Transition(label='Gather Specs')
DesignCustom = Transition(label='Design Custom')
SourceParts = Transition(label='Source Parts')
FirmwareLoad = Transition(label='Firmware Load')
MechanicalFit = Transition(label='Mechanical Fit')
CableRouting = Transition(label='Cable Routing')
SensorAlign = Transition(label='Sensor Align')
ComponentTest = Transition(label='Component Test')
SoftwareSync = Transition(label='Software Sync')
FlightCalibrate = Transition(label='Flight Calibrate')
EnviroTest = Transition(label='Enviro Test')
RemotePair = Transition(label='Remote Pair')
QualityCheck = Transition(label='Quality Check')
PackageUnit = Transition(label='Package Unit')
RegisterDrone = Transition(label='Register Drone')
ClientTrain = Transition(label='Client Train')

# Define the loop for quality assurance
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[QualityCheck, PackageUnit])

# Define the exclusive choice for flight calibration and environmental testing
flight_enviro_choice = OperatorPOWL(operator=Operator.XOR, children=[FlightCalibrate, EnviroTest])

# Define the exclusive choice for software integration and remote pairing
software_remote_choice = OperatorPOWL(operator=Operator.XOR, children=[SoftwareSync, RemotePair])

# Define the sequence for drone assembly
assembly_sequence = StrictPartialOrder(nodes=[SourceParts, FirmwareLoad, MechanicalFit, CableRouting, SensorAlign, ComponentTest, flight_enviro_choice, software_remote_choice, quality_loop])

# Define the sequence for post-assembly operations
post_assembly_sequence = StrictPartialOrder(nodes=[RegisterDrone, ClientTrain])

# Define the overall process
root = StrictPartialOrder(nodes=[GatherSpecs, DesignCustom, assembly_sequence, post_assembly_sequence])

# Add dependencies
root.order.add_edge(GatherSpecs, DesignCustom)
root.order.add_edge(DesignCustom, SourceParts)
root.order.add_edge(SourceParts, FirmwareLoad)
root.order.add_edge(FirmwareLoad, MechanicalFit)
root.order.add_edge(MechanicalFit, CableRouting)
root.order.add_edge(CableRouting, SensorAlign)
root.order.add_edge(SensorAlign, ComponentTest)
root.order.add_edge(ComponentTest, flight_enviro_choice)
root.order.add_edge(flight_enviro_choice, software_remote_choice)
root.order.add_edge(software_remote_choice, quality_loop)
root.order.add_edge(quality_loop, PackageUnit)
root.order.add_edge(GatherSpecs, post_assembly_sequence)
root.order.add_edge(DesignCustom, post_assembly_sequence)
root.order.add_edge(SourceParts, post_assembly_sequence)
root.order.add_edge(FirmwareLoad, post_assembly_sequence)
root.order.add_edge(MechanicalFit, post_assembly_sequence)
root.order.add_edge(CableRouting, post_assembly_sequence)
root.order.add_edge(SensorAlign, post_assembly_sequence)
root.order.add_edge(ComponentTest, post_assembly_sequence)
root.order.add_edge(flight_enviro_choice, post_assembly_sequence)
root.order.add_edge(software_remote_choice, post_assembly_sequence)
root.order.add_edge(quality_loop, post_assembly_sequence)
root.order.add_edge(RegisterDrone, post_assembly_sequence)
root.order.add_edge(ClientTrain, post_assembly_sequence)

print(root)