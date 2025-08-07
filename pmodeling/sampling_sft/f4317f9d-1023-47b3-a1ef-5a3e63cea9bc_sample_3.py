import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
ic = Transition(label='AI Imaging')
sc = Transition(label='Style Compare')
ct = Transition(label='Chemical Test')
av = Transition(label='Aging Verify')
rm = Transition(label='Record Match')
dq = Transition(label='Database Query')
pr = Transition(label='Panel Review')
fr = Transition(label='Forgery Risk')
mv = Transition(label='Market Value')
rd = Transition(label='Report Draft')
cs = Transition(label='Certification')
asg = Transition(label='Approval Stage')
sp = Transition(label='Secure Packing')
tp = Transition(label='Transport Prep')

# Loop for cross-checking database and record
cross_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[dq, rm]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, ms, ic, sc, cross_loop,
    ct, av, pr, fr, mv,
    rd, cs, asg,
    sp, tp
])

# Add ordering constraints
root.order.add_edge(pc, ms)
root.order.add_edge(pc, ic)
root.order.add_edge(ms, sc)
root.order.add_edge(ic, sc)
root.order.add_edge(sc, cross_loop)
root.order.add_edge(cross_loop, ct)
root.order.add_edge(ct, av)
root.order.add_edge(av, pr)
root.order.add_edge(pr, fr)
root.order.add_edge(fr, mv)
root.order.add_edge(mv, rd)
root.order.add_edge(rd, cs)
root.order.add_edge(cs, asg)
root.order.add_edge(asg, sp)
root.order.add_edge(sp, tp)