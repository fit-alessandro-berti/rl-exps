import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop and XOR nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[multi_spectral_scan, material_test])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[database_match, provenance_check])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[expert_review, historical_query])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[lab_collaboration, imaging_analysis])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[forgeries_detection, legal_drafting])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[certification_issue, client_briefing])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[archival_update, client_briefing])

# Define the root node
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, loop1, loop2, xor1, xor2, xor3, xor4, xor5])

# Define the edges
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, client_briefing)

print(root)