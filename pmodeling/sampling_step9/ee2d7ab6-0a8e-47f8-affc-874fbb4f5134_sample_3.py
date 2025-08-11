import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

ClientConsult = Transition(label='Client Consult')
SpecGathering = Transition(label='Spec Gathering')
SupplierSourcing = Transition(label='Supplier Sourcing')
DesignReview = Transition(label='Design Review')
SimulationTest = Transition(label='Simulation Test')
ProtoAssembly = Transition(label='Proto Assembly')
QualityCheck = Transition(label='Quality Check')
FirmwareFlash = Transition(label='Firmware Flash')
SensorInstall = Transition(label='Sensor Install')
FinalTesting = Transition(label='Final Testing')
BrandPackaging = Transition(label='Brand Packaging')
ShippingPrep = Transition(label='Shipping Prep')
DeliverySchedule = Transition(label='Delivery Schedule')
ClientTraining = Transition(label='Client Training')
DiagnosticsSetup = Transition(label='Diagnostics Setup')

skip = SilentTransition()

# Loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[DesignReview, SimulationTest])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ProtoAssembly, QualityCheck])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[FirmwareFlash, SensorInstall])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[FinalTesting, BrandPackaging])

# Exclusive choices
xor1 = OperatorPOWL(operator=Operator.XOR, children=[skip, ShippingPrep])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, DeliverySchedule])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[skip, ClientTraining])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[skip, DiagnosticsSetup])

# Partial Order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, xor1, xor2, xor3, xor4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)

# Connect loops and exclusive choices
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, loop3)
root.order.add_edge(xor4, loop4)