import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the root node as a strict partial order
root = StrictPartialOrder(nodes=[
    client_consult,
    spec_gathering,
    supplier_sourcing,
    design_review,
    simulation_test,
    proto_assembly,
    quality_check,
    firmware_flash,
    sensor_install,
    final_testing,
    brand_packaging,
    shipping_prep,
    delivery_schedule,
    client_training,
    diagnostics_setup
])

# Add dependencies as needed
# For example, if 'spec_gathering' depends on 'client_consult', add an edge
# root.order.add_edge(client_consult, spec_gathering)

# If you have more complex dependencies, you can add them similarly
# root.order.add_edge(supplier_sourcing, design_review)

# If you have loops, you can define them similarly
# For example, if 'proto_assembly' is part of a loop, you can define it as:
# loop = OperatorPOWL(operator=Operator.LOOP, children=[proto_assembly])
# root.order.add_edge(proto_assembly, loop)

# If you have XOR (exclusive choice) nodes, you can define them similarly
# For example, if 'client_training' and 'diagnostics_setup' are part of an XOR node, you can define it as:
# xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, diagnostics_setup])
# root.order.add_edge(xor, client_training)
# root.order.add_edge(xor, diagnostics_setup)

# The root node is now defined as the root of the POWL model
print(root)