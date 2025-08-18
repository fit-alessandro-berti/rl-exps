from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the POWL model
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

# Define the control-flow operators for the POWL model
xor_forger_risk = OperatorPOWL(operator=Operator.XOR, children=[forger_risk, SilentTransition()])
xor_legal_audit = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, SilentTransition()])
xor_data_crosscheck = OperatorPOWL(operator=Operator.XOR, children=[data_crosscheck, SilentTransition()])
xor_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[client_feedback, SilentTransition()])
xor_final_approval = OperatorPOWL(operator=Operator.XOR, children=[final_approval, SilentTransition()])
xor_release_prep = OperatorPOWL(operator=Operator.XOR, children=[release_prep, SilentTransition()])
xor_blockchain_tag = OperatorPOWL(operator=Operator.XOR, children=[blockchain_tag, SilentTransition()])
xor_certification = OperatorPOWL(operator=Operator.XOR, children=[certification, SilentTransition()])

# Define the partial order for the POWL model
root = StrictPartialOrder(nodes=[
    intake_review, 
    condition_scan, 
    material_test, 
    style_match, 
    provenance_log, 
    xor_forger_risk, 
    xor_legal_audit, 
    xor_data_crosscheck, 
    xor_client_feedback, 
    xor_final_approval, 
    xor_release_prep, 
    xor_blockchain_tag, 
    xor_certification
])

# Define the dependencies between nodes
root.order.add_edge(intake_review, condition_scan)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(material_test, style_match)
root.order.add_edge(style_match, provenance_log)
root.order.add_edge(provenance_log, xor_forger_risk)
root.order.add_edge(xor_forger_risk, xor_legal_audit)
root.order.add_edge(xor_legal_audit, xor_data_crosscheck)
root.order.add_edge(xor_data_crosscheck, xor_client_feedback)
root.order.add_edge(xor_client_feedback, xor_final_approval)
root.order.add_edge(xor_final_approval, xor_release_prep)
root.order.add_edge(xor_release_prep, xor_blockchain_tag)
root.order.add_edge(xor_blockchain_tag, xor_certification)

# Print the POWL model
print(root)