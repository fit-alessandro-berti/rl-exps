import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
pc = Transition(label='Provenance Check')
ic = Transition(label='Image Capture')
ms = Transition(label='Material Scan')
ec = Transition(label='Expert Review')
hc = Transition(label='Historical Cross')
lv = Transition(label='Legal Verify')
rs = Transition(label='Registry Search')
cs = Transition(label='Customs Clear')
ca = Transition(label='Condition Assess')
dl = Transition(label='Data Log')
cc = Transition(label='Chain Custody')
rd = Transition(label='Report Draft')
cert = Transition(label='Certification')
sa = Transition(label='Secure Archive')
ap = Transition(label='Auction Prep')

# Loop for repeated logging and custody checks
loop_po = StrictPartialOrder(nodes=[dl, cc])
loop_po.order.add_edge(dl, cc)
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_po, loop_po])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    pc, ic, ms, ec, hc, lv, rs, cs, ca, loop, rd, cert, sa, ap
])

# Sequence of activities before the loop
root.order.add_edge(pc, ic)
root.order.add_edge(ic, ms)
root.order.add_edge(ms, ec)
root.order.add_edge(ec, hc)
root.order.add_edge(hc, lv)
root.order.add_edge(lv, rs)
root.order.add_edge(rs, cs)
root.order.add_edge(cs, ca)

# After the loop, draft the report and issue certification
root.order.add_edge(ca, rd)
root.order.add_edge(rd, cert)

# Finally, archive securely and prepare for auction
root.order.add_edge(cert, sa)
root.order.add_edge(sa, ap)