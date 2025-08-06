import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transition
skip = SilentTransition()

# Define the loop nodes
loop_design_review = OperatorPOWL(operator=Operator.LOOP, children=[design_review, simulation_test])
loop_firmware_flash = OperatorPOWL(operator=Operator.LOOP, children=[firmware_flash, sensor_install])
loop_final_testing = OperatorPOWL(operator=Operator.LOOP, children=[final_testing, brand_packaging])

# Define the exclusive choice nodes
xor_suppliers = OperatorPOWL(operator=Operator.XOR, children=[supplier_sourcing, skip])
xor_quality = OperatorPOWL(operator=Operator.XOR, children=[quality_check, skip])
xor_firmware = OperatorPOWL(operator=Operator.XOR, children=[firmware_flash, skip])
xor_sensor = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, skip])
xor_branding = OperatorPOWL(operator=Operator.XOR, children=[brand_packaging, skip])
xor_training = OperatorPOWL(operator=Operator.XOR, children=[client_training, skip])
xor_diagnostics = OperatorPOWL(operator=Operator.XOR, children=[diagnostics_setup, skip])

# Define the root node
root = StrictPartialOrder(nodes=[client_consult, spec_gathering, loop_design_review, xor_suppliers, loop_firmware_flash, xor_quality, loop_final_testing, xor_firmware, xor_sensor, xor_branding, xor_training, xor_diagnostics, shipping_prep, delivery_schedule])
root.order.add_edge(client_consult, spec_gathering)
root.order.add_edge(spec_gathering, loop_design_review)
root.order.add_edge(loop_design_review, xor_suppliers)
root.order.add_edge(xor_suppliers, loop_firmware_flash)
root.order.add_edge(loop_firmware_flash, xor_quality)
root.order.add_edge(xor_quality, loop_final_testing)
root.order.add_edge(loop_final_testing, xor_firmware)
root.order.add_edge(xor_firmware, xor_sensor)
root.order.add_edge(xor_sensor, xor_branding)
root.order.add_edge(xor_branding, xor_training)
root.order.add_edge(xor_training, xor_diagnostics)
root.order.add_edge(xor_diagnostics, shipping_prep)
root.order.add_edge(shipping_prep, delivery_schedule)

print(root)