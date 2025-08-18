import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

submit = Transition(label='Submit Artifact')
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

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan])
context_loop = OperatorPOWL(operator=Operator.LOOP, children=[context_analysis, expert_panel])
ai_loop = OperatorPOWL(operator=Operator.LOOP, children=[ai_pattern, legal_audit])
ethics_loop = OperatorPOWL(operator=Operator.LOOP, children=[ethics_review, fraud_detection])
blockchain_loop = OperatorPOWL(operator=Operator.LOOP, children=[blockchain_log, certification])

root = StrictPartialOrder(nodes=[
    submit,
    initial_review,
    provenance_loop,
    context_loop,
    ai_loop,
    ethics_loop,
    blockchain_loop,
    owner_notify,
    archive_data,
    secure_storage
])
root.order.add_edge(submit, initial_review)
root.order.add_edge(initial_review, provenance_loop)
root.order.add_edge(provenance_loop, context_loop)
root.order.add_edge(context_loop, ai_loop)
root.order.add_edge(ai_loop, ethics_loop)
root.order.add_edge(ethics_loop, blockchain_loop)
root.order.add_edge(blockchain_loop, owner_notify)
root.order.add_edge(owner_notify, archive_data)
root.order.add_edge(archive_data, secure_storage)