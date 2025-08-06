import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
data_collection = Transition(label='Data Collection')
point_aggregation = Transition(label='Point Aggregation')
conflict_check = Transition(label='Conflict Check')
fraud_scan = Transition(label='Fraud Scan')
reward_adjust = Transition(label='Reward Adjust')
redemption_verify = Transition(label='Redemption Verify')
partner_sync = Transition(label='Partner Sync')
behavior_analyze = Transition(label='Behavior Analyze')
async_update = Transition(label='Async Update')
rollback_trigger = Transition(label='Rollback Trigger')
compliance_check = Transition(label='Compliance Check')
notification_send = Transition(label='Notification Send')
user_feedback = Transition(label='User Feedback')
report_generate = Transition(label='Report Generate')
system_audit = Transition(label='System Audit')

# Define silent transitions for rollback and notification
rollback = SilentTransition()
notification = SilentTransition()

# Define loop nodes
data_collection_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_collection])
point_aggregation_loop = OperatorPOWL(operator=Operator.LOOP, children=[point_aggregation])

# Define XOR nodes for point aggregation and conflict check
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, conflict_check])

# Define XOR nodes for fraud scan and reward adjust
fraud_scan_xor = OperatorPOWL(operator=Operator.XOR, children=[fraud_scan, reward_adjust])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze and async update
behavior_analyze_xor = OperatorPOWL(operator=Operator.XOR, children=[behavior_analyze, async_update])

# Define XOR nodes for compliance check and rollback trigger
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, rollback_trigger])

# Define XOR nodes for notification send and user feedback
notification_send_xor = OperatorPOWL(operator=Operator.XOR, children=[notification_send, user_feedback])

# Define XOR nodes for report generate and system audit
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, system_audit])

# Define XOR nodes for data collection and behavior analyze
data_collection_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collection, behavior_analyze])

# Define XOR nodes for point aggregation and fraud scan
point_aggregation_xor = OperatorPOWL(operator=Operator.XOR, children=[point_aggregation, fraud_scan])

# Define XOR nodes for redemption verify and partner sync
redemption_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[redemption_verify, partner_sync])

# Define XOR nodes for behavior analyze