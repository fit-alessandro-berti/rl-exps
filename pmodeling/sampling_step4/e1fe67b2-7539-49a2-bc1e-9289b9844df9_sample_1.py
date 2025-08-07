import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Gather_Specs = Transition(label='Gather Specs')
Design_Custom = Transition(label='Design Custom')
Source_Parts = Transition(label='Source Parts')
Firmware_Load = Transition(label='Firmware Load')
Mechanical_Fit = Transition(label='Mechanical Fit')
Cable_Routing = Transition(label='Cable Routing')
Sensor_Align = Transition(label='Sensor Align')
Component_Test = Transition(label='Component Test')
Software_Sync = Transition(label='Software Sync')
Flight_Calibrate = Transition(label='Flight Calibrate')
Enviro_Test = Transition(label='Enviro Test')
Remote_Pair = Transition(label='Remote Pair')
Quality_Check = Transition(label='Quality Check')
Package_Unit = Transition(label='Package Unit')
Register_Drone = Transition(label='Register Drone')
Client_Train = Transition(label='Client Train')

root = StrictPartialOrder(nodes=[
    Gather_Specs,
    Design_Custom,
    Source_Parts,
    Firmware_Load,
    Mechanical_Fit,
    Cable_Routing,
    Sensor_Align,
    Component_Test,
    Software_Sync,
    Flight_Calibrate,
    Enviro_Test,
    Remote_Pair,
    Quality_Check,
    Package_Unit,
    Register_Drone,
    Client_Train
])

root.order.add_edge(Gather_Specs, Design_Custom)
root.order.add_edge(Design_Custom, Source_Parts)
root.order.add_edge(Source_Parts, Firmware_Load)
root.order.add_edge(Firmware_Load, Mechanical_Fit)
root.order.add_edge(Mechanical_Fit, Cable_Routing)
root.order.add_edge(Cable_Routing, Sensor_Align)
root.order.add_edge(Sensor_Align, Component_Test)
root.order.add_edge(Component_Test, Software_Sync)
root.order.add_edge(Software_Sync, Flight_Calibrate)
root.order.add_edge(Flight_Calibrate, Enviro_Test)
root.order.add_edge(Enviro_Test, Remote_Pair)
root.order.add_edge(Remote_Pair, Quality_Check)
root.order.add_edge(Quality_Check, Package_Unit)
root.order.add_edge(Package_Unit, Register_Drone)
root.order.add_edge(Register_Drone, Client_Train)

print(root)