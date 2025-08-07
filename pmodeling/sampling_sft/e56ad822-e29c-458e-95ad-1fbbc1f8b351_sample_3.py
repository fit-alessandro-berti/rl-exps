import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
submit = Transition(label='Submit Artifact')
initial_review = Transition(label='Initial Review')
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
context_analysis = Transition(label='Context Analysis')
expert_panel = Transition(label='Expert Panel')
ai_pattern = Transition(label='AI Pattern')
legal_audit = Transition(label='Legal Audit')
ethics_review = Transition(label='Ethics Review')
fraud_detection = Transition(label='Fraud Detection')
digital_fingerprint = Transition(label='Digital Fingerprint')
blockchain_log = Transition(label='Blockchain Log')
certification = Transition(label='Certification')
owner_notify = Transition(label='Owner Notify')
archive_data = Transition(label='Archive Data')
secure_storage = Transition(label='Secure Storage')

# Build the loop for expert panel & fraud detection
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_panel, fraud_detection])

# Build the AI pattern analysis as a concurrent group
ai_group = StrictPartialOrder(nodes=[ai_pattern, blockchain_log])
ai_group.order.add_edge(ai_pattern, blockchain_log)

# Build the core processing partial order
core = StrictPartialOrder(nodes=[
    initial_review,
    provenance_check,
    material_scan,
    context_analysis,
    expert_loop,
    ai_group,
    legal_audit,
    ethics_review,
    digital_fingerprint,
    certification,
    owner_notify,
    archive_data,
    secure_storage
])
core.order.add_edge(initial_review, provenance_check)
core.order.add_edge(provenance_check, material_scan)
core.order.add_edge(material_scan, context_analysis)
core.order.add_edge(context_analysis, expert_loop)
core.order.add_edge(expert_loop, ai_group)
core.order.add_edge(ai_group, legal_audit)
core.order.add_edge(legal_audit, ethics_review)
core.order.add_edge(ethics_review, digital_fingerprint)
core.order.add_edge(digital_fingerprint, certification)
core.order.add_edge(certification, owner_notify)
core.order.add_edge(owner_notify, archive_data)
core.order.add_edge(archive_data, secure_storage)

# Final root partial order
root = StrictPartialOrder(nodes=[submit, core])
root.order.add_edge(submit, initial_review)