import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
initial_review = Transition(label='Initial Review')
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
chemical_test = Transition(label='Chemical Test')
imaging_capture = Transition(label='Imaging Capture')
expert_consult = Transition(label='Expert Consult')
historical_match = Transition(label='Historical Match')
forgery_detect = Transition(label='Forgery Detect')
documentation_verify = Transition(label='Documentation Verify')
cross_border_check = Transition(label='Cross-Border Check')
condition_assess = Transition(label='Condition Assess')
value_estimate = Transition(label='Value Estimate')
report_draft = Transition(label='Report Draft')
report_review = Transition(label='Report Review')
client_approval = Transition(label='Client Approval')
certification_issue = Transition(label='Certification Issue')
archive_record = Transition(label='Archive Record')

# Define the workflow
root = StrictPartialOrder(nodes=[
    initial_review, provenance_check, material_scan, chemical_test, imaging_capture,
    expert_consult, historical_match, forgery_detect, documentation_verify, cross_border_check,
    condition_assess, value_estimate, report_draft, report_review, client_approval, certification_issue,
    archive_record
])

# Define the dependencies
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, chemical_test)
root.order.add_edge(chemical_test, imaging_capture)
root.order.add_edge(imaging_capture, expert_consult)
root.order.add_edge(expert_consult, historical_match)
root.order.add_edge(historical_match, forgery_detect)
root.order.add_edge(forgery_detect, documentation_verify)
root.order.add_edge(documentation_verify, cross_border_check)
root.order.add_edge(cross_border_check, condition_assess)
root.order.add_edge(condition_assess, value_estimate)
root.order.add_edge(value_estimate, report_draft)
root.order.add_edge(report_draft, report_review)
root.order.add_edge(report_review, client_approval)
root.order.add_edge(client_approval, certification_issue)
root.order.add_edge(certification_issue, archive_record)

# Print the workflow
print(root)