import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
skip = SilentTransition()

# Define the loop for expert consultations
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult])

# Define the exclusive choice between historical match and forgery detection
historical_or_forgery = OperatorPOWL(operator=Operator.XOR, children=[historical_match, forgery_detect])

# Define the exclusive choice between condition assessment and value estimation
condition_or_value = OperatorPOWL(operator=Operator.XOR, children=[condition_assess, value_estimate])

# Define the exclusive choice between documentation verification and cross-border check
documentation_or_cross_border = OperatorPOWL(operator=Operator.XOR, children=[documentation_verify, cross_border_check])

# Define the exclusive choice between imaging capture and chemical test
imaging_or_chemical = OperatorPOWL(operator=Operator.XOR, children=[imaging_capture, chemical_test])

# Define the exclusive choice between material scan and provenance check
material_or_provenance = OperatorPOWL(operator=Operator.XOR, children=[material_scan, provenance_check])

# Define the exclusive choice between initial review and expert loop
initial_or_expert = OperatorPOWL(operator=Operator.XOR, children=[initial_review, expert_loop])

# Define the exclusive choice between report draft and report review
draft_or_review = OperatorPOWL(operator=Operator.XOR, children=[report_draft, report_review])

# Define the exclusive choice between client approval and certification issue
approval_or_issue = OperatorPOWL(operator=Operator.XOR, children=[client_approval, certification_issue])

# Define the exclusive choice between archive record and final decision
archive_or_final = OperatorPOWL(operator=Operator.XOR, children=[archive_record, approval_or_issue])

# Define the final decision
final_decision = OperatorPOWL(operator=Operator.XOR, children=[archive_or_final, report_draft])

# Define the final workflow
root = StrictPartialOrder(nodes=[initial_or_expert, imaging_or_chemical, material_or_provenance, documentation_or_cross_border, condition_or_value, historical_or_forgery, expert_loop, report_draft, report_review, client_approval, certification_issue, archive_record, approval_or_issue, archive_or_final, final_decision])

# Add dependencies
root.order.add_edge(initial_or_expert, imaging_or_chemical)
root.order.add_edge(imaging_or_chemical, material_or_provenance)
root.order.add_edge(material_or_provenance, documentation_or_cross_border)
root.order.add_edge(documentation_or_cross_border, condition_or_value)
root.order.add_edge(condition_or_value, historical_or_forgery)
root.order.add_edge(historical_or_forgery, expert_loop)
root.order.add_edge(expert_loop, report_draft)
root.order.add_edge(report_draft, report_review)
root.order.add_edge(report_review, client_approval)
root.order.add_edge(client_approval, certification_issue)
root.order.add_edge(certification_issue, archive_record)
root.order.add_edge(archive_record, approval_or_issue)
root.order.add_edge(approval_or_issue, archive_or_final)
root.order.add_edge(archive_or_final, final_decision)

# Print the root model
print(root)