import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the workflow
client_consult_next_spec_gathering = OperatorPOWL(operator=Operator.XOR, children=[client_consult, spec_gathering])
spec_gathering_next_supplier_sourcing = OperatorPOWL(operator=Operator.XOR, children=[spec_gathering, supplier_sourcing])
supplier_sourcing_next_design_review = OperatorPOWL(operator=Operator.XOR, children=[supplier_sourcing, design_review])
design_review_next_simulation_test = OperatorPOWL(operator=Operator.XOR, children=[design_review, simulation_test])
simulation_test_next_proto_assembly = OperatorPOWL(operator=Operator.XOR, children=[simulation_test, proto_assembly])
proto_assembly_next_quality_check = OperatorPOWL(operator=Operator.XOR, children=[proto_assembly, quality_check])
quality_check_next_firmware_flash = OperatorPOWL(operator=Operator.XOR, children=[quality_check, firmware_flash])
firmware_flash_next_sensor_install = OperatorPOWL(operator=Operator.XOR, children=[firmware_flash, sensor_install])
sensor_install_next_final_testing = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, final_testing])
final_testing_next_brand_packaging = OperatorPOWL(operator=Operator.XOR, children=[final_testing, brand_packaging])
brand_packaging_next_shipping_prep = OperatorPOWL(operator=Operator.XOR, children=[brand_packaging, shipping_prep])
shipping_prep_next_delivery_schedule = OperatorPOWL(operator=Operator.XOR, children=[shipping_prep, delivery_schedule])
delivery_schedule_next_client_training = OperatorPOWL(operator=Operator.XOR, children=[delivery_schedule, client_training])
client_training_next_diagnostics_setup = OperatorPOWL(operator=Operator.XOR, children=[client_training, diagnostics_setup])

# Define the partial order
root = StrictPartialOrder(nodes=[
    client_consult, spec_gathering, supplier_sourcing, design_review, simulation_test,
    proto_assembly, quality_check, firmware_flash, sensor_install, final_testing,
    brand_packaging, shipping_prep, delivery_schedule, client_training, diagnostics_setup
])

# Define the dependencies
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

# Print the final result
print(root)