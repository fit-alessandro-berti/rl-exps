import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
intake_review = Transition(label='Intake Review')
condition_scan = Transition(label='Condition Scan')
material_test = Transition(label='Material Test')
style_match = Transition(label='Style Match')
provenance_log = Transition(label='Provenance Log')
forger_risk = Transition(label='Forgery Risk')
legal_audit = Transition(label='Legal Audit')
expert_panel = Transition(label='Expert Panel')
data_crosscheck = Transition(label='Data Crosscheck')
report_draft = Transition(label='Report Draft')
blockchain_tag = Transition(label='Blockchain Tag')
certification = Transition(label='Certification')
client_feedback = Transition(label='Client Feedback')
final_approval = Transition(label='Final Approval')
release_prep = Transition(label='Release Prep')

# Define loops and choices
intake_loop = OperatorPOWL(operator=Operator.LOOP, children=[intake_review, condition_scan, material_test, style_match, provenance_log, forger_risk, legal_audit, expert_panel, data_crosscheck, report_draft, blockchain_tag, certification, client_feedback, final_approval, release_prep])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_feedback, final_approval, release_prep])

# Define XOR (exclusive choice) for legal audit and expert panel
xor = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, expert_panel])

# Define partial order
root = StrictPartialOrder(nodes=[intake_loop, xor, feedback_loop])
root.order.add_edge(intake_loop, xor)
root.order.add_edge(xor, feedback_loop)

print(root)