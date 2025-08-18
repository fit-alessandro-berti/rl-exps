import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the control flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[client_consult, spec_gathering, supplier_sourcing, design_review, simulation_test, proto_assembly, quality_check, firmware_flash, sensor_install, final_testing, brand_packaging, shipping_prep, delivery_schedule, client_training, diagnostics_setup])

# Define the partial order
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(client_consult, xor)
root.order.add_edge(spec_gathering, xor)
root.order.add_edge(supplier_sourcing, xor)
root.order.add_edge(design_review, xor)
root.order.add_edge(simulation_test, xor)
root.order.add_edge(proto_assembly, xor)
root.order.add_edge(quality_check, xor)
root.order.add_edge(firmware_flash, xor)
root.order.add_edge(sensor_install, xor)
root.order.add_edge(final_testing, xor)
root.order.add_edge(brand_packaging, xor)
root.order.add_edge(shipping_prep, xor)
root.order.add_edge(delivery_schedule, xor)
root.order.add_edge(client_training, xor)
root.order.add_edge(diagnostics_setup, xor)

# Print the root
print(root)