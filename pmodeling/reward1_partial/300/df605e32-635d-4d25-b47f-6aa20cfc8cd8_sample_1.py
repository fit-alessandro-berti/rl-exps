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

# Define silent transitions
skip = SilentTransition()

# Define loops and exclusive choices
artifact_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_scan, ownership_verify])
risk_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, legal_review])
stakeholder_notify_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_notify, recovery_plan])
third_party_contact_loop = OperatorPOWL(operator=Operator.LOOP, children=[third_party_contact, negotiation_setup])
secure_transport_loop = OperatorPOWL(operator=Operator.LOOP, children=[secure_transport, condition_inspect])
restoration_begin_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_begin, documentation_log])

# Define the root node with the defined transitions and loops
root = StrictPartialOrder(nodes=[
    artifact_scan_loop,
    risk_assess_loop,
    stakeholder_notify_loop,
    third_party_contact_loop,
    secure_transport_loop,
    restoration_begin_loop,
    heritage_archive,
    final_audit,
    process_close
])

# Add dependencies between nodes
root.order.add_edge(artifact_scan_loop, risk_assess_loop)
root.order.add_edge(risk_assess_loop, stakeholder_notify_loop)
root.order.add_edge(stakeholder_notify_loop, third_party_contact_loop)
root.order.add_edge(third_party_contact_loop, secure_transport_loop)
root.order.add_edge(secure_transport_loop, restoration_begin_loop)
root.order.add_edge(restoration_begin_loop, heritage_archive)
root.order.add_edge(heritage_archive, final_audit)
root.order.add_edge(final_audit, process_close)

print(root)