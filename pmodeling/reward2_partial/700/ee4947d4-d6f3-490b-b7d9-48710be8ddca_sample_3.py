from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
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

# Create the partial order graph
root = StrictPartialOrder(nodes=[data_capture, fingerprint_art, record_input, historical_check, stakeholder_vote, consensus_validate, timestamp_entry, ledger_update, ai_patternscan, flag_anomaly, dispute_submit, panel_review, arbitrate_case, trade_monitor, feedback_loop, insurance_sync, collector_notify])

# Define the partial order relationships
root.order.add_edge(data_capture, fingerprint_art)
root.order.add_edge(fingerprint_art, record_input)
root.order.add_edge(record_input, historical_check)
root.order.add_edge(historical_check, stakeholder_vote)
root.order.add_edge(stakeholder_vote, consensus_validate)
root.order.add_edge(consensus_validate, timestamp_entry)
root.order.add_edge(timestamp_entry, ledger_update)
root.order.add_edge(ledger_update, ai_patternscan)
root.order.add_edge(ai_patternscan, flag_anomaly)
root.order.add_edge(flag_anomaly, dispute_submit)
root.order.add_edge(dispute_submit, panel_review)
root.order.add_edge(panel_review, arbitrate_case)
root.order.add_edge(arbitrate_case, trade_monitor)
root.order.add_edge(trade_monitor, feedback_loop)
root.order.add_edge(feedback_loop, insurance_sync)
root.order.add_edge(insurance_sync, collector_notify)

print(root)