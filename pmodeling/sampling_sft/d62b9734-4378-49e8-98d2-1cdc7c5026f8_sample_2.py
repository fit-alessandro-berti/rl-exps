import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
pc = Transition(label='Provenance Check')
ic = Transition(label='Image Capture')
ms = Transition(label='Material Scan')
ec = Transition(label='Expert Review')
hc = Transition(label='Historical Cross')
lv = Transition(label='Legal Verify')
rs = Transition(label='Registry Search')
cu = Transition(label='Customs Clear')
ca = Transition(label='Condition Assess')
dl = Transition(label='Data Log')
cc = Transition(label='Chain Custody')
rd = Transition(label='Report Draft')
cert = Transition(label='Certification')
sa = Transition(label='Secure Archive')
ap = Transition(label='Auction Prep')

# Define the multi‐spectral imaging & material composition analysis as a partial order
po_analysis = StrictPartialOrder(nodes=[ic, ms])
po_analysis.order.add_edge(ic, ms)

# Define the chain-of-custody loop: Data Log -> Chain Custody, repeated until exit
skip = SilentTransition()
loop_chain = OperatorPOWL(operator=Operator.LOOP, children=[dl, cc])

# Build the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    pc, po_analysis, ec, hc, lv, rs, cu, ca, loop_chain,
    rd, cert, sa, ap
])

# Sequential flow: Provenance Check -> Imaging/Analysis -> Expert Review -> Historical Cross
root.order.add_edge(pc, po_analysis)
root.order.add_edge(po_analysis, ec)
root.order.add_edge(ec, hc)

# Legal and registry verification can happen in parallel
root.order.add_edge(pc, lv)
root.order.add_edge(lv, rs)
root.order.add_edge(rs, cu)

# After imaging and analysis, proceed to condition assessment and then chain-of-custody loop
root.order.add_edge(po_analysis, ca)
root.order.add_edge(ca, loop_chain)

# After chain-of-custody, draft report and certification
root.order.add_edge(loop_chain, rd)
root.order.add_edge(rd, cert)

# Final steps: Secure Archive and Auction Prep
root.order.add_edge(cert, sa)
root.order.add_edge(sa, ap)