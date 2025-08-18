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

# Define the workflow
xor = OperatorPOWL(operator=Operator.XOR, children=[forger_risk, legal_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[client_feedback, final_approval])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[release_prep, certification])

root = StrictPartialOrder(nodes=[intake_review, condition_scan, material_test, style_match, provenance_log, xor, xor2, xor3])
root.order.add_edge(intake_review, condition_scan)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(material_test, style_match)
root.order.add_edge(style_match, provenance_log)
root.order.add_edge(provenance_log, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, release_prep)