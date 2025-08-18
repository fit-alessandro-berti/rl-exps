from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
meet = Transition(label='Client Meet')
capture = Transition(label='Vision Capture')
draft = Transition(label='Concept Draft')
feedback = Transition(label='Feedback Loop')
source = Transition(label='Material Sourcing')
select = Transition(label='Vendor Selection')
assign = Transition(label='Artisan Assign')
build = Transition(label='Prototype Build')
review = Transition(label='Quality Review')
check = Transition(label='Technical Check')
approve = Transition(label='Final Approval')
pack = Transition(label='Packaging Prep')
plan = Transition(label='Logistics Plan')
transport = Transition(label='Secure Transport')
install = Transition(label='Installation Set')
support = Transition(label='Client Support')
record = Transition(label='Archival Record')

# Define the partial order
root = StrictPartialOrder(nodes=[
    meet, capture, draft, feedback, source, select, assign, build, review, check, approve,
    pack, plan, transport, install, support, record
])

# Define the order
root.order.add_edge(meet, capture)
root.order.add_edge(capture, draft)
root.order.add_edge(draft, feedback)
root.order.add_edge(feedback, source)
root.order.add_edge(source, select)
root.order.add_edge(select, assign)
root.order.add_edge(assign, build)
root.order.add_edge(build, review)
root.order.add_edge(review, check)
root.order.add_edge(check, approve)
root.order.add_edge(approve, pack)
root.order.add_edge(pack, plan)
root.order.add_edge(plan, transport)
root.order.add_edge(transport, install)
root.order.add_edge(install, support)
root.order.add_edge(support, record)