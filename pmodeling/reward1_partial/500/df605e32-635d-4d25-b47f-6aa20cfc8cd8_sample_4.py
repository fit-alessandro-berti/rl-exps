import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

artifact_scan_order = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, skip])
risk_assess_order = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, skip])
legal_review_order = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
stakeholder_notify_order = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_notify, skip])
recovery_plan_order = OperatorPOWL(operator=Operator.XOR, children=[recovery_plan, skip])
third_party_contact_order = OperatorPOWL(operator=Operator.XOR, children=[third_party_contact, skip])
negotiation_setup_order = OperatorPOWL(operator=Operator.XOR, children=[negotiation_setup, skip])
secure_transport_order = OperatorPOWL(operator=Operator.XOR, children=[secure_transport, skip])
condition_inspect_order = OperatorPOWL(operator=Operator.XOR, children=[condition_inspect, skip])
restoration_begin_order = OperatorPOWL(operator=Operator.XOR, children=[restoration_begin, skip])
documentation_log_order = OperatorPOWL(operator=Operator.XOR, children=[documentation_log, skip])
heritage_archive_order = OperatorPOWL(operator=Operator.XOR, children=[heritage_archive, skip])
final_audit_order = OperatorPOWL(operator=Operator.XOR, children=[final_audit, skip])
process_close_order = OperatorPOWL(operator=Operator.XOR, children=[process_close, skip])

root = StrictPartialOrder(nodes=[
    artifact_scan,
    artifact_scan_order,
    risk_assess_order,
    legal_review_order,
    stakeholder_notify_order,
    recovery_plan_order,
    third_party_contact_order,
    negotiation_setup_order,
    secure_transport_order,
    condition_inspect_order,
    restoration_begin_order,
    documentation_log_order,
    heritage_archive_order,
    final_audit_order,
    process_close_order
])

root.order.add_edge(artifact_scan, artifact_scan_order)
root.order.add_edge(artifact_scan, risk_assess_order)
root.order.add_edge(artifact_scan, legal_review_order)
root.order.add_edge(artifact_scan, stakeholder_notify_order)
root.order.add_edge(artifact_scan, recovery_plan_order)
root.order.add_edge(artifact_scan, third_party_contact_order)
root.order.add_edge(artifact_scan, negotiation_setup_order)
root.order.add_edge(artifact_scan, secure_transport_order)
root.order.add_edge(artifact_scan, condition_inspect_order)
root.order.add_edge(artifact_scan, restoration_begin_order)
root.order.add_edge(artifact_scan, documentation_log_order)
root.order.add_edge(artifact_scan, heritage_archive_order)
root.order.add_edge(artifact_scan, final_audit_order)
root.order.add_edge(artifact_scan, process_close_order)