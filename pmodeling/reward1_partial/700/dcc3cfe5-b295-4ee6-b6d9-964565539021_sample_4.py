import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

demand_forecast = Transition(label='Demand Forecast')
courier_match = Transition(label='Courier Match')
credential_check = Transition(label='Credential Check')
route_design = Transition(label='Route Design')
load_assign = Transition(label='Load Assign')
traffic_scan = Transition(label='Traffic Scan')
package_secure = Transition(label='Package Secure')
dispatch_alert = Transition(label='Dispatch Alert')
real_time_track = Transition(label='Real-time Track')
incentive_issue = Transition(label='Incentive Issue')
dispute_review = Transition(label='Dispute Review')
customer_notify = Transition(label='Customer Notify')
feedback_collect = Transition(label='Feedback Collect')
performance_log = Transition(label='Performance Log')
ledger_update = Transition(label='Ledger Update')
hub_sync = Transition(label='Hub Sync')

skip = SilentTransition()

# Define the process using POWL
demand_forecast_to_courier_match = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, courier_match])
credential_check_to_route_design = OperatorPOWL(operator=Operator.XOR, children=[credential_check, route_design])
traffic_scan_to_package_secure = OperatorPOWL(operator=Operator.XOR, children=[traffic_scan, package_secure])
dispatch_alert_to_real_time_track = OperatorPOWL(operator=Operator.XOR, children=[dispatch_alert, real_time_track])
incentive_issue_to_dispute_review = OperatorPOWL(operator=Operator.XOR, children=[incentive_issue, dispute_review])
customer_notify_to_feedback_collect = OperatorPOWL(operator=Operator.XOR, children=[customer_notify, feedback_collect])
performance_log_to_ledger_update = OperatorPOWL(operator=Operator.XOR, children=[performance_log, ledger_update])
hub_sync_to_performance_log = OperatorPOWL(operator=Operator.XOR, children=[hub_sync, performance_log])

# Define the partial order
root = StrictPartialOrder(nodes=[
    demand_forecast_to_courier_match,
    credential_check_to_route_design,
    traffic_scan_to_package_secure,
    dispatch_alert_to_real_time_track,
    incentive_issue_to_dispute_review,
    customer_notify_to_feedback_collect,
    performance_log_to_ledger_update,
    hub_sync_to_performance_log
])

# Define the order of execution
root.order.add_edge(demand_forecast_to_courier_match, credential_check_to_route_design)
root.order.add_edge(credential_check_to_route_design, traffic_scan_to_package_secure)
root.order.add_edge(traffic_scan_to_package_secure, dispatch_alert_to_real_time_track)
root.order.add_edge(dispatch_alert_to_real_time_track, incentive_issue_to_dispute_review)
root.order.add_edge(incentive_issue_to_dispute_review, customer_notify_to_feedback_collect)
root.order.add_edge(customer_notify_to_feedback_collect, performance_log_to_ledger_update)
root.order.add_edge(performance_log_to_ledger_update, hub_sync_to_performance_log)

# Print the root model
print(root)