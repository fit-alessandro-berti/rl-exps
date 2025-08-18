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

provenance_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
material_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan])
context_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[context_analysis])
expert_panel_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_panel])
digital_fingerprint_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_fingerprint])
ai_pattern_loop = OperatorPOWL(operator=Operator.LOOP, children=[ai_pattern])
legal_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_audit])
ethics_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[ethics_review])
fraud_detection_loop = OperatorPOWL(operator=Operator.LOOP, children=[fraud_detection])

root = StrictPartialOrder(nodes=[
    submit_artifact,
    initial_review,
    provenance_check_loop,
    material_scan_loop,
    context_analysis_loop,
    expert_panel_loop,
    digital_fingerprint_loop,
    ai_pattern_loop,
    legal_audit_loop,
    ethics_review_loop,
    fraud_detection_loop,
    blockchain_log,
    certification,
    owner_notify,
    archive_data,
    secure_storage
])

root.order.add_edge(submit_artifact, initial_review)
root.order.add_edge(initial_review, provenance_check_loop)
root.order.add_edge(provenance_check_loop, material_scan_loop)
root.order.add_edge(material_scan_loop, context_analysis_loop)
root.order.add_edge(context_analysis_loop, expert_panel_loop)
root.order.add_edge(expert_panel_loop, digital_fingerprint_loop)
root.order.add_edge(digital_fingerprint_loop, ai_pattern_loop)
root.order.add_edge(ai_pattern_loop, legal_audit_loop)
root.order.add_edge(legal_audit_loop, ethics_review_loop)
root.order.add_edge(ethics_review_loop, fraud_detection_loop)
root.order.add_edge(fraud_detection_loop, blockchain_log)
root.order.add_edge(blockchain_log, certification)
root.order.add_edge(certification, owner_notify)
root.order.add_edge(owner_notify, archive_data)
root.order.add_edge(archive_data, secure_storage)