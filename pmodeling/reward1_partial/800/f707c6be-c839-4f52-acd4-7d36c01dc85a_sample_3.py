import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define each activity as a Transition object
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
forger_detection = Transition(label='Forgery Detection')
legal_drafting = Transition(label='Legal Drafting')
certification_issue = Transition(label='Certification Issue')
client_briefing = Transition(label='Client Briefing')
archival_update = Transition(label='Archival Update')

# Create the exclusive choice (XOR) for some activities
xor = OperatorPOWL(operator=Operator.XOR, children=[database_match, provenance_check, expert_review, historical_query, lab_collaboration, imaging_analysis, forger_detection])

# Create the loop for the multi-spectral scan and material test
loop = OperatorPOWL(operator=Operator.LOOP, children=[multi_spectral_scan, material_test])

# Define the partial order by creating a StrictPartialOrder and adding edges
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, loop, xor, legal_drafting, certification_issue, client_briefing, archival_update])
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, legal_drafting)
root.order.add_edge(legal_drafting, certification_issue)
root.order.add_edge(certification_issue, client_briefing)
root.order.add_edge(client_briefing, archival_update)

print(root)