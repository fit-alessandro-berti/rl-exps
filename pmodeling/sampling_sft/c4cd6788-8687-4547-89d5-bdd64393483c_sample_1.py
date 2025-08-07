import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ar = Transition(label='Artifact Research')
ov = Transition(label='Ownership Verify')
sm = Transition(label='Stakeholder Meet')
lr = Transition(label='Legal Review')
dc = Transition(label='Diplomatic Contact')
cr = Transition(label='Condition Report')
tp = Transition(label='Transport Plan')
isup = Transition(label='Insurance Setup')
cc = Transition(label='Customs Clear')
sp = Transition(label='Secure Packaging')
smo = Transition(label='Shipping Monitor')
cb = Transition(label='Community Brief')
ai = Transition(label='Arrival Inspect')
ep = Transition(label='Exhibit Prepare')
pr = Transition(label='Public Release')

# Loop for repeated condition reporting and secure packaging
loop = OperatorPOWL(operator=Operator.LOOP, children=[cr, sp])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ar, ov, sm, lr, dc,
    loop, tp, isup, cc, smo,
    cb, ai, ep, pr
])

# Define the control-flow dependencies
root.order.add_edge(ar, ov)
root.order.add_edge(ov, sm)
root.order.add_edge(sm, lr)
root.order.add_edge(lr, dc)
root.order.add_edge(dc, loop)
root.order.add_edge(loop, tp)
root.order.add_edge(tp, isup)
root.order.add_edge(isup, cc)
root.order.add_edge(cc, smo)
root.order.add_edge(smo, cb)
root.order.add_edge(cb, ai)
root.order.add_edge(ai, ep)
root.order.add_edge(ep, pr)