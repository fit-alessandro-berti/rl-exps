import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, legal_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_notify, recovery_plan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[third_party_contact, negotiation_setup])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[secure_transport, condition_inspect])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[restoration_begin, documentation_log])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[heritage_archive, final_audit])

loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_scan, ownership_verify])

root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)

print(root)