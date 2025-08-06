import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice for risk assessment
risk_choice = OperatorPOWL(operator=Operator.XOR, children=[forger_risk, legal_audit])

# Define the exclusive choice for expert panel
expert_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, data_crosscheck])

# Define the loop for data crosscheck
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_crosscheck, report_draft])

# Define the loop for expert panel
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_panel, data_loop])

# Define the exclusive choice for expert panel and final approval
final_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_loop, final_approval])

# Define the exclusive choice for blockchain tag and release prep
release_choice = OperatorPOWL(operator=Operator.XOR, children=[blockchain_tag, release_prep])

# Define the root POWL model
root = StrictPartialOrder(nodes=[intake_review, condition_scan, material_test, style_match, provenance_log, risk_choice, expert_choice, final_choice, release_choice])
root.order.add_edge(intake_review, condition_scan)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(material_test, style_match)
root.order.add_edge(style_match, provenance_log)
root.order.add_edge(provenance_log, risk_choice)
root.order.add_edge(risk_choice, expert_choice)
root.order.add_edge(expert_choice, final_choice)
root.order.add_edge(final_choice, release_choice)
root.order.add_edge(release_choice, release_prep)