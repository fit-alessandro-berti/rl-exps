import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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
skip = SilentTransition()

# Define the POWL model structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[intake_review, condition_scan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[material_test, style_match])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_log, forger_risk])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[legal_audit, expert_panel])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[data_crosscheck, report_draft])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[blockchain_tag, certification])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[client_feedback, final_approval])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[release_prep, skip])

# Define the POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])

# Define the POWL model dependencies
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop2, loop4)
root.order.add_edge(loop2, loop5)
root.order.add_edge(loop3, loop6)
root.order.add_edge(loop3, loop7)
root.order.add_edge(loop4, loop8)
root.order.add_edge(loop5, loop8)
root.order.add_edge(loop6, loop8)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, loop8)

# Print the POWL model
print(root)