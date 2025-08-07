import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ir = Transition(label='Intake Review')
pi = Transition(label='Preliminary Inspect')
pc = Transition(label='Provenance Check')
ar = Transition(label='Archival Research')
mt = Transition(label='Material Testing')
rd = Transition(label='Radiocarbon Date')
sa = Transition(label='Stylistic Assess')
ec = Transition(label='Expert Consult')
fc = Transition(label='Findings Compile')
irr = Transition(label='Internal Review')
cp = Transition(label='Client Present')
ac = Transition(label='Approval Confirm')
sp = Transition(label='Secure Package')
ta = Transition(label='Transport Arrange')
cc = Transition(label='Chain Custody')

# Build the partial order
root = StrictPartialOrder(nodes=[
    ir, pi, pc, ar,
    mt, rd, sa,
    ec, fc,
    irr, cp, ac,
    sp, ta, cc
])

# Define the control-flow dependencies
root.order.add_edge(ir, pi)
root.order.add_edge(pi, pc)
root.order.add_edge(pc, ar)
root.order.add_edge(ar, mt)
root.order.add_edge(ar, rd)
root.order.add_edge(mt, sa)
root.order.add_edge(rd, sa)
root.order.add_edge(sa, ec)
root.order.add_edge(ec, fc)
root.order.add_edge(fc, irr)
root.order.add_edge(irr, cp)
root.order.add_edge(cp, ac)
root.order.add_edge(ac, sp)
root.order.add_edge(sp, ta)
root.order.add_edge(ta, cc)