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
skip_verify_provenance = SilentTransition()
skip_assess_condition = SilentTransition()
skip_negotiate_terms = SilentTransition()
skip_arrange_transport = SilentTransition()
skip_customs_clearance = SilentTransition()
skip_secure_insurance = SilentTransition()
skip_schedule_handlers = SilentTransition()
skip_install_artwork = SilentTransition()
skip_monitor_climate = SilentTransition()
skip_manage_security = SilentTransition()
skip_facilitate_access = SilentTransition()
skip_document_display = SilentTransition()
skip_coordinate_events = SilentTransition()
skip_inspect_periodically = SilentTransition()
skip_plan_return = SilentTransition()
skip_deinstall_artwork = SilentTransition()
skip_finalize_reports = SilentTransition()

# Define exclusive choice for each activity
verify_provenance_xor = OperatorPOWL(operator=Operator.XOR, children=[verify_provenance, skip_verify_provenance])
assess_condition_xor = OperatorPOWL(operator=Operator.XOR, children=[assess_condition, skip_assess_condition])
negotiate_terms_xor = OperatorPOWL(operator=Operator.XOR, children=[negotiate_terms, skip_negotiate_terms])
arrange_transport_xor = OperatorPOWL(operator=Operator.XOR, children=[arrange_transport, skip_arrange_transport])
customs_clearance_xor = OperatorPOWL(operator=Operator.XOR, children=[customs_clearance, skip_customs_clearance])
secure_insurance_xor = OperatorPOWL(operator=Operator.XOR, children=[secure_insurance, skip_secure_insurance])
schedule_handlers_xor = OperatorPOWL(operator=Operator.XOR, children=[schedule_handlers, skip_schedule_handlers])
install_artwork_xor = OperatorPOWL(operator=Operator.XOR, children=[install_artwork, skip_install_artwork])
monitor_climate_xor = OperatorPOWL(operator=Operator.XOR, children=[monitor_climate, skip_monitor_climate])
manage_security_xor = OperatorPOWL(operator=Operator.XOR, children=[manage_security, skip_manage_security])
facilitate_access_xor = OperatorPOWL(operator=Operator.XOR, children=[facilitate_access, skip_facilitate_access])
document_display_xor = OperatorPOWL(operator=Operator.XOR, children=[document_display, skip_document_display])
coordinate_events_xor = OperatorPOWL(operator=Operator.XOR, children=[coordinate_events, skip_coordinate_events])
inspect_periodically_xor = OperatorPOWL(operator=Operator.XOR, children=[inspect_periodically, skip_inspect_periodically])
plan_return_xor = OperatorPOWL(operator=Operator.XOR, children=[plan_return, skip_plan_return])
deinstall_artwork_xor = OperatorPOWL(operator=Operator.XOR, children=[deinstall_artwork, skip_deinstall_artwork])
finalize_reports_xor = OperatorPOWL(operator=Operator.XOR, children=[finalize_reports, skip_finalize_reports])

# Define loops for certain activities
customs_clearance_loop = OperatorPOWL(operator=Operator.LOOP, children=[customs_clearance_xor])
secure_insurance_loop = OperatorPOWL(operator=Operator.LOOP, children=[secure_insurance_xor])
manage_security_loop = OperatorPOWL(operator=Operator.LOOP, children=[manage_security_xor])
inspect_periodically_loop = OperatorPOWL(operator=Operator.LOOP, children=[inspect_periodically_xor])
plan_return_loop = OperatorPOWL(operator=Operator.LOOP, children=[plan_return_xor])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    verify_provenance_xor, assess_condition_xor, negotiate_terms_xor, arrange_transport_xor,
    customs_clearance_loop, secure_insurance_loop, schedule_handlers_xor, install_artwork_xor,
    monitor_climate_xor, manage_security_loop, facilitate_access_xor, document_display_xor,
    coordinate_events_xor, inspect_periodically_loop, plan_return_loop, deinstall_artwork_xor,
    finalize_reports_xor
])

# Define dependencies between nodes
root.order.add_edge(verify_provenance_xor, assess_condition_xor)
root.order.add_edge(assess_condition_xor, negotiate_terms_xor)
root.order.add_edge(negotiate_terms_xor, arrange_transport_xor)
root.order.add_edge(arrange_transport_xor, customs_clearance_loop)
root.order.add_edge(customs_clearance_loop, secure_insurance_loop)
root.order.add_edge(secure_insurance_loop, schedule_handlers_xor)
root.order.add_edge(schedule_handlers_xor, install_artwork_xor)
root.order.add_edge(install_artwork_xor, monitor_climate_xor)
root.order.add_edge(monitor_climate_xor, manage_security_loop)
root.order.add_edge(manage_security_loop, facilitate_access_xor)
root.order.add_edge(facilitate_access_xor, document_display_xor)
root.order.add_edge(document_display_xor, coordinate_events_xor)
root.order.add_edge(coordinate_events_xor, inspect_periodically_loop)
root.order.add_edge(inspect_periodically_loop, plan_return_loop)
root.order.add_edge(plan_return_loop, deinstall_artwork_xor)
root.order.add_edge(deinstall_artwork_xor, finalize_reports_xor)

# Print the root POWL model
print(root)