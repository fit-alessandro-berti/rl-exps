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

# Define silent activities
skip = SilentTransition()

# Define the POWL model
loop_verify = OperatorPOWL(operator=Operator.LOOP, children=[verify_provenance, assess_condition])
loop_inspect = OperatorPOWL(operator=Operator.LOOP, children=[inspect_periodically, finalize_reports])
xor_customs_insurance = OperatorPOWL(operator=Operator.XOR, children=[customs_clearance, secure_insurance])
xor_transport_inspect = OperatorPOWL(operator=Operator.XOR, children=[arrange_transport, inspect_periodically])
xor_inspect_schedule = OperatorPOWL(operator=Operator.XOR, children=[inspect_periodically, schedule_handlers])
xor_inspect_install = OperatorPOWL(operator=Operator.XOR, children=[inspect_periodically, install_artwork])
xor_inspect_manage = OperatorPOWL(operator=Operator.XOR, children=[inspect_periodically, manage_security])
xor_inspect_access = OperatorPOWL(operator=Operator.XOR, children=[inspect_periodically, facilitate_access])
xor_inspect_display = OperatorPOWL(operator=Operator.XOR, children=[inspect_periodically, document_display])
xor_inspect_events = OperatorPOWL(operator=Operator.XOR, children=[inspect_periodically, coordinate_events])
xor_inspect_plan = OperatorPOWL(operator=Operator.XOR, children=[inspect_periodically, plan_return])
xor_inspect_deinstall = OperatorPOWL(operator=Operator.XOR, children=[inspect_periodically, deinstall_artwork])

# Define the root node
root = StrictPartialOrder(nodes=[
    loop_verify,
    xor_customs_insurance,
    xor_transport_inspect,
    xor_inspect_schedule,
    xor_inspect_install,
    xor_inspect_manage,
    xor_inspect_access,
    xor_inspect_display,
    xor_inspect_events,
    xor_inspect_plan,
    xor_inspect_deinstall,
    finalize_reports
])

# Define the dependencies
root.order.add_edge(loop_verify, xor_inspect_schedule)
root.order.add_edge(xor_customs_insurance, xor_inspect_manage)
root.order.add_edge(xor_transport_inspect, xor_inspect_install)
root.order.add_edge(xor_inspect_schedule, xor_inspect_manage)
root.order.add_edge(xor_inspect_install, xor_inspect_manage)
root.order.add_edge(xor_inspect_manage, xor_inspect_access)
root.order.add_edge(xor_inspect_access, xor_inspect_display)
root.order.add_edge(xor_inspect_display, xor_inspect_events)
root.order.add_edge(xor_inspect_events, xor_inspect_plan)
root.order.add_edge(xor_inspect_plan, xor_inspect_deinstall)
root.order.add_edge(xor_inspect_deinstall, finalize_reports)

# Print the POWL model
print(root)