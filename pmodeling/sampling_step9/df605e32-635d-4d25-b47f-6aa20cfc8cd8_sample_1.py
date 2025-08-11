import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define silent transitions
skip = SilentTransition()

# Define the loop and XOR nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_scan, ownership_verify])
xor = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, legal_review, stakeholder_notify, recovery_plan, third_party_contact, negotiation_setup, secure_transport, condition_inspect, documentation_log, heritage_archive, final_audit, process_close])

# Define the root
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root
print(root)