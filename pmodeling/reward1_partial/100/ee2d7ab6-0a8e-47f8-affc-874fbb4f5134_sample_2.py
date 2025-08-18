from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the process using POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[ClientConsult, SpecGathering])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[SupplierSourcing, DesignReview])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[SimulationTest, ProtoAssembly])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[QualityCheck, FirmwareFlash])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[SensorInstall, FinalTesting])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[BrandPackaging, ShippingPrep])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[DeliverySchedule, ClientTraining])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[DiagnosticsSetup, skip])

# Define the strict partial order structure
root = StrictPartialOrder(nodes=[xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8])

# Add edges to define the control flow
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)