from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Artifact_Scan = Transition(label='Artifact Scan')
Ownership_Verify = Transition(label='Ownership Verify')
Risk_Assess = Transition(label='Risk Assess')
Legal_Review = Transition(label='Legal Review')
Stakeholder_Notify = Transition(label='Stakeholder Notify')
Recovery_Plan = Transition(label='Recovery Plan')
Third_Party_Contact = Transition(label='Third-Party Contact')
Negotiation_Setup = Transition(label='Negotiation Setup')
Secure_Transport = Transition(label='Secure Transport')
Condition_Inspect = Transition(label='Condition Inspect')
Restoration_Begin = Transition(label='Restoration Begin')
Documentation_Log = Transition(label='Documentation Log')
Heritage_Archive = Transition(label='Heritage Archive')
Final_Audit = Transition(label='Final Audit')
Process_Close = Transition(label='Process Close')

# Define transitions
skip = SilentTransition()

# Define POWL model
loop_artifact_scan = OperatorPOWL(operator=Operator.LOOP, children=[Artifact_Scan, Ownership_Verify])
xor_risk_assess = OperatorPOWL(operator=Operator.XOR, children=[Risk_Assess, skip])
xor_legal_review = OperatorPOWL(operator=Operator.XOR, children=[Legal_Review, skip])
xor_stakeholder_notify = OperatorPOWL(operator=Operator.XOR, children=[Stakeholder_Notify, skip])
xor_recovery_plan = OperatorPOWL(operator=Operator.XOR, children=[Recovery_Plan, skip])
xor_third_party_contact = OperatorPOWL(operator=Operator.XOR, children=[Third_Party_Contact, skip])
xor_negotiation_setup = OperatorPOWL(operator=Operator.XOR, children=[Negotiation_Setup, skip])
xor_secure_transport = OperatorPOWL(operator=Operator.XOR, children=[Secure_Transport, skip])
xor_condition_inspect = OperatorPOWL(operator=Operator.XOR, children=[Condition_Inspect, skip])
xor_restoration_begin = OperatorPOWL(operator=Operator.XOR, children=[Restoration_Begin, skip])
xor_documentation_log = OperatorPOWL(operator=Operator.XOR, children=[Documentation_Log, skip])
xor_heritage_archive = OperatorPOWL(operator=Operator.XOR, children=[Heritage_Archive, skip])
xor_final_audit = OperatorPOWL(operator=Operator.XOR, children=[Final_Audit, skip])
xor_process_close = OperatorPOWL(operator=Operator.XOR, children=[Process_Close, skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[
    loop_artifact_scan,
    xor_risk_assess,
    xor_legal_review,
    xor_stakeholder_notify,
    xor_recovery_plan,
    xor_third_party_contact,
    xor_negotiation_setup,
    xor_secure_transport,
    xor_condition_inspect,
    xor_restoration_begin,
    xor_documentation_log,
    xor_heritage_archive,
    xor_final_audit,
    xor_process_close
])

# Add dependencies
root.order.add_edge(loop_artifact_scan, xor_risk_assess)
root.order.add_edge(xor_risk_assess, xor_legal_review)
root.order.add_edge(xor_legal_review, xor_stakeholder_notify)
root.order.add_edge(xor_stakeholder_notify, xor_recovery_plan)
root.order.add_edge(xor_recovery_plan, xor_third_party_contact)
root.order.add_edge(xor_third_party_contact, xor_negotiation_setup)
root.order.add_edge(xor_negotiation_setup, xor_secure_transport)
root.order.add_edge(xor_secure_transport, xor_condition_inspect)
root.order.add_edge(xor_condition_inspect, xor_restoration_begin)
root.order.add_edge(xor_restoration_begin, xor_documentation_log)
root.order.add_edge(xor_documentation_log, xor_heritage_archive)
root.order.add_edge(xor_heritage_archive, xor_final_audit)
root.order.add_edge(xor_final_audit, xor_process_close)

print(root)