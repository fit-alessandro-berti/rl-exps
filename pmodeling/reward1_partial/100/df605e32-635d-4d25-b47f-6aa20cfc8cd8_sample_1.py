import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for end of process
end_transition = SilentTransition()

# Define exclusive choice for Artifact Scan and Ownership Verify
artifact_scan_xor = OperatorPOWL(operator=Operator.XOR, children=[artifact_scan, ownership_verify])

# Define exclusive choice for Legal Review and Stakeholder Notify
legal_review_xor = OperatorPOWL(operator=Operator.XOR, children=[legal_review, stakeholder_notify])

# Define exclusive choice for Recovery Plan and Third-Party Contact
recovery_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[recovery_plan, third_party_contact])

# Define exclusive choice for Negotiation Setup and Secure Transport
negotiation_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[negotiation_setup, secure_transport])

# Define exclusive choice for Condition Inspect and Restoration Begin
condition_inspect_xor = OperatorPOWL(operator=Operator.XOR, children=[condition_inspect, restoration_begin])

# Define exclusive choice for Documentation Log and Heritage Archive
documentation_log_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_log, heritage_archive])

# Define exclusive choice for Final Audit and Process Close
final_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[final_audit, process_close])

# Define the loop for Artifact Scan, Ownership Verify, and Recovery Plan
artifact_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_scan_xor, ownership_verify, recovery_plan_xor])

# Define the loop for Condition Inspect and Restoration Begin
condition_inspect_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_inspect_xor, restoration_begin])

# Define the loop for Documentation Log and Heritage Archive
documentation_log_loop = OperatorPOWL(operator=Operator.LOOP, children=[documentation_log_xor, heritage_archive])

# Define the loop for Final Audit and Process Close
final_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_audit_xor, process_close])

# Define the root model with the loops and exclusive choices
root = StrictPartialOrder(nodes=[artifact_scan_loop, legal_review_xor, recovery_plan_xor, negotiation_setup_xor, secure_transport, condition_inspect_loop, documentation_log_loop, final_audit_loop, end_transition])
root.order.add_edge(artifact_scan_loop, legal_review_xor)
root.order.add_edge(legal_review_xor, recovery_plan_xor)
root.order.add_edge(recovery_plan_xor, negotiation_setup_xor)
root.order.add_edge(negotiation_setup_xor, secure_transport)
root.order.add_edge(secure_transport, condition_inspect_xor)
root.order.add_edge(condition_inspect_xor, restoration_begin)
root.order.add_edge(restoration_begin, documentation_log_xor)
root.order.add_edge(documentation_log_xor, heritage_archive)
root.order.add_edge(heritage_archive, final_audit_xor)
root.order.add_edge(final_audit_xor, process_close)
root.order.add_edge(process_close, end_transition)

# Print the root model
print(root)