import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    initial_review,
    provenance_check,
    material_scan,
    chemical_test,
    imaging_capture,
    expert_consult,
    historical_match,
    forgery_detect,
    documentation_verify,
    cross_border_check,
    condition_assess,
    value_estimate,
    report_draft,
    report_review,
    client_approval,
    certification_issue,
    archive_record
])

# Define the order dependencies
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(initial_review, material_scan)
root.order.add_edge(initial_review, chemical_test)
root.order.add_edge(initial_review, imaging_capture)
root.order.add_edge(initial_review, expert_consult)
root.order.add_edge(initial_review, historical_match)
root.order.add_edge(initial_review, forgery_detect)
root.order.add_edge(initial_review, documentation_verify)
root.order.add_edge(initial_review, cross_border_check)
root.order.add_edge(initial_review, condition_assess)
root.order.add_edge(initial_review, value_estimate)
root.order.add_edge(initial_review, report_draft)
root.order.add_edge(initial_review, report_review)
root.order.add_edge(initial_review, client_approval)
root.order.add_edge(initial_review, certification_issue)
root.order.add_edge(initial_review, archive_record)

# Print the root POWL model
print(root)