import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
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

skip = SilentTransition()

# Define the POWL model
loop_verify = OperatorPOWL(operator=Operator.LOOP, children=[verify_provenance, assess_condition, negotiate_terms])
loop_transport = OperatorPOWL(operator=Operator.LOOP, children=[arrange_transport, customs_clearance, secure_insurance])
loop_schedule = OperatorPOWL(operator=Operator.LOOP, children=[schedule_handlers, install_artwork, monitor_climate, manage_security, facilitate_access, document_display, coordinate_events, inspect_periodically])
loop_return = OperatorPOWL(operator=Operator.LOOP, children=[plan_return, deinstall_artwork, finalize_reports])

xor_inspect = OperatorPOWL(operator=Operator.XOR, children=[loop_schedule, skip])

root = StrictPartialOrder(nodes=[loop_verify, loop_transport, loop_schedule, loop_return, xor_inspect])
root.order.add_edge(loop_verify, loop_transport)
root.order.add_edge(loop_transport, loop_schedule)
root.order.add_edge(loop_schedule, loop_return)
root.order.add_edge(loop_return, xor_inspect)