import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
provenance_check    = Transition(label='Provenance Check')
material_scan       = Transition(label='Material Scan')
wear_analysis       = Transition(label='Wear Analysis')
image_capture       = Transition(label='Image Capture')
pattern_match       = Transition(label='Pattern Match')
ownership_verify    = Transition(label='Ownership Verify')
ethics_review       = Transition(label='Ethics Review')
carbon_dating       = Transition(label='Carbon Dating')
restoration_eval    = Transition(label='Restoration Eval')
condition_monitor   = Transition(label='Condition Monitor')
report_draft        = Transition(label='Report Draft')
stakeholder_review  = Transition(label='Stakeholder Review')
archive_data        = Transition(label='Archive Data')
final_certification = Transition(label='Final Certification')
exhibit_approve     = Transition(label='Exhibit Approve')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    provenance_check, material_scan, wear_analysis, image_capture,
    pattern_match, ownership_verify, ethics_review, carbon_dating,
    restoration_eval, condition_monitor, report_draft,
    stakeholder_review, archive_data, final_certification, exhibit_approve
])

# Define the control‐flow dependencies
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(provenance_check, wear_analysis)
root.order.add_edge(material_scan, pattern_match)
root.order.add_edge(wear_analysis, pattern_match)
root.order.add_edge(pattern_match, ownership_verify)
root.order.add_edge(ownership_verify, ethics_review)
root.order.add_edge(ethics_review, carbon_dating)
root.order.add_edge(carbon_dating, restoration_eval)
root.order.add_edge(restoration_eval, condition_monitor)
root.order.add_edge(condition_monitor, report_draft)
root.order.add_edge(report_draft, stakeholder_review)
root.order.add_edge(stakeholder_review, archive_data)
root.order.add_edge(archive_data, final_certification)
root.order.add_edge(final_certification, exhibit_approve)

# Print the model for verification
print(root)