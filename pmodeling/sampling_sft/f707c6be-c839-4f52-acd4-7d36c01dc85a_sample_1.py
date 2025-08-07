import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
artifact_intake     = Transition(label='Artifact Intake')
condition_check     = Transition(label='Condition Check')
multi_spectral_scan = Transition(label='Multi-spectral Scan')
material_test       = Transition(label='Material Test')
database_match      = Transition(label='Database Match')
provenance_check    = Transition(label='Provenance Check')
expert_review       = Transition(label='Expert Review')
historical_query    = Transition(label='Historical Query')
lab_collaboration   = Transition(label='Lab Collaboration')
imaging_analysis    = Transition(label='Imaging Analysis')
forgery_detection   = Transition(label='Forgery Detection')
legal_drafting      = Transition(label='Legal Drafting')
certification_issue = Transition(label='Certification Issue')
client_briefing     = Transition(label='Client Briefing')
archival_update     = Transition(label='Archival Update')

# Define the forensic analysis branch
forensic_branch = StrictPartialOrder(nodes=[
    multi_spectral_scan, material_test,
    database_match, provenance_check,
    expert_review, historical_query,
    lab_collaboration, imaging_analysis,
    forgery_detection
])
forensic_branch.order.add_edge(multi_spectral_scan, material_test)
forensic_branch.order.add_edge(material_test, database_match)
forensic_branch.order.add_edge(material_test, provenance_check)
forensic_branch.order.add_edge(database_match, expert_review)
forensic_branch.order.add_edge(provenance_check, expert_review)
forensic_branch.order.add_edge(expert_review, historical_query)
forensic_branch.order.add_edge(historical_query, lab_collaboration)
forensic_branch.order.add_edge(lab_collaboration, imaging_analysis)
forensic_branch.order.add_edge(imaging_analysis, forgery_detection)

# Define the documentation and legal branch
legal_branch = StrictPartialOrder(nodes=[
    legal_drafting, certification_issue, client_briefing
])
legal_branch.order.add_edge(legal_drafting, certification_issue)
legal_branch.order.add_edge(certification_issue, client_briefing)

# Define the archival update
archival_update = Transition(label='Archival Update')

# Define the overall process as a choice between forensic and archival branches
root = OperatorPOWL(operator=Operator.XOR, children=[forensic_branch, archival_update])

# Connect the intake and condition check to the main process
root.order.add_edge(artifact_intake, root)
root.order.add_edge(condition_check, root)

# Finalize the process with legal briefing and archival update
root.order.add_edge(root, legal_branch)
root.order.add_edge(root, archival_update)

# Finalize the archival update with the archival update transition
root.order.add_edge(archival_update, archival_update)

# Print the root model for verification
print(root)