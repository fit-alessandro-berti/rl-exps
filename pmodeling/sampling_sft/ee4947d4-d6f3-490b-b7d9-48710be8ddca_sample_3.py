import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
data_capture    = Transition(label='Data Capture')
fingerprint_art = Transition(label='Fingerprint Art')
record_input    = Transition(label='Record Input')
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

# Loop for dispute resolution: submit -> review -> arbitration -> submit (repeat until exit)
dispute_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[dispute_submit, OperatorPOWL(operator=Operator.XOR, children=[panel_review, arbitrate_case])]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    data_capture, fingerprint_art, record_input, historical_check,
    stakeholder_vote, consensus_validate, timestamp_entry, ledger_update,
    ai_pattern_scan, flag_anomaly, dispute_loop,
    trade_monitor, feedback_loop, insurance_sync, collector_notify
])

# Define the control-flow dependencies
root.order.add_edge(data_capture, fingerprint_art)
root.order.add_edge(fingerprint_art, record_input)
root.order.add_edge(record_input, historical_check)
root.order.add_edge(historical_check, stakeholder_vote)
root.order.add_edge(stakeholder_vote, consensus_validate)
root.order.add_edge(consensus_validate, timestamp_entry)
root.order.add_edge(timestamp_entry, ledger_update)
root.order.add_edge(ledger_update, ai_pattern_scan)
root.order.add_edge(ai_pattern_scan, flag_anomaly)
root.order.add_edge(flag_anomaly, dispute_loop)

# After dispute resolution, update AI patterns and monitor trade
root.order.add_edge(dispute_loop, ai_pattern_scan)
root.order.add_edge(dispute_loop, trade_monitor)

# Finally, run the feedback loop and sync with insurance and collectors
root.order.add_edge(ai_pattern_scan, feedback_loop)
root.order.add_edge(trade_monitor, feedback_loop)
root.order.add_edge(feedback_loop, insurance_sync)
root.order.add_edge(feedback_loop, collector_notify)