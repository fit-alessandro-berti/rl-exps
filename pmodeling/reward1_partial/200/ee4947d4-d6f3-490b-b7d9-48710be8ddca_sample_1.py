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
ai_patternscan = Transition(label='AI PatternScan')
flag_anomaly = Transition(label='Flag Anomaly')
dispute_submit = Transition(label='Dispute Submit')
panel_review = Transition(label='Panel Review')
arbitrate_case = Transition(label='Arbitrate Case')
trade_monitor = Transition(label='Trade Monitor')
feedback_loop = Transition(label='Feedback Loop')
insurance_sync = Transition(label='Insurance Sync')
collector_notify = Transition(label='Collector Notify')

# Define workflow
root = StrictPartialOrder(
    nodes=[data_capture, fingerprint_art, record_input, historical_check, stakeholder_vote, consensus_validate,
           timestamp_entry, ledger_update, ai_patternscan, flag_anomaly, dispute_submit, panel_review, arbitrate_case,
           trade_monitor, feedback_loop, insurance_sync, collector_notify],
    order={
        data_capture: fingerprint_art,
        fingerprint_art: record_input,
        record_input: historical_check,
        historical_check: stakeholder_vote,
        stakeholder_vote: consensus_validate,
        consensus_validate: timestamp_entry,
        timestamp_entry: ledger_update,
        ledger_update: ai_patternscan,
        ai_patternscan: flag_anomaly,
        flag_anomaly: dispute_submit,
        dispute_submit: panel_review,
        panel_review: arbitrate_case,
        arbitrate_case: trade_monitor,
        trade_monitor: feedback_loop,
        feedback_loop: insurance_sync,
        insurance_sync: collector_notify
    }
)