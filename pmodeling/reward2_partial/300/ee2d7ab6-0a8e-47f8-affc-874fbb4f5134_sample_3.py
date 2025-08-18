import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define POWL model nodes
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

# Define POWL model structure
root = StrictPartialOrder(nodes=[
    client_consult, spec_gathering, supplier_sourcing, design_review, simulation_test,
    proto_assembly, quality_check, firmware_flash, sensor_install, final_testing,
    brand_packaging, shipping_prep, delivery_schedule, client_training, diagnostics_setup
])

# Define dependencies
root.order.add_edge(client_consult, spec_gathering)
root.order.add_edge(spec_gathering, supplier_sourcing)
root.order.add_edge(supplier_sourcing, design_review)
root.order.add_edge(design_review, simulation_test)
root.order.add_edge(simulation_test, proto_assembly)
root.order.add_edge(proto_assembly, quality_check)
root.order.add_edge(quality_check, firmware_flash)
root.order.add_edge(firmware_flash, sensor_install)
root.order.add_edge(sensor_install, final_testing)
root.order.add_edge(final_testing, brand_packaging)
root.order.add_edge(brand_packaging, shipping_prep)
root.order.add_edge(shipping_prep, delivery_schedule)
root.order.add_edge(delivery_schedule, client_training)
root.order.add_edge(client_training, diagnostics_setup)

print(root)