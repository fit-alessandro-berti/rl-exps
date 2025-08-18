import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the control flow elements
xor1 = OperatorPOWL(operator=Operator.XOR, children=[forger_risk, legal_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[style_match, expert_panel])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[data_crosscheck, report_draft])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[blockchain_tag, certification])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[client_feedback, final_approval])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[release_prep])
root = StrictPartialOrder(nodes=[intake_review, condition_scan, material_test, xor1, xor2, xor3, xor4, xor5, loop1])

# Define the partial order dependencies
root.order.add_edge(intake_review, condition_scan)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(material_test, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, loop1)
root.order.add_edge(loop1, xor1)

print(root)