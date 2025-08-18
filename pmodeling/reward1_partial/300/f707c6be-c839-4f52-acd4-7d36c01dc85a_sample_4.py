import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Constructing the POWL model
root = StrictPartialOrder(
    nodes=[
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
        forgery_detection,
        legal_drafting,
        certification_issue,
        client_briefing,
        archival_update
    ],
    order=[
        (artifact_intake, condition_check),
        (condition_check, multi_spectral_scan),
        (multi_spectral_scan, material_test),
        (material_test, database_match),
        (database_match, provenance_check),
        (provenance_check, expert_review),
        (expert_review, historical_query),
        (historical_query, lab_collaboration),
        (lab_collaboration, imaging_analysis),
        (imaging_analysis, forgery_detection),
        (forgery_detection, legal_drafting),
        (legal_drafting, certification_issue),
        (certification_issue, client_briefing),
        (client_briefing, archival_update)
    ]
)

print(root)