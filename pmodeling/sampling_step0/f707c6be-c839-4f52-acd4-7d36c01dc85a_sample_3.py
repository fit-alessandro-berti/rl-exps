import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[multi_spectral_scan, condition_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[database_match, provenance_check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[expert_review, historical_query])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[lab_collaboration, imaging_analysis])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[forgery_detection, legal_drafting])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[certification_issue, client_briefing])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[archival_update, artifact_intake])

# Define the POWL model
root = StrictPartialOrder(nodes=[artifact_intake, xor, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(artifact_intake, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, artifact_intake)