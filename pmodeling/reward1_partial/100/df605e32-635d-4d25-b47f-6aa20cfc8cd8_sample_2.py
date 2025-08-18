import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the operators
xor = OperatorPOWL(operator=Operator.XOR, children=[legal_review, stakeholder_notify])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[recovery_plan, third_party_contact])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[negotiation_setup, secure_transport])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[condition_inspect, documentation_log])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[restoration_begin, heritage_archive])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[final_audit, process_close])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor, xor2, xor3, xor4, xor5, xor6])

# Define the root
root = StrictPartialOrder(nodes=[artifact_scan, ownership_verify, risk_assess, loop])
root.order.add_edge(artifact_scan, ownership_verify)
root.order.add_edge(ownership_verify, risk_assess)
root.order.add_edge(risk_assess, loop)

# Print the root
print(root)