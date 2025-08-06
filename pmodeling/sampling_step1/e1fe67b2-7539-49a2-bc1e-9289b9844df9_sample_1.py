import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the process flow
root = StrictPartialOrder(nodes=[
    GatherSpecs,
    DesignCustom,
    SourceParts,
    FirmwareLoad,
    MechanicalFit,
    CableRouting,
    SensorAlign,
    ComponentTest,
    SoftwareSync,
    FlightCalibrate,
    EnviroTest,
    RemotePair,
    QualityCheck,
    PackageUnit,
    RegisterDrone,
    ClientTrain
])

# Add the dependencies between the activities
root.order.add_edge(GatherSpecs, DesignCustom)
root.order.add_edge(DesignCustom, SourceParts)
root.order.add_edge(SourceParts, FirmwareLoad)
root.order.add_edge(FirmwareLoad, MechanicalFit)
root.order.add_edge(MechanicalFit, CableRouting)
root.order.add_edge(CableRouting, SensorAlign)
root.order.add_edge(SensorAlign, ComponentTest)
root.order.add_edge(ComponentTest, SoftwareSync)
root.order.add_edge(SoftwareSync, FlightCalibrate)
root.order.add_edge(FlightCalibrate, EnviroTest)
root.order.add_edge(EnviroTest, RemotePair)
root.order.add_edge(RemotePair, QualityCheck)
root.order.add_edge(QualityCheck, PackageUnit)
root.order.add_edge(PackageUnit, RegisterDrone)
root.order.add_edge(RegisterDrone, ClientTrain)