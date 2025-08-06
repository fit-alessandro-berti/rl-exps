import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
data_capture = Transition(label='Data Capture')
fingerprint_art = Transition(label='Fingerprint Art')
record_input = Transition(label='Record Input')
historical_check = Transition(label='Historical Check')
stakeholder_vote = Transition(label='Stakeholder Vote')
consensus_validate = Transition(label='Consensus Validate')
timestamp_entry = Transition(label='Timestamp Entry')
ledger_update = Transition(label='Ledger Update')
ai_pattern_scan = Transition(label='AI PatternScan')
flag_anomaly = Transition(label='Flag Anomaly')
dispute_submit = Transition(label='Dispute Submit')
panel_review = Transition(label='Panel Review')
arbitrate_case = Transition(label='Arbitrate Case')
trade_monitor = Transition(label='Trade Monitor')
feedback_loop = Transition(label='Feedback Loop')
insurance_sync = Transition(label='Insurance Sync')
collector_notify = Transition(label='Collector Notify')

# Define silent transitions
skip = SilentTransition()

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_vote, skip])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[historical_check, xor])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[record_input, loop1])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[fingerprint_art, loop2])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[timestamp_entry, loop3])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[ledger_update, loop4])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[ai_pattern_scan, loop5])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[flag_anomaly, loop6])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[dispute_submit, loop7])
loop9 = OperatorPOWL(operator=Operator.LOOP, children=[panel_review, loop8])
loop10 = OperatorPOWL(operator=Operator.LOOP, children=[arbitrate_case, loop9])
loop11 = OperatorPOWL(operator=Operator.LOOP, children=[trade_monitor, loop10])
loop12 = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, loop11])
loop13 = OperatorPOWL(operator=Operator.LOOP, children=[insurance_sync, loop12])
loop14 = OperatorPOWL(operator=Operator.LOOP, children=[collector_notify, loop13])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[loop14])

# Add edges between the nodes to define the flow of the process
root.order.add_edge(data_capture, loop1)
root.order.add_edge(historical_check, loop2)
root.order.add_edge(record_input, loop3)
root.order.add_edge(fingerprint_art, loop4)
root.order.add_edge(timestamp_entry, loop5)
root.order.add_edge(ledger_update, loop6)
root.order.add_edge(ai_pattern_scan, loop7)
root.order.add_edge(flag_anomaly, loop8)
root.order.add_edge(dispute_submit, loop9)
root.order.add_edge(panel_review, loop10)
root.order.add_edge(arbitrate_case, loop11)
root.order.add_edge(trade_monitor, loop12)
root.order.add_edge(feedback_loop, loop13)
root.order.add_edge(insurance_sync, loop14)
root.order.add_edge(collector_notify, loop14)

# Print the POWL model
print(root)