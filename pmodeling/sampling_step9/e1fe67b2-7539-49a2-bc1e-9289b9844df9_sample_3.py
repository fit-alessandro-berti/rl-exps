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

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[DesignCustom, SourceParts, FirmwareLoad, MechanicalFit, CableRouting, SensorAlign, ComponentTest])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[FlightCalibrate, EnviroTest])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[RemotePair, QualityCheck])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[PackageUnit, RegisterDrone])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ClientTrain, skip])

root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)