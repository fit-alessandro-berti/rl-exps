from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for each activity
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

# Create a partial order model
root = StrictPartialOrder(nodes=[
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
])

# Define dependencies (POWL model)
root.order.add_edge(intake_review, condition_scan)
root.order.add_edge(intake_review, material_test)
root.order.add_edge(intake_review, style_match)
root.order.add_edge(intake_review, provenance_log)
root.order.add_edge(intake_review, forger_risk)
root.order.add_edge(intake_review, legal_audit)
root.order.add_edge(intake_review, expert_panel)
root.order.add_edge(intake_review, data_crosscheck)
root.order.add_edge(intake_review, report_draft)
root.order.add_edge(intake_review, blockchain_tag)
root.order.add_edge(intake_review, certification)
root.order.add_edge(intake_review, client_feedback)
root.order.add_edge(intake_review, final_approval)
root.order.add_edge(intake_review, release_prep)

# Print the root model
print(root)