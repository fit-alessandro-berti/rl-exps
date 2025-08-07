import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
wa = Transition(label='Wear Analysis')
ic = Transition(label='Image Capture')
pm = Transition(label='Pattern Match')
ov = Transition(label='Ownership Verify')
er = Transition(label='Ethics Review')
cd = Transition(label='Carbon Dating')
re = Transition(label='Restoration Eval')
rd = Transition(label='Report Draft')
sr = Transition(label='Stakeholder Review')
ad = Transition(label='Archive Data')
ea = Transition(label='Exhibit Approve')
cm = Transition(label='Condition Monitor')
fc = Transition(label='Final Certification')

# Build the loop body for condition monitoring
loop_body = StrictPartialOrder(nodes=[cm, fc])
loop_body.order.add_edge(cm, fc)

# Loop: perform condition monitoring repeatedly until final certification
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, pc])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    pc, ms, wa, ic, pm, ov, er, cd, re, rd, sr, ad, ea, loop
])

# Sequential dependencies
root.order.add_edge(pc, ms)
root.order.add_edge(pc, wa)
root.order.add_edge(pc, ov)
root.order.add_edge(ms, pm)
root.order.add_edge(wa, pm)
root.order.add_edge(ov, pm)
root.order.add_edge(pm, er)
root.order.add_edge(er, cd)
root.order.add_edge(cd, re)
root.order.add_edge(re, rd)
root.order.add_edge(rd, sr)
root.order.add_edge(sr, ad)
root.order.add_edge(ad, ea)
root.order.add_edge(ea, loop)