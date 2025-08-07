import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    visual_inspect,
    document_gather,
    material_test,
    pigment_analyze,
    style_compare,
    provenance_trace,
    data_crosscheck,
    infrared_scan,
    xray_fluoresce,
    expert_consult,
    forgery_detect,
    report_draft,
    stakeholder_review,
    final_approval,
    archive_store
])

# Define dependencies
root.order.add_edge(visual_inspect, document_gather)
root.order.add_edge(visual_inspect, material_test)
root.order.add_edge(visual_inspect, pigment_analyze)
root.order.add_edge(visual_inspect, style_compare)
root.order.add_edge(visual_inspect, provenance_trace)
root.order.add_edge(visual_inspect, data_crosscheck)
root.order.add_edge(visual_inspect, infrared_scan)
root.order.add_edge(visual_inspect, xray_fluoresce)
root.order.add_edge(visual_inspect, expert_consult)
root.order.add_edge(visual_inspect, forgery_detect)
root.order.add_edge(visual_inspect, report_draft)
root.order.add_edge(visual_inspect, stakeholder_review)
root.order.add_edge(visual_inspect, final_approval)
root.order.add_edge(visual_inspect, archive_store)