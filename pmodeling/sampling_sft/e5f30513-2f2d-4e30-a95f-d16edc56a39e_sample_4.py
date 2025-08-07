import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
ir = Transition(label='Intake Review')
pi = Transition(label='Preliminary Inspect')
pc = Transition(label='Provenance Check')
ar = Transition(label='Archival Research')
mt = Transition(label='Material Testing')
rd = Transition(label='Radiocarbon Date')
sa = Transition(label='Stylistic Assess')
ec = Transition(label='Expert Consult')
fc = Transition(label='Findings Compile')
irv = Transition(label='Internal Review')
cp = Transition(label='Client Present')
ac = Transition(label='Approval Confirm')
sp = Transition(label='Secure Package')
ta = Transition(label='Transport Arrange')
cc = Transition(label='Chain Custody')

# Build the loop body for scientific analysis
analysis_loop = StrictPartialOrder(nodes=[mt, rd, sa])
analysis_loop.order.add_edge(mt, rd)
analysis_loop.order.add_edge(rd, sa)

# Build the loop for expert consultation
consult_loop = StrictPartialOrder(nodes=[ec])
consult_loop.order.add_edge(ec, ec)  # self-loop for repeating the consultation

# Build the loop for archival research
research_loop = StrictPartialOrder(nodes=[ar])
research_loop.order.add_edge(ar, ar)  # self-loop for repeating the research

# Build the loop for provenance verification
provenance_loop = StrictPartialOrder(nodes=[pc])
provenance_loop.order.add_edge(pc, pc)  # self-loop for repeating the check

# Build the main workflow as a partial order
root = StrictPartialOrder(nodes=[
    ir, pi, pc, ar, analysis_loop,
    sa, ec, consult_loop,
    mt, rd,
    fc, irv, cp, ac, sp, ta, cc
])

# Initial intake and inspection
root.order.add_edge(ir, pi)

# Provenance loop: after preliminary inspect, run provenance check and archival research in parallel
root.order.add_edge(pi, provenance_loop)
root.order.add_edge(provenance_loop, provenance_loop)

# After provenance loop, run stylistic assessment and material testing in parallel
root.order.add_edge(provenance_loop, sa)
root.order.add_edge(provenance_loop, mt)

# Parallel scientific analysis loop: run material testing, radiocarbon date, and stylistic assessment in parallel
root.order.add_edge(sa, analysis_loop)
root.order.add_edge(mt, analysis_loop)

# Expert consultation loop: after stylistic assessment, run expert consultation in parallel
root.order.add_edge(sa, consult_loop)

# After expert consultation loop, compile findings
root.order.add_edge(consult_loop, fc)

# After findings compilation, review internally and present to client
root.order.add_edge(fc, irv)
root.order.add_edge(irv, cp)

# After client approval, confirm, package securely, and arrange transport
root.order.add_edge(cp, ac)
root.order.add_edge(ac, sp)
root.order.add_edge(sp, ta)

# Finally, ensure chain-of-custody protocols are followed
root.order.add_edge(ta, cc)