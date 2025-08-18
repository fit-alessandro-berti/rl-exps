import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    verify_provenance,
    assess_condition,
    negotiate_terms,
    arrange_transport,
    customs_clearance,
    secure_insurance,
    schedule_handlers,
    install_artwork,
    monitor_climate,
    manage_security,
    facilitate_access,
    document_display,
    coordinate_events,
    inspect_periodically,
    plan_return,
    deinstall_artwork,
    finalize_reports
])

# Define the order (dependencies)
root.order.add_edge(verify_provenance, assess_condition)
root.order.add_edge(assess_condition, negotiate_terms)
root.order.add_edge(negotiate_terms, arrange_transport)
root.order.add_edge(arrange_transport, customs_clearance)
root.order.add_edge(customs_clearance, secure_insurance)
root.order.add_edge(secure_insurance, schedule_handlers)
root.order.add_edge(schedule_handlers, install_artwork)
root.order.add_edge(install_artwork, monitor_climate)
root.order.add_edge(monitor_climate, manage_security)
root.order.add_edge(manage_security, facilitate_access)
root.order.add_edge(facilitate_access, document_display)
root.order.add_edge(document_display, coordinate_events)
root.order.add_edge(coordinate_events, inspect_periodically)
root.order.add_edge(inspect_periodically, plan_return)
root.order.add_edge(plan_return, deinstall_artwork)
root.order.add_edge(deinstall_artwork, finalize_reports)

print(root)