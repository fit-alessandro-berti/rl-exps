import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
vis_inspect = Transition(label='Visual Inspect')
doc_gather = Transition(label='Document Gather')
mat_test = Transition(label='Material Test')
pig_test = Transition(label='Pigment Analyze')
style_cmp = Transition(label='Style Compare')
prov_trace = Transition(label='Provenance Trace')
data_cross = Transition(label='Data Crosscheck')
ir_scan = Transition(label='Infrared Scan')
xray_flu = Transition(label='Xray Fluoresce')
expert_cons = Transition(label='Expert Consult')
forg_detect = Transition(label='Forgery Detect')
report_draft = Transition(label='Report Draft')
stake_review = Transition(label='Stakeholder Review')
final_app = Transition(label='Final Approval')
archive_store = Transition(label='Archive Store')

# Build the loop body: Data Crosscheck -> Expert Consult -> Forgery Detect
body_loop = StrictPartialOrder(nodes=[data_cross, expert_cons, forg_detect])
body_loop.order.add_edge(data_cross, expert_cons)
body_loop.order.add_edge(expert_cons, forg_detect)

# LOOP: Provenance Trace -> Body Loop (then optionally repeat)
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[prov_trace, body_loop])

# Build the main sequence
seq_main = StrictPartialOrder(nodes=[
    vis_inspect, doc_gather, mat_test, pig_test, style_cmp,
    loop_provenance, ir_scan, xray_flu, expert_cons, forg_detect,
    report_draft, stake_review, final_app, archive_store
])
seq_main.order.add_edge(vis_inspect, doc_gather)
seq_main.order.add_edge(doc_gather, mat_test)
seq_main.order.add_edge(mat_test, pig_test)
seq_main.order.add_edge(pig_test, style_cmp)
seq_main.order.add_edge(style_cmp, loop_provenance)
seq_main.order.add_edge(loop_provenance, ir_scan)
seq_main.order.add_edge(loop_provenance, xray_flu)
seq_main.order.add_edge(ir_scan, expert_cons)
seq_main.order.add_edge(xray_flu, expert_cons)
seq_main.order.add_edge(expert_cons, forg_detect)
seq_main.order.add_edge(forg_detect, report_draft)
seq_main.order.add_edge(report_draft, stake_review)
seq_main.order.add_edge(stake_review, final_app)
seq_main.order.add_edge(final_app, archive_store)

# Final root model
root = seq_main