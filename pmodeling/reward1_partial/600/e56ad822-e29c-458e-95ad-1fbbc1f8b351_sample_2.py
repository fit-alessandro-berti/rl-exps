import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
submit_artifact = Transition(label='Submit Artifact')
initial_review = Transition(label='Initial Review')
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
context_analysis = Transition(label='Context Analysis')
expert_panel = Transition(label='Expert Panel')
digital_fingerprint = Transition(label='Digital Fingerprint')
ai_pattern = Transition(label='AI Pattern')
legal_audit = Transition(label='Legal Audit')
ethics_review = Transition(label='Ethics Review')
fraud_detection = Transition(label='Fraud Detection')
blockchain_log = Transition(label='Blockchain Log')
certification = Transition(label='Certification')
owner_notify = Transition(label='Owner Notify')
archive_data = Transition(label='Archive Data')
secure_storage = Transition(label='Secure Storage')

# Define nodes and edges
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, ethics_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[fraud_detection, blockchain_log])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[certification, archive_data])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[owner_notify, secure_storage])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, context_analysis, expert_panel, digital_fingerprint, ai_pattern])
root = StrictPartialOrder(nodes=[submit_artifact, initial_review, loop1, xor1, xor2, xor3, xor4])
root.order.add_edge(submit_artifact, initial_review)
root.order.add_edge(initial_review, loop1)
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, None)