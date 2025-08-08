import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
client_consult = Transition(label='Client Consult')
spec_gathering = Transition(label='Spec Gathering')
supplier_sourcing = Transition(label='Supplier Sourcing')
design_review = Transition(label='Design Review')
simulation_test = Transition(label='Simulation Test')
proto_assembly = Transition(label='Proto Assembly')
quality_check = Transition(label='Quality Check')
firmware_flash = Transition(label='Firmware Flash')
sensor_install = Transition(label='Sensor Install')
final_testing = Transition(label='Final Testing')
brand_packaging = Transition(label='Brand Packaging')
shipping_prep = Transition(label='Shipping Prep')
delivery_schedule = Transition(label='Delivery Schedule')
client_training = Transition(label='Client Training')
diagnostics_setup = Transition(label='Diagnostics Setup')

# Define the operators and partial order
xor = OperatorPOWL(operator=Operator.XOR, children=[spec_gathering, supplier_sourcing])
loop = OperatorPOWL(operator=Operator.LOOP, children=[design_review, simulation_test, proto_assembly, quality_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[firmware_flash, sensor_install, final_testing])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[brand_packaging, shipping_prep, delivery_schedule])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[client_training, diagnostics_setup])

root = StrictPartialOrder(nodes=[xor, loop, xor2, xor3, xor4])
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)

# Print the root node
print(root)