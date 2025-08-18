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

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, context_analysis])
expert_panel_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_panel, ai_pattern, legal_audit, ethics_review, fraud_detection])
blockchain_log_loop = OperatorPOWL(operator=Operator.LOOP, children=[blockchain_log, certification, owner_notify, archive_data, secure_storage])

xor = OperatorPOWL(operator=Operator.XOR, children=[skip, provenance_loop, expert_panel_loop, blockchain_log_loop])

root = StrictPartialOrder(nodes=[submit_artifact, initial_review, xor])
root.order.add_edge(submit_artifact, initial_review)
root.order.add_edge(initial_review, xor)
root.order.add_edge(provenance_loop, xor)
root.order.add_edge(expert_panel_loop, xor)
root.order.add_edge(blockchain_log_loop, xor)