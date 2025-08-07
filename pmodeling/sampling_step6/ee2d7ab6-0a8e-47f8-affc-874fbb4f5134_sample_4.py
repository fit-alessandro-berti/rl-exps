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

# Define the partial order
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

# Add dependencies between activities (POWL model)
# Note: This is a simplified representation and may not capture all dependencies accurately.
# You would need to add the appropriate dependencies based on the process flow.
# For example, client_consult -> spec_gathering, etc.

# Example dependency: Client Consult -> Spec Gathering
root.order.add_edge(client_consult, spec_gathering)

# Continue adding dependencies as needed

# The final result is stored in 'root'