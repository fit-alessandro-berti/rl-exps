from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
wear_analysis = Transition(label='Wear Analysis')
image_capture = Transition(label='Image Capture')
pattern_match = Transition(label='Pattern Match')
ownership_verify = Transition(label='Ownership Verify')
ethics_review = Transition(label='Ethics Review')
carbon_dating = Transition(label='Carbon Dating')
restoration_eval = Transition(label='Restoration Eval')
report_draft = Transition(label='Report Draft')
stakeholder_review = Transition(label='Stakeholder Review')
archive_data = Transition(label='Archive Data')
exhibit_approve = Transition(label='Exhibit Approve')
condition_monitor = Transition(label='Condition Monitor')
final_certification = Transition(label='Final Certification')

# Define silent transitions for loops and XORs
skip = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()

# Define POWL model for the process
root = StrictPartialOrder()

# Provenance Check
root.add_transition(provenance_check)

# Material Scan
root.add_transition(material_scan)

# Wear Analysis
root.add_transition(wear_analysis)

# Image Capture
root.add_transition(image_capture)

# Pattern Match
root.add_transition(pattern_match)

# Ownership Verify
root.add_transition(ownership_verify)

# Ethics Review
root.add_transition(ethics_review)

# Carbon Dating
root.add_transition(carbon_dating)

# Restoration Eval
root.add_transition(restoration_eval)

# Report Draft
root.add_transition(report_draft)

# Stakeholder Review
root.add_transition(stakeholder_review)

# Archive Data
root.add_transition(archive_data)

# Exhibit Approve
root.add_transition(exhibit_approve)

# Condition Monitor
root.add_transition(condition_monitor)

# Final Certification
root.add_transition(final_certification)

# Define dependencies between activities
root.add_edge(provenance_check, material_scan)
root.add_edge(material_scan, wear_analysis)
root.add_edge(wear_analysis, image_capture)
root.add_edge(image_capture, pattern_match)
root.add_edge(pattern_match, ownership_verify)
root.add_edge(ownership_verify, ethics_review)
root.add_edge(ethics_review, carbon_dating)
root.add_edge(carbon_dating, restoration_eval)
root.add_edge(restoration_eval, report_draft)
root.add_edge(report_draft, stakeholder_review)
root.add_edge(stakeholder_review, archive_data)
root.add_edge(archive_data, exhibit_approve)
root.add_edge(exhibit_approve, condition_monitor)
root.add_edge(condition_monitor, final_certification)