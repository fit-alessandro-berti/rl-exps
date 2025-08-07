import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
initial_review     = Transition(label='Initial Review')
provenance_check   = Transition(label='Provenance Check')
material_scan      = Transition(label='Material Scan')
chemical_test      = Transition(label='Chemical Test')
imaging_capture    = Transition(label='Imaging Capture')
historical_match   = Transition(label='Historical Match')
expert_consult     = Transition(label='Expert Consult')
forgery_detect     = Transition(label='Forgery Detect')
documentation_verify= Transition(label='Documentation Verify')
cross_border_check = Transition(label='Cross-Border Check')
condition_assess   = Transition(label='Condition Assess')
value_estimate     = Transition(label='Value Estimate')
report_draft       = Transition(label='Report Draft')
report_review      = Transition(label='Report Review')
client_approval    = Transition(label='Client Approval')
certification_issue= Transition(label='Certification Issue')
archive_record     = Transition(label='Archive Record')

# Define the cross‐border loop: capture, verify, repeat or exit
cross_border_body = StrictPartialOrder(nodes=[imaging_capture, documentation_verify])
cross_border_loop = OperatorPOWL(operator=Operator.LOOP, children=[cross_border_body, cross_border_check])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    initial_review,
    provenance_check,
    material_scan,
    chemical_test,
    cross_border_loop,
    historical_match,
    expert_consult,
    forgery_detect,
    condition_assess,
    value_estimate,
    report_draft,
    report_review,
    client_approval,
    certification_issue,
    archive_record
])

# Add dependencies
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, chemical_test)
root.order.add_edge(chemical_test, cross_border_loop)
root.order.add_edge(cross_border_loop, historical_match)
root.order.add_edge(historical_match, expert_consult)
root.order.add_edge(expert_consult, forgery_detect)
root.order.add_edge(forgery_detect, condition_assess)
root.order.add_edge(condition_assess, value_estimate)
root.order.add_edge(value_estimate, report_draft)
root.order.add_edge(report_draft, report_review)
root.order.add_edge(report_review, client_approval)
root.order.add_edge(client_approval, certification_issue)
root.order.add_edge(certification_issue, archive_record)