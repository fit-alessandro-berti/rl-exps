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
digital_fingerprint = Transition(label='Digital Fingerprint')
legal_audit = Transition(label='Legal Audit')
ethics_review = Transition(label='Ethics Review')
fraud_detection = Transition(label='Fraud Detection')
blockchain_log = Transition(label='Blockchain Log')
certification = Transition(label='Certification')
owner_notify = Transition(label='Owner Notify')
archive_data = Transition(label='Archive Data')
secure_storage = Transition(label='Secure Storage')

# Define the expert panel sub-process as a partial order
expert_sub = StrictPartialOrder(nodes=[expert_panel, ai_pattern, digital_fingerprint])
expert_sub.order.add_edge(expert_panel, ai_pattern)
expert_sub.order.add_edge(ai_pattern, digital_fingerprint)

# Define the loop for repeated fraud detection and blockchain logging
loop_po = OperatorPOWL(operator=Operator.LOOP, children=[fraud_detection, blockchain_log])

# Build the main partial order for the overall process
root = StrictPartialOrder(nodes=[
    submit, initial_review, provenance_check, material_scan, context_analysis,
    expert_sub, loop_po, certification, owner_notify, archive_data, secure_storage
])

# Sequence of activities
root.order.add_edge(submit, initial_review)
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, context_analysis)
root.order.add_edge(context_analysis, expert_sub)
root.order.add_edge(expert_sub, loop_po)
root.order.add_edge(loop_po, certification)
root.order.add_edge(certification, owner_notify)
root.order.add_edge(owner_notify, archive_data)
root.order.add_edge(archive_data, secure_storage)

# Legal and ethics review must complete before any certification step
root.order.add_edge(legal_audit, certification)
root.order.add_edge(ethics_review, certification)

# Final storage must occur after certification
root.order.add_edge(certification, secure_storage)