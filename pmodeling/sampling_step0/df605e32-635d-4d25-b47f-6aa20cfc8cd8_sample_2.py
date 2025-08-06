import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
artifact_scan = Transition(label='Artifact Scan')
ownership_verify = Transition(label='Ownership Verify')
risk_assess = Transition(label='Risk Assess')
legal_review = Transition(label='Legal Review')
stakeholder_notify = Transition(label='Stakeholder Notify')
recovery_plan = Transition(label='Recovery Plan')
third_party_contact = Transition(label='Third-Party Contact')
negotiation_setup = Transition(label='Negotiation Setup')
secure_transport = Transition(label='Secure Transport')
condition_inspect = Transition(label='Condition Inspect')
restoration_begin = Transition(label='Restoration Begin')
documentation_log = Transition(label='Documentation Log')
heritage_archive = Transition(label='Heritage Archive')
final_audit = Transition(label='Final Audit')
process_close = Transition(label='Process Close')

# Define the control flow operators
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[artifact_scan, ownership_verify])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, legal_review])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_notify, recovery_plan])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[third_party_contact, negotiation_setup])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[secure_transport, condition_inspect])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[restoration_begin, documentation_log])
xor_7 = OperatorPOWL(operator=Operator.XOR, children=[heritage_archive, final_audit])
xor_8 = OperatorPOWL(operator=Operator.XOR, children=[process_close, artifact_scan])

# Define the partial order
root = StrictPartialOrder(nodes=[xor_1, xor_2, xor_3, xor_4, xor_5, xor_6, xor_7, xor_8])
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, xor_4)
root.order.add_edge(xor_4, xor_5)
root.order.add_edge(xor_5, xor_6)
root.order.add_edge(xor_6, xor_7)
root.order.add_edge(xor_7, xor_8)

# Print the POWL model
print(root)