import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ci = Transition(label='Client Inquiry')
rg = Transition(label='Requirement Gather')
cs = Transition(label='Concept Sketch')
cf = Transition(label='Client Feedback')
rc = Transition(label='Revision Cycle')
fa = Transition(label='Final Approval')
ac = Transition(label='Art Creation')
pu = Transition(label='Progress Update')
qc = Transition(label='Quality Check')
fa2 = Transition(label='Final Adjust')
ii = Transition(label='Invoice Issue')
sp = Transition(label='Shipment Prep')
dc = Transition(label='Delivery Confirm')
ps = Transition(label='Post Support')
ls = Transition(label='License Setup')
fr = Transition(label='Frame Arrange')

# Define the iterative feedback loop: Concept Sketch -> Client Feedback -> Revision Cycle
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[cs, cf, rc])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ci, rg, feedback_loop, fa, ac, pu, qc, fa2, ii, sp, dc, ps, ls, fr
])

# Define the control-flow dependencies
root.order.add_edge(ci, rg)
root.order.add_edge(rg, feedback_loop)
root.order.add_edge(feedback_loop, fa)
root.order.add_edge(fa, ac)
root.order.add_edge(ac, pu)
root.order.add_edge(pu, qc)
root.order.add_edge(qc, fa2)
root.order.add_edge(fa2, ii)
root.order.add_edge(ii, sp)
root.order.add_edge(sp, dc)
root.order.add_edge(dc, ps)
root.order.add_edge(ps, ls)
root.order.add_edge(ps, fr)