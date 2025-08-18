import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define the process model
intake_loop = OperatorPOWL(operator=Operator.LOOP, children=[intake_review, condition_scan, material_test, style_match])
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_log, forger_risk, legal_audit, expert_panel])
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_crosscheck, report_draft, blockchain_tag, certification])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_feedback, final_approval, release_prep])

root = StrictPartialOrder(nodes=[intake_loop, provenance_loop, data_loop, feedback_loop])
root.order.add_edge(intake_loop, provenance_loop)
root.order.add_edge(provenance_loop, data_loop)
root.order.add_edge(data_loop, feedback_loop)

print(root)