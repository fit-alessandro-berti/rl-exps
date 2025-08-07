import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
pc = Transition(label='Provenance Check')
sc = Transition(label='Spectroscopy Test')
cd = Transition(label='Carbon Dating')
sa = Transition(label='Style Analysis')
is_img = Transition(label='Image Scanning')
rs_img = Transition(label='Restoration Scan')
ap = Transition(label='Appraiser Review')
dm = Transition(label='Database Match')
be = Transition(label='Blockchain Entry')
ci = Transition(label='Certificate Issue')
fd = Transition(label='Forgery Detect')
rc = Transition(label='Report Compilation')
cb = Transition(label='Client Briefing')
ss = Transition(label='Secure Storage')
fa = Transition(label='Final Approval')

# Build the partial‐order sub‐workflow for scientific testing
scientific_tests = StrictPartialOrder(nodes=[sc, cd, sa, is_img, rs_img])
scientific_tests.order.add_edge(sc, sa)
scientific_tests.order.add_edge(cd, sa)
scientific_tests.order.add_edge(sa, is_img)
scientific_tests.order.add_edge(is_img, rs_img)

# Build the partial‐order sub‐workflow for cross‐database matching
db_workflow = StrictPartialOrder(nodes=[dm])
# No edges needed as these tests run in parallel

# Build the partial‐order sub‐workflow for forgery detection and report compilation
forgery_seq = StrictPartialOrder(nodes=[fd, rc])
forgery_seq.order.add_edge(fd, rc)

# Build the partial‐order sub‐workflow for final approval and storage
final_seq = StrictPartialOrder(nodes=[fa, ss])
final_seq.order.add_edge(fa, ss)

# Build the main partial order with the control‐flow operators
root = StrictPartialOrder(nodes=[
    pc, scientific_tests, db_workflow, forgery_seq, ci, cb, final_seq
])

# Sequential control‐flow: Provenance Check -> scientific tests -> database match -> forgery detection -> report compilation -> blockchain entry -> certificate issue -> final approval -> storage
root.order.add_edge(pc, scientific_tests)
root.order.add_edge(scientific_tests, db_workflow)
root.order.add_edge(db_workflow, forgery_seq)
root.order.add_edge(forgery_seq, ci)
root.order.add_edge(ci, cb)
root.order.add_edge(cb, final_seq)
root.order.add_edge(final_seq, ss)