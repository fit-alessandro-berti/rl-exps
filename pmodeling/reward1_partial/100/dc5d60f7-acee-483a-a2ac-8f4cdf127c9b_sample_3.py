import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
intake_review = Transition(label='Intake Review')
condition_scan = Transition(label='Condition Scan')
material_test = Transition(label='Material Test')
style_match = Transition(label='Style Match')
provenance_log = Transition(label='Provenance Log')
forgery_risk = Transition(label='Forgery Risk')
legal_audit = Transition(label='Legal Audit')
expert_panel = Transition(label='Expert Panel')
data_crosscheck = Transition(label='Data Crosscheck')
report_draft = Transition(label='Report Draft')
blockchain_tag = Transition(label='Blockchain Tag')
certification = Transition(label='Certification')
client_feedback = Transition(label='Client Feedback')
final_approval = Transition(label='Final Approval')
release_prep = Transition(label='Release Prep')

# Define the silent transitions (empty labels)
skip = SilentTransition()

# Define the partial order nodes and their dependencies
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[forgery_risk, legal_audit, expert_panel, data_crosscheck, report_draft, blockchain_tag, certification, client_feedback, final_approval, release_prep])
xor_node = OperatorPOWL(operator=Operator.XOR, children=[intake_review, condition_scan, material_test, style_match, provenance_log])

# Define the root node
root = StrictPartialOrder(nodes=[loop_node, xor_node])

# Add the dependencies between nodes
root.order.add_edge(xor_node, loop_node)

# Print the root node to see the model
print(root)