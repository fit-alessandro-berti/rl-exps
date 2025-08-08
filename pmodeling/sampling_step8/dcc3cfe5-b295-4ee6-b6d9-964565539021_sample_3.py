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

demand_forecast_xor = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, skip])

credential_check_xor = OperatorPOWL(operator=Operator.XOR, children=[credential_check, skip])

traffic_scan_xor = OperatorPOWL(operator=Operator.XOR, children=[traffic_scan, skip])

package_secure_xor = OperatorPOWL(operator=Operator.XOR, children=[package_secure, skip])

dispatch_alert_xor = OperatorPOWL(operator=Operator.XOR, children=[dispatch_alert, skip])

real_time_track_xor = OperatorPOWL(operator=Operator.XOR, children=[real_time_track, skip])

incentive_issue_xor = OperatorPOWL(operator=Operator.XOR, children=[incentive_issue, skip])

dispute_review_xor = OperatorPOWL(operator=Operator.XOR, children=[dispute_review, skip])

customer_notify_xor = OperatorPOWL(operator=Operator.XOR, children=[customer_notify, skip])

feedback_collect_xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, skip])

hub_sync_xor = OperatorPOWL(operator=Operator.XOR, children=[hub_sync, skip])

root = StrictPartialOrder(nodes=[demand_forecast_xor, credential_check_xor, traffic_scan_xor, package_secure_xor, dispatch_alert_xor, real_time_track_xor, incentive_issue_xor, dispute_review_xor, customer_notify_xor, feedback_collect_xor, hub_sync_xor])
root.order.add_edge(demand_forecast_xor, courier_match)
root.order.add_edge(courier_match, credential_check_xor)
root.order.add_edge(credential_check_xor, route_design)
root.order.add_edge(route_design, load_assign)
root.order.add_edge(load_assign, traffic_scan_xor)
root.order.add_edge(traffic_scan_xor, package_secure_xor)
root.order.add_edge(package_secure_xor, dispatch_alert_xor)
root.order.add_edge(dispatch_alert_xor, real_time_track_xor)
root.order.add_edge(real_time_track_xor, incentive_issue_xor)
root.order.add_edge(incentive_issue_xor, dispute_review_xor)
root.order.add_edge(dispute_review_xor, customer_notify_xor)
root.order.add_edge(customer_notify_xor, feedback_collect_xor)
root.order.add_edge(feedback_collect_xor, hub_sync_xor)