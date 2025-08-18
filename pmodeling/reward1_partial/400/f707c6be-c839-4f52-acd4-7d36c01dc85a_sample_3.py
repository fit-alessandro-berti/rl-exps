import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names
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
forgeries_detection = Transition(label='Forgery Detection')
legal_drafting = Transition(label='Legal Drafting')
certification_issue = Transition(label='Certification Issue')
client_briefing = Transition(label='Client Briefing')
archival_update = Transition(label='Archival Update')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    artifact_intake,
    condition_check,
    multi_spectral_scan,
    material_test,
    database_match,
    provenance_check,
    expert_review,
    historical_query,
    lab_collaboration,
    imaging_analysis,
    forgeries_detection,
    legal_drafting,
    certification_issue,
    client_briefing,
    archival_update
])

# Define the order dependencies (partial order)
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, multi_spectral_scan)
root.order.add_edge(multi_spectral_scan, material_test)
root.order.add_edge(material_test, database_match)
root.order.add_edge(database_match, provenance_check)
root.order.add_edge(provenance_check, expert_review)
root.order.add_edge(expert_review, historical_query)
root.order.add_edge(historical_query, lab_collaboration)
root.order.add_edge(lab_collaboration, imaging_analysis)
root.order.add_edge(imaging_analysis, forgeries_detection)
root.order.add_edge(forgeries_detection, legal_drafting)
root.order.add_edge(legal_drafting, certification_issue)
root.order.add_edge(certification_issue, client_briefing)
root.order.add_edge(client_briefing, archival_update)

print(root)