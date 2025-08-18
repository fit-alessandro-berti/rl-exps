import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
root = StrictPartialOrder(nodes=[visual_inspect, document_gather, material_test, pigment_analyze, style_compare, provenance_trace, data_crosscheck, infrared_scan, xray_fluoresce, expert_consult, forgery_detect, report_draft, stakeholder_review, final_approval, archive_store])

# Define the dependencies
root.order.add_edge(visual_inspect, document_gather)
root.order.add_edge(document_gather, material_test)
root.order.add_edge(material_test, pigment_analyze)
root.order.add_edge(pigment_analyze, style_compare)
root.order.add_edge(style_compare, provenance_trace)
root.order.add_edge(provenance_trace, data_crosscheck)
root.order.add_edge(data_crosscheck, infrared_scan)
root.order.add_edge(infrared_scan, xray_fluoresce)
root.order.add_edge(xray_fluoresce, expert_consult)
root.order.add_edge(expert_consult, forgery_detect)
root.order.add_edge(forgery_detect, report_draft)
root.order.add_edge(report_draft, stakeholder_review)
root.order.add_edge(stakeholder_review, final_approval)
root.order.add_edge(final_approval, archive_store)

# Print the POWL model
print(root)