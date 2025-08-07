import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
verify = Transition(label='Verify Provenance')
assess = Transition(label='Assess Condition')
negotiate = Transition(label='Negotiate Terms')
arrange = Transition(label='Arrange Transport')
clearance = Transition(label='Customs Clearance')
secure = Transition(label='Secure Insurance')
schedule = Transition(label='Schedule Handlers')
install = Transition(label='Install Artwork')
monitor = Transition(label='Monitor Climate')
manage = Transition(label='Manage Security')
access = Transition(label='Facilitate Access')
doc_display = Transition(label='Document Display')
events = Transition(label='Coordinate Events')
inspect = Transition(label='Inspect Periodically')
plan_return = Transition(label='Plan Return')
deinstall = Transition(label='Deinstall Artwork')
finalize = Transition(label='Finalize Reports')

# Loop for periodic inspection and display documentation
inspection_loop = OperatorPOWL(operator=Operator.LOOP, children=[inspect, doc_display])

# Build the partial order
root = StrictPartialOrder(nodes=[
    verify, assess, negotiate,
    arrange, clearance, secure,
    schedule, install, monitor, manage,
    access, events,
    inspection_loop,
    plan_return, deinstall, finalize
])

# Define the control-flow dependencies
root.order.add_edge(verify, assess)
root.order.add_edge(assess, negotiate)
root.order.add_edge(negotiate, arrange)
root.order.add_edge(arrange, clearance)
root.order.add_edge(clearance, secure)
root.order.add_edge(secure, schedule)
root.order.add_edge(schedule, install)
root.order.add_edge(install, monitor)
root.order.add_edge(monitor, manage)
root.order.add_edge(manage, access)
root.order.add_edge(access, events)
root.order.add_edge(events, inspection_loop)
root.order.add_edge(inspection_loop, plan_return)
root.order.add_edge(plan_return, deinstall)
root.order.add_edge(deinstall, finalize)