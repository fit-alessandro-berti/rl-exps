from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
intake_review = Transition(label='Intake Review')
condition_scan = Transition(label='Condition Scan')
material_test = Transition(label='Material Test')
style_match = Transition(label='Style Match')
provenance_log = Transition(label='Provenance Log')
forger_risk = Transition(label='Forgery Risk')
legal_audit = Transition(label='Legal Audit')
expert_panel = Transition(label='Expert Panel')
data_crosscheck = Transition(label='Data Crosscheck')
report_draft = Transition(label='Report Draft')
blockchain_tag = Transition(label='Blockchain Tag')
certification = Transition(label='Certification')
client_feedback = Transition(label='Client Feedback')
final_approval = Transition(label='Final Approval')
release_prep = Transition(label='Release Prep')

# Define silent transitions
skip_intake = SilentTransition()
skip_condition = SilentTransition()
skip_material = SilentTransition()
skip_style = SilentTransition()
skip_provenance = SilentTransition()
skip_forger = SilentTransition()
skip_legal = SilentTransition()
skip_expert = SilentTransition()
skip_data = SilentTransition()
skip_report = SilentTransition()
skip_blockchain = SilentTransition()
skip_certification = SilentTransition()
skip_feedback = SilentTransition()

# Define process tree
root = StrictPartialOrder(
    nodes=[
        intake_review, 
        condition_scan, 
        material_test, 
        style_match, 
        provenance_log, 
        forger_risk, 
        legal_audit, 
        expert_panel, 
        data_crosscheck, 
        report_draft, 
        blockchain_tag, 
        certification, 
        client_feedback, 
        final_approval, 
        release_prep
    ],
    order=[
        (intake_review, condition_scan),
        (intake_review, material_test),
        (condition_scan, style_match),
        (condition_scan, provenance_log),
        (condition_scan, forger_risk),
        (condition_scan, legal_audit),
        (material_test, style_match),
        (material_test, provenance_log),
        (material_test, forger_risk),
        (material_test, legal_audit),
        (style_match, data_crosscheck),
        (style_match, report_draft),
        (style_match, blockchain_tag),
        (style_match, certification),
        (provenance_log, data_crosscheck),
        (provenance_log, report_draft),
        (provenance_log, blockchain_tag),
        (provenance_log, certification),
        (forger_risk, legal_audit),
        (forger_risk, expert_panel),
        (legal_audit, expert_panel),
        (expert_panel, data_crosscheck),
        (expert_panel, report_draft),
        (expert_panel, blockchain_tag),
        (expert_panel, certification),
        (data_crosscheck, report_draft),
        (data_crosscheck, blockchain_tag),
        (data_crosscheck, certification),
        (report_draft, blockchain_tag),
        (report_draft, certification),
        (blockchain_tag, certification),
        (certification, client_feedback),
        (certification, final_approval),
        (client_feedback, final_approval),
        (final_approval, release_prep)
    ]
)

print(root)