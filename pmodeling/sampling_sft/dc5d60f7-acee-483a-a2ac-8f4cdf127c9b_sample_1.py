import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ir = Transition(label='Intake Review')
cs = Transition(label='Condition Scan')
mt = Transition(label='Material Test')
sm = Transition(label='Style Match')
pl = Transition(label='Provenance Log')
fr = Transition(label='Forgery Risk')
la = Transition(label='Legal Audit')
ep = Transition(label='Expert Panel')
dc = Transition(label='Data Crosscheck')
rd = Transition(label='Report Draft')
bt = Transition(label='Blockchain Tag')
cert = Transition(label='Certification')
cf = Transition(label='Client Feedback')
fa = Transition(label='Final Approval')
rp = Transition(label='Release Prep')

# Build the loop for iterative feedback
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cf, fa]
)

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    ir, cs, mt, sm, pl, fr, la, ep, dc, rd, bt, cert,
    feedback_loop, rp
])

# Define the control-flow edges
root.order.add_edge(ir, cs)
root.order.add_edge(ir, mt)
root.order.add_edge(cs, sm)
root.order.add_edge(mt, sm)
root.order.add_edge(sm, pl)
root.order.add_edge(pl, fr)
root.order.add_edge(fr, la)
root.order.add_edge(la, ep)
root.order.add_edge(ep, dc)
root.order.add_edge(dc, rd)
root.order.add_edge(rd, bt)
root.order.add_edge(bt, cert)
root.order.add_edge(cert, feedback_loop)
root.order.add_edge(feedback_loop, rp)

print(root)