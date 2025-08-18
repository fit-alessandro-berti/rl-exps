import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Visual Inspection and Document Gathering
root = StrictPartialOrder(nodes=[visual_inspect, document_gather])

# Material Testing
material_test_order = StrictPartialOrder(nodes=[material_test])
root.order.add_edge(root, material_test_order)

# Pigment Analysis
pigment_analyze_order = StrictPartialOrder(nodes=[pigment_analyze])
root.order.add_edge(material_test_order, pigment_analyze_order)

# Style Comparison
style_compare_order = StrictPartialOrder(nodes=[style_compare])
root.order.add_edge(pigment_analyze_order, style_compare_order)

# Provenance Tracing
provenance_trace_order = StrictPartialOrder(nodes=[provenance_trace])
root.order.add_edge(style_compare_order, provenance_trace_order)

# Data Crosscheck
data_crosscheck_order = StrictPartialOrder(nodes=[data_crosscheck])
root.order.add_edge(provenance_trace_order, data_crosscheck_order)

# Infrared Scan
infrared_scan_order = StrictPartialOrder(nodes=[infrared_scan])
root.order.add_edge(data_crosscheck_order, infrared_scan_order)

# X-Ray Fluorescence
xray_fluoresce_order = StrictPartialOrder(nodes=[xray_fluoresce])
root.order.add_edge(infrared_scan_order, xray_fluoresce_order)

# Expert Consultation
expert_consult_order = StrictPartialOrder(nodes=[expert_consult])
root.order.add_edge(xray_fluoresce_order, expert_consult_order)

# Forgery Detection
forgery_detect_order = StrictPartialOrder(nodes=[forgery_detect])
root.order.add_edge(expert_consult_order, forgery_detect_order)

# Report Drafting
report_draft_order = StrictPartialOrder(nodes=[report_draft])
root.order.add_edge(forgery_detect_order, report_draft_order)

# Stakeholder Review
stakeholder_review_order = StrictPartialOrder(nodes=[stakeholder_review])
root.order.add_edge(report_draft_order, stakeholder_review_order)

# Final Approval
final_approval_order = StrictPartialOrder(nodes=[final_approval])
root.order.add_edge(stakeholder_review_order, final_approval_order)

# Archive Storage
archive_store_order = StrictPartialOrder(nodes=[archive_store])
root.order.add_edge(final_approval_order, archive_store_order)