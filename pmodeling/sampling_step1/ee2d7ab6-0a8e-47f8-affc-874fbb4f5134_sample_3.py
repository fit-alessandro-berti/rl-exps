import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loops
loop_design = OperatorPOWL(operator=Operator.LOOP, children=[design_review, simulation_test])
loop_assembly = OperatorPOWL(operator=Operator.LOOP, children=[proto_assembly, quality_check])
loop_testing = OperatorPOWL(operator=Operator.LOOP, children=[firmware_flash, sensor_install, final_testing])
loop_branding = OperatorPOWL(operator=Operator.LOOP, children=[brand_packaging, shipping_prep])
loop_delivery = OperatorPOWL(operator=Operator.LOOP, children=[delivery_schedule, client_training, diagnostics_setup])

# Define root model
root = StrictPartialOrder(nodes=[client_consult, spec_gathering, supplier_sourcing, loop_design, loop_assembly, loop_testing, loop_branding, loop_delivery])
root.order.add_edge(client_consult, spec_gathering)
root.order.add_edge(spec_gathering, supplier_sourcing)
root.order.add_edge(supplier_sourcing, loop_design)
root.order.add_edge(loop_design, loop_assembly)
root.order.add_edge(loop_assembly, loop_testing)
root.order.add_edge(loop_testing, loop_branding)
root.order.add_edge(loop_branding, loop_delivery)