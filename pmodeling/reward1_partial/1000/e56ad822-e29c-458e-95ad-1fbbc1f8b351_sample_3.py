import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, ethics_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[fraud_detection, blockchain_log])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[certification, owner_notify])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[archive_data, secure_storage])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, context_analysis, expert_panel, digital_fingerprint, ai_pattern])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4])

root = StrictPartialOrder(nodes=[submit_artifact, initial_review, loop1, loop2])
root.order.add_edge(submit_artifact, initial_review)
root.order.add_edge(initial_review, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, submit_artifact)