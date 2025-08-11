import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
verify_provenance = Transition(label='Verify Provenance')
assess_condition = Transition(label='Assess Condition')
negotiate_terms = Transition(label='Negotiate Terms')
arrange_transport = Transition(label='Arrange Transport')
customs_clearance = Transition(label='Customs Clearance')
secure_insurance = Transition(label='Secure Insurance')
schedule_handlers = Transition(label='Schedule Handlers')
install_artwork = Transition(label='Install Artwork')
monitor_climate = Transition(label='Monitor Climate')
manage_security = Transition(label='Manage Security')
facilitate_access = Transition(label='Facilitate Access')
document_display = Transition(label='Document Display')
coordinate_events = Transition(label='Coordinate Events')
inspect_periodically = Transition(label='Inspect Periodically')
plan_return = Transition(label='Plan Return')
deinstall_artwork = Transition(label='Deinstall Artwork')
finalize_reports = Transition(label='Finalize Reports')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
arrange_loop = OperatorPOWL(operator=Operator.LOOP, children=[arrange_transport, customs_clearance, secure_insurance])
schedule_loop = OperatorPOWL(operator=Operator.LOOP, children=[schedule_handlers, manage_security])
install_loop = OperatorPOWL(operator=Operator.LOOP, children=[install_artwork, monitor_climate, secure_security])
inspect_loop = OperatorPOWL(operator=Operator.LOOP, children=[inspect_periodically, plan_return])
deinstall_loop = OperatorPOWL(operator=Operator.LOOP, children=[deinstall_artwork, finalize_reports])

# Define XOR nodes
xor_loop = OperatorPOWL(operator=Operator.XOR, children=[inspect_loop, skip])

# Define root node
root = StrictPartialOrder(nodes=[arrange_loop, schedule_loop, install_loop, inspect_loop, deinstall_loop, xor_loop])

# Define the order dependencies
root.order.add_edge(arrange_loop, schedule_loop)
root.order.add_edge(schedule_loop, install_loop)
root.order.add_edge(install_loop, inspect_loop)
root.order.add_edge(inspect_loop, deinstall_loop)
root.order.add_edge(deinstall_loop, xor_loop)
root.order.add_edge(xor_loop, inspect_loop)

# Print the root node
print(root)