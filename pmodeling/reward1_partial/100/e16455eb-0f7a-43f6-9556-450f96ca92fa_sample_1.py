import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL transitions
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[customs_clearance, secure_insurance])
loop = OperatorPOWL(operator=Operator.LOOP, children=[schedule_handlers, install_artwork, manage_security, facilitate_access, document_display, coordinate_events, inspect_periodically, plan_return, deinstall_artwork, finalize_reports])
root = StrictPartialOrder(nodes=[verify_provenance, assess_condition, negotiate_terms, arrange_transport, xor, loop])
root.order.add_edge(verify_provenance, assess_condition)
root.order.add_edge(assess_condition, negotiate_terms)
root.order.add_edge(negotiate_terms, arrange_transport)
root.order.add_edge(arrange_transport, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, loop)