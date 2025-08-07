import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
verify = Transition(label='Verify Provenance')
assess = Transition(label='Assess Condition')
negotiate = Transition(label='Negotiate Terms')
arrange = Transition(label='Arrange Transport')
clearance = Transition(label='Customs Clearance')
insurance = Transition(label='Secure Insurance')
schedule = Transition(label='Schedule Handlers')
install = Transition(label='Install Artwork')
monitor = Transition(label='Monitor Climate')
manage = Transition(label='Manage Security')
access = Transition(label='Facilitate Access')
document = Transition(label='Document Display')
events = Transition(label='Coordinate Events')
inspect = Transition(label='Inspect Periodically')
plan_return = Transition(label='Plan Return')
deinstall = Transition(label='Deinstall Artwork')
finalize = Transition(label='Finalize Reports')

# Loop for periodic inspections: do Inspect, then choose to exit or do Inspect again
inspection_loop = OperatorPOWL(operator=Operator.LOOP, children=[inspect, inspect])

# Build the partial order
root = StrictPartialOrder(nodes=[
    verify, assess, negotiate, arrange, clearance,
    insurance, schedule, install, monitor, manage,
    access, document, events, inspection_loop,
    plan_return, deinstall, finalize
])

# Define the control-flow edges
root.order.add_edge(verify, assess)
root.order.add_edge(assess, negotiate)
root.order.add_edge(negotiate, arrange)
root.order.add_edge(arrange, clearance)
root.order.add_edge(clearance, insurance)
root.order.add_edge(insurance, schedule)
root.order.add_edge(schedule, install)
root.order.add_edge(install, monitor)
root.order.add_edge(monitor, manage)
root.order.add_edge(manage, access)
root.order.add_edge(access, document)
root.order.add_edge(document, events)
root.order.add_edge(events, inspection_loop)
root.order.add_edge(inspection_loop, plan_return)
root.order.add_edge(plan_return, deinstall)
root.order.add_edge(deinstall, finalize)