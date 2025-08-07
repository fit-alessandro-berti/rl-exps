import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
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

# Create the root of the POWL model as a StrictPartialOrder
root = StrictPartialOrder(nodes=[
    data_capture, fingerprint_art, record_input, historical_check,
    stakeholder_vote, consensus_validate, timestamp_entry, ledger_update,
    ai_patternscan, flag_anomaly, dispute_submit, panel_review,
    arbitrate_case, trade_monitor, feedback_loop, insurance_sync,
    collector_notify
])

# Define the dependencies between activities (POWL model structure)
root.order.add_edge(data_capture, fingerprint_art)
root.order.add_edge(data_capture, record_input)
root.order.add_edge(data_capture, historical_check)
root.order.add_edge(data_capture, stakeholder_vote)
root.order.add_edge(fingerprint_art, consensus_validate)
root.order.add_edge(fingerprint_art, timestamp_entry)
root.order.add_edge(fingerprint_art, ledger_update)
root.order.add_edge(ledger_update, ai_patternscan)
root.order.add_edge(ledger_update, flag_anomaly)
root.order.add_edge(flag_anomaly, dispute_submit)
root.order.add_edge(flag_anomaly, panel_review)
root.order.add_edge(flag_anomaly, arbitrate_case)
root.order.add_edge(flag_anomaly, trade_monitor)
root.order.add_edge(flag_anomaly, feedback_loop)
root.order.add_edge(flag_anomaly, insurance_sync)
root.order.add_edge(flag_anomaly, collector_notify)

# The final POWL model is represented by the 'root' variable