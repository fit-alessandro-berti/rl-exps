import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
visual_inspect = Transition(label='Visual Inspect')
document_gather = Transition(label='Document Gather')
material_test = Transition(label='Material Test')
pigment_analyze = Transition(label='Pigment Analyze')
style_compare = Transition(label='Style Compare')
provenance_trace = Transition(label='Provenance Trace')
data_crosscheck = Transition(label='Data Crosscheck')
infrared_scan = Transition(label='Infrared Scan')
xray_fluoresce = Transition(label='Xray Fluoresce')
expert_consult = Transition(label='Expert Consult')
forgery_detect = Transition(label='Forgery Detect')
report_draft = Transition(label='Report Draft')
stakeholder_review = Transition(label='Stakeholder Review')
final_approval = Transition(label='Final Approval')
archive_store = Transition(label='Archive Store')

# Build the loop body: Expert Consult -> Forgery Detect -> Report Draft
body = StrictPartialOrder(nodes=[expert_consult, forgery_detect, report_draft])
body.order.add_edge(expert_consult, forgery_detect)
body.order.add_edge(forgery_detect, report_draft)

# Loop: Provenance Trace -> Data Crosscheck -> body
loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_trace, data_crosscheck])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    visual_inspect,
    document_gather,
    material_test,
    pigment_analyze,
    style_compare,
    loop,
    stakeholder_review,
    final_approval,
    archive_store
])

# Define the control-flow dependencies
root.order.add_edge(visual_inspect, document_gather)
root.order.add_edge(document_gather, material_test)
root.order.add_edge(material_test, pigment_analyze)
root.order.add_edge(pigment_analyze, style_compare)
root.order.add_edge(style_compare, loop)
root.order.add_edge(loop, stakeholder_review)
root.order.add_edge(stakeholder_review, final_approval)
root.order.add_edge(final_approval, archive_store)