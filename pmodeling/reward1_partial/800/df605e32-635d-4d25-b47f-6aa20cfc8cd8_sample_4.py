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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        # Artifact Scan
        (artifact_scan, ownership_verify),
        (artifact_scan, risk_assess),
        # Ownership Verify
        (ownership_verify, legal_review),
        (ownership_verify, stakeholder_notify),
        # Legal Review
        (legal_review, recovery_plan),
        (legal_review, stakeholder_notify),
        # Stakeholder Notify
        (stakeholder_notify, recovery_plan),
        (stakeholder_notify, third_party_contact),
        # Recovery Plan
        (recovery_plan, secure_transport),
        (recovery_plan, stakeholder_notify),
        # Third-Party Contact
        (third_party_contact, negotiation_setup),
        (third_party_contact, stakeholder_notify),
        # Negotiation Setup
        (negotiation_setup, secure_transport),
        (negotiation_setup, stakeholder_notify),
        # Secure Transport
        (secure_transport, condition_inspect),
        (secure_transport, stakeholder_notify),
        # Condition Inspect
        (condition_inspect, restoration_begin),
        (condition_inspect, stakeholder_notify),
        # Restoration Begin
        (restoration_begin, documentation_log),
        (restoration_begin, stakeholder_notify),
        # Documentation Log
        (documentation_log, heritage_archive),
        (documentation_log, stakeholder_notify),
        # Heritage Archive
        (heritage_archive, final_audit),
        (heritage_archive, stakeholder_notify),
        # Final Audit
        (final_audit, process_close),
        (final_audit, stakeholder_notify),
        # Process Close
        (process_close, stakeholder_notify)
    ]
)