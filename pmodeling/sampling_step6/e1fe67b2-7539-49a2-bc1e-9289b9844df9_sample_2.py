import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

root = StrictPartialOrder(nodes=[GatherSpecs, DesignCustom, SourceParts, FirmwareLoad, MechanicalFit, CableRouting, SensorAlign, ComponentTest, SoftwareSync, FlightCalibrate, EnviroTest, RemotePair, QualityCheck, PackageUnit, RegisterDrone, ClientTrain])