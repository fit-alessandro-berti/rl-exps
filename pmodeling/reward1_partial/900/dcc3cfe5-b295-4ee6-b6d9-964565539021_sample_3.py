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

demand_forecast_to_courier_match = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, skip])
courier_match_to_credential_check = OperatorPOWL(operator=Operator.XOR, children=[courier_match, skip])
credential_check_to_route_design = OperatorPOWL(operator=Operator.XOR, children=[credential_check, skip])
route_design_to_load_assign = OperatorPOWL(operator=Operator.XOR, children=[route_design, skip])
load_assign_to_traffic_scan = OperatorPOWL(operator=Operator.XOR, children=[load_assign, skip])
traffic_scan_to_package_secure = OperatorPOWL(operator=Operator.XOR, children=[traffic_scan, skip])
package_secure_to_dispatch_alert = OperatorPOWL(operator=Operator.XOR, children=[package_secure, skip])
dispatch_alert_to_real_time_track = OperatorPOWL(operator=Operator.XOR, children=[dispatch_alert, skip])
real_time_track_to_incentive_issue = OperatorPOWL(operator=Operator.XOR, children=[real_time_track, skip])
incentive_issue_to_dispute_review = OperatorPOWL(operator=Operator.XOR, children=[incentive_issue, skip])
dispute_review_to_customer_notify = OperatorPOWL(operator=Operator.XOR, children=[dispute_review, skip])
customer_notify_to_feedback_collect = OperatorPOWL(operator=Operator.XOR, children=[customer_notify, skip])
feedback_collect_to_performance_log = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, skip])
performance_log_to_ledger_update = OperatorPOWL(operator=Operator.XOR, children=[performance_log, skip])
ledger_update_to_hub_sync = OperatorPOWL(operator=Operator.XOR, children=[ledger_update, skip])

root = StrictPartialOrder(nodes=[
    demand_forecast,
    courier_match,
    credential_check,
    route_design,
    load_assign,
    traffic_scan,
    package_secure,
    dispatch_alert,
    real_time_track,
    incentive_issue,
    dispute_review,
    customer_notify,
    feedback_collect,
    performance_log,
    ledger_update,
    hub_sync
])

root.order.add_edge(demand_forecast, courier_match)
root.order.add_edge(courier_match, credential_check)
root.order.add_edge(credential_check, route_design)
root.order.add_edge(route_design, load_assign)
root.order.add_edge(load_assign, traffic_scan)
root.order.add_edge(traffic_scan, package_secure)
root.order.add_edge(package_secure, dispatch_alert)
root.order.add_edge(dispatch_alert, real_time_track)
root.order.add_edge(real_time_track, incentive_issue)
root.order.add_edge(incentive_issue, dispute_review)
root.order.add_edge(dispute_review, customer_notify)
root.order.add_edge(customer_notify, feedback_collect)
root.order.add_edge(feedback_collect, performance_log)
root.order.add_edge(performance_log, ledger_update)
root.order.add_edge(ledger_update, hub_sync)