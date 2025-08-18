import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
data_capture = Transition(label='Data Capture')
fingerprint_art = Transition(label='Fingerprint Art')
record_input = Transition(label='Record Input')
historical_check = Transition(label='Historical Check')
stakeholder_vote = Transition(label='Stakeholder Vote')
consensus_validate = Transition(label='Consensus Validate')
timestamp_entry = Transition(label='Timestamp Entry')
ledger_update = Transition(label='Ledger Update')
ai_patternscan = Transition(label='AI PatternScan')
flag_anomaly = Transition(label='Flag Anomaly')
dispute_submit = Transition(label='Dispute Submit')
panel_review = Transition(label='Panel Review')
arbitrate_case = Transition(label='Arbitrate Case')
trade_monitor = Transition(label='Trade Monitor')
feedback_loop = Transition(label='Feedback Loop')
insurance_sync = Transition(label='Insurance Sync')
collector_notify = Transition(label='Collector Notify')

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_vote, consensus_validate])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[historical_check, ai_patternscan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[timestamp_entry, ledger_update])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[flag_anomaly, dispute_submit])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[panel_review, arbitrate_case])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[trade_monitor, feedback_loop])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[insurance_sync, collector_notify])

# Define the partial order
root = StrictPartialOrder(nodes=[data_capture, fingerprint_art, record_input, xor, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(data_capture, fingerprint_art)
root.order.add_edge(fingerprint_art, record_input)
root.order.add_edge(record_input, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)

print(root)