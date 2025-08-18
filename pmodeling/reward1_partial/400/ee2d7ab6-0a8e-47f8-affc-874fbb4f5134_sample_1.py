import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

xor = OperatorPOWL(operator=Operator.XOR, children=[client_consult, spec_gathering, supplier_sourcing])
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[design_review, simulation_test, proto_assembly])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, firmware_flash, sensor_install])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[final_testing, brand_packaging, shipping_prep])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[delivery_schedule, client_training, diagnostics_setup])

root = StrictPartialOrder(nodes=[xor, xor_1, xor_2, xor_3, xor_4])
root.order.add_edge(xor, xor_1)
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, xor_4)