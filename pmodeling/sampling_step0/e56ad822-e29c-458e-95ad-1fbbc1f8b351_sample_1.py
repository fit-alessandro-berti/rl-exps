import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for skipped activities
skip_initial_review = SilentTransition()
skip_material_scan = SilentTransition()
skip_context_analysis = SilentTransition()
skip_ethics_review = SilentTransition()
skip_blockchain_log = SilentTransition()
skip_archive_data = SilentTransition()
skip_secure_storage = SilentTransition()

# Define exclusive choices
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip_legal_audit])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, skip_ethics_review])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[fraud_detection, skip_fraud_detection])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[blockchain_log, skip_blockchain_log])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[archive_data, skip_archive_data])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[secure_storage, skip_secure_storage])

# Define loops
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[initial_review, xor_1])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, xor_2])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, xor_3])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[context_analysis, xor_4])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[expert_panel, xor_5])
loop_6 = OperatorPOWL(operator=Operator.LOOP, children=[digital_fingerprint, xor_6])

# Define the root partial order
root = StrictPartialOrder(nodes=[
    submit_artifact,
    loop_1,
    loop_2,
    loop_3,
    loop_4,
    loop_5,
    loop_6,
    xor_1,
    xor_2,
    xor_3,
    xor_4,
    xor_5,
    xor_6,
    certification,
    owner_notify
])

# Define the partial order dependencies
root.order.add_edge(submit_artifact, loop_1)
root.order.add_edge(loop_1, xor_1)
root.order.add_edge(xor_1, certification)
root.order.add_edge(certification, owner_notify)

root.order.add_edge(submit_artifact, loop_2)
root.order.add_edge(loop_2, xor_2)
root.order.add_edge(xor_2, provenance_check)
root.order.add_edge(provenance_check, loop_3)
root.order.add_edge(loop_3, xor_3)
root.order.add_edge(xor_3, material_scan)
root.order.add_edge(material_scan, loop_4)
root.order.add_edge(loop_4, xor_4)
root.order.add_edge(xor_4, context_analysis)
root.order.add_edge(context_analysis, loop_5)
root.order.add_edge(loop_5, xor_5)
root.order.add_edge(xor_5, expert_panel)
root.order.add_edge(expert_panel, loop_6)
root.order.add_edge(loop_6, xor_6)
root.order.add_edge(xor_6, digital_fingerprint)
root.order.add_edge(digital_fingerprint, certification)
root.order.add_edge(certification, owner_notify)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge(submit_artifact, xor_1)
root.order.add_edge(submit_artifact, xor_2)
root.order.add_edge(submit_artifact, xor_3)
root.order.add_edge(submit_artifact, xor_4)
root.order.add_edge(submit_artifact, xor_5)
root.order.add_edge(submit_artifact, xor_6)

root.order.add_edge