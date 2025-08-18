import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for stakeholder validation rounds
stakeholder_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_vote, consensus_validate])

# Define the XOR for AI pattern scan and flag anomaly
xor_ai_pattern_scan_flag_anomaly = OperatorPOWL(operator=Operator.XOR, children=[ai_patternscan, flag_anomaly])

# Define the XOR for dispute submit and panel review
xor_dispute_submit_panel_review = OperatorPOWL(operator=Operator.XOR, children=[dispute_submit, panel_review])

# Define the XOR for arbitrate case and trade monitor
xor_arbitrate_case_trade_monitor = OperatorPOWL(operator=Operator.XOR, children=[arbitrate_case, trade_monitor])

# Define the XOR for feedback loop and insurance sync
xor_feedback_loop_insurance_sync = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, insurance_sync])

# Define the XOR for collector notify and insurance sync
xor_collector_notify_insurance_sync = OperatorPOWL(operator=Operator.XOR, children=[collector_notify, insurance_sync])

# Define the partial order with all the transitions and loops
root = StrictPartialOrder(
    nodes=[
        data_capture,
        fingerprint_art,
        record_input,
        historical_check,
        stakeholder_loop,
        xor_ai_pattern_scan_flag_anomaly,
        xor_dispute_submit_panel_review,
        xor_arbitrate_case_trade_monitor,
        xor_feedback_loop_insurance_sync,
        xor_collector_notify_insurance_sync
    ],
    order={
        # Source-->target dependencies
        data_capture: [fingerprint_art],
        fingerprint_art: [record_input],
        record_input: [historical_check],
        historical_check: [stakeholder_loop],
        stakeholder_loop: [xor_ai_pattern_scan_flag_anomaly],
        xor_ai_pattern_scan_flag_anomaly: [xor_dispute_submit_panel_review],
        xor_dispute_submit_panel_review: [xor_arbitrate_case_trade_monitor],
        xor_arbitrate_case_trade_monitor: [xor_feedback_loop_insurance_sync],
        xor_feedback_loop_insurance_sync: [xor_collector_notify_insurance_sync],
        xor_collector_notify_insurance_sync: [collector_notify]
    }
)

# Add dependencies for the stakeholder loop
root.order.add_edge(stakeholder_loop, xor_ai_pattern_scan_flag_anomaly)
root.order.add_edge(stakeholder_loop, xor_dispute_submit_panel_review)

# Add dependencies for the XORs
root.order.add_edge(xor_ai_pattern_scan_flag_anomaly, xor_arbitrate_case_trade_monitor)
root.order.add_edge(xor_dispute_submit_panel_review, xor_arbitrate_case_trade_monitor)
root.order.add_edge(xor_arbitrate_case_trade_monitor, xor_feedback_loop_insurance_sync)
root.order.add_edge(xor_feedback_loop_insurance_sync, xor_collector_notify_insurance_sync)
root.order.add_edge(xor_collector_notify_insurance_sync, collector_notify)

# Print the final POWL model
print(root)