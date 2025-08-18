from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
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

# Define the partial order and dependencies between the activities
root = StrictPartialOrder(nodes=[
    provenance_check, material_scan, wear_analysis, image_capture, pattern_match,
    ownership_verify, ethics_review, carbon_dating, restoration_eval, report_draft,
    stakeholder_review, archive_data, exhibit_approve, condition_monitor, final_certification
])
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, wear_analysis)
root.order.add_edge(wear_analysis, image_capture)
root.order.add_edge(image_capture, pattern_match)
root.order.add_edge(ownership_verify, ethics_review)
root.order.add_edge(ethics_review, carbon_dating)
root.order.add_edge(carbon_dating, restoration_eval)
root.order.add_edge(restoration_eval, report_draft)
root.order.add_edge(report_draft, stakeholder_review)
root.order.add_edge(stakeholder_review, archive_data)
root.order.add_edge(archive_data, exhibit_approve)
root.order.add_edge(exhibit_approve, condition_monitor)
root.order.add_edge(condition_monitor, final_certification)