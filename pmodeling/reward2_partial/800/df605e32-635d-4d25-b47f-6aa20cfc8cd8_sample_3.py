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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    artifact_scan,
    ownership_verify,
    risk_assess,
    legal_review,
    stakeholder_notify,
    recovery_plan,
    third_party_contact,
    negotiation_setup,
    secure_transport,
    condition_inspect,
    restoration_begin,
    documentation_log,
    heritage_archive,
    final_audit,
    process_close
])

# Define the order of activities
root.order.add_edge(artifact_scan, ownership_verify)
root.order.add_edge(ownership_verify, risk_assess)
root.order.add_edge(risk_assess, legal_review)
root.order.add_edge(legal_review, stakeholder_notify)
root.order.add_edge(stakeholder_notify, recovery_plan)
root.order.add_edge(recovery_plan, third_party_contact)
root.order.add_edge(third_party_contact, negotiation_setup)
root.order.add_edge(negotiation_setup, secure_transport)
root.order.add_edge(secure_transport, condition_inspect)
root.order.add_edge(condition_inspect, restoration_begin)
root.order.add_edge(restoration_begin, documentation_log)
root.order.add_edge(documentation_log, heritage_archive)
root.order.add_edge(heritage_archive, final_audit)
root.order.add_edge(final_audit, process_close)

# Print the POWL model
print(root)