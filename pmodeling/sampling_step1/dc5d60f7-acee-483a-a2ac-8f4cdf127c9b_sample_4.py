from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition

# Define the activities
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

# Define the partial order
root = StrictPartialOrder()

# Add the activities to the root
root.nodes = [intake_review, condition_scan, material_test, style_match, provenance_log,
              forger_risk, legal_audit, expert_panel, data_crosscheck, report_draft,
              blockchain_tag, certification, client_feedback, final_approval, release_prep]

# Define the dependencies
root.order.add_edge(intake_review, condition_scan)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(material_test, style_match)
root.order.add_edge(style_match, provenance_log)
root.order.add_edge(provenance_log, forger_risk)
root.order.add_edge(forger_risk, legal_audit)
root.order.add_edge(legal_audit, expert_panel)
root.order.add_edge(expert_panel, data_crosscheck)
root.order.add_edge(data_crosscheck, report_draft)
root.order.add_edge(report_draft, blockchain_tag)
root.order.add_edge(blockchain_tag, certification)
root.order.add_edge(certification, client_feedback)
root.order.add_edge(client_feedback, final_approval)
root.order.add_edge(final_approval, release_prep)

# Print the root to verify the model
print(root)