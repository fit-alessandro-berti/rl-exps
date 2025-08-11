import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loops
condition_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_scan])
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test])
style_loop = OperatorPOWL(operator=Operator.LOOP, children=[style_match])
forger_loop = OperatorPOWL(operator=Operator.LOOP, children=[forger_risk])
legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_audit])
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_panel])
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_crosscheck])
report_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_draft])
blockchain_loop = OperatorPOWL(operator=Operator.LOOP, children=[blockchain_tag])
certification_loop = OperatorPOWL(operator=Operator.LOOP, children=[certification])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_feedback])
approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_approval])
release_loop = OperatorPOWL(operator=Operator.LOOP, children=[release_prep])

# Define the exclusive choices
condition_xor = OperatorPOWL(operator=Operator.XOR, children=[intake_review, condition_loop])
material_xor = OperatorPOWL(operator=Operator.XOR, children=[condition_loop, material_loop])
style_xor = OperatorPOWL(operator=Operator.XOR, children=[material_loop, style_loop])
forger_xor = OperatorPOWL(operator=Operator.XOR, children=[style_loop, forger_loop])
legal_xor = OperatorPOWL(operator=Operator.XOR, children=[forger_loop, legal_loop])
expert_xor = OperatorPOWL(operator=Operator.XOR, children=[legal_loop, expert_loop])
data_xor = OperatorPOWL(operator=Operator.XOR, children=[expert_loop, data_loop])
report_xor = OperatorPOWL(operator=Operator.XOR, children=[data_loop, report_loop])
blockchain_xor = OperatorPOWL(operator=Operator.XOR, children=[report_loop, blockchain_loop])
certification_xor = OperatorPOWL(operator=Operator.XOR, children=[blockchain_loop, certification_loop])
feedback_xor = OperatorPOWL(operator=Operator.XOR, children=[certification_loop, feedback_loop])
approval_xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, approval_loop])
release_xor = OperatorPOWL(operator=Operator.XOR, children=[approval_loop, release_loop])

# Define the root POWL model
root = StrictPartialOrder(nodes=[condition_xor, material_xor, style_xor, forger_xor, legal_xor, expert_xor, data_xor, report_xor, blockchain_xor, certification_xor, feedback_xor, approval_xor, release_xor])
root.order.add_edge(condition_xor, material_xor)
root.order.add_edge(material_xor, style_xor)
root.order.add_edge(style_xor, forger_xor)
root.order.add_edge(forger_xor, legal_xor)
root.order.add_edge(legal_xor, expert_xor)
root.order.add_edge(expert_xor, data_xor)
root.order.add_edge(data_xor, report_xor)
root.order.add_edge(report_xor, blockchain_xor)
root.order.add_edge(blockchain_xor, certification_xor)
root.order.add_edge(certification_xor, feedback_xor)
root.order.add_edge(feedback_xor, approval_xor)
root.order.add_edge(approval_xor, release_xor)

# Print the root POWL model
print(root)