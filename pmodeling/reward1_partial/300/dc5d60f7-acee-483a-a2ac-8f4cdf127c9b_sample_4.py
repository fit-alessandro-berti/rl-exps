from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the activities
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

# Define the loop for the expert panel
expert_panel_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_panel])

# Define the XOR node for the data crosscheck and expert panel
xor_data_crosscheck = OperatorPOWL(operator=Operator.XOR, children=[data_crosscheck, expert_panel_loop])

# Define the XOR node for the final approval and release preparation
xor_final_approval = OperatorPOWL(operator=Operator.XOR, children=[final_approval, release_prep])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[intake_review, condition_scan, material_test, style_match, provenance_log, forger_risk, legal_audit, xor_data_crosscheck, xor_final_approval])
root.order.add_edge(intake_review, condition_scan)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(material_test, style_match)
root.order.add_edge(style_match, provenance_log)
root.order.add_edge(provenance_log, forger_risk)
root.order.add_edge(forger_risk, legal_audit)
root.order.add_edge(legal_audit, xor_data_crosscheck)
root.order.add_edge(xor_data_crosscheck, xor_final_approval)
root.order.add_edge(xor_final_approval, final_approval)
root.order.add_edge(final_approval, release_prep)

# Print the root POWL model
print(root)