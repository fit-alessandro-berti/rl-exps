from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
multi_spectral_scan = Transition(label='Multi-spectral Scan')
material_test = Transition(label='Material Test')
database_match = Transition(label='Database Match')
provenance_check = Transition(label='Provenance Check')
expert_review = Transition(label='Expert Review')
historical_query = Transition(label='Historical Query')
lab_collaboration = Transition(label='Lab Collaboration')
imaging_analysis = Transition(label='Imaging Analysis')
forgery_detection = Transition(label='Forgery Detection')
legal_drafting = Transition(label='Legal Drafting')
certification_issue = Transition(label='Certification Issue')
client_briefing = Transition(label='Client Briefing')
archival_update = Transition(label='Archival Update')

# Define the loop and choice structures
artifact_authentication = OperatorPOWL(operator=Operator.LOOP, children=[
    artifact_intake, condition_check, multi_spectral_scan, material_test, database_match, provenance_check, expert_review, historical_query, lab_collaboration, imaging_analysis, forgery_detection, legal_drafting, certification_issue, client_briefing, archival_update
])

root = StrictPartialOrder(nodes=[artifact_authentication])
root.order.add_edge(artifact_authentication, artifact_authentication)

print(root)