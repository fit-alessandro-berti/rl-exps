import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the partial order structure
root = StrictPartialOrder(nodes=[demand_forecast, courier_match, credential_check, route_design, load_assign, traffic_scan, package_secure, dispatch_alert, real_time_track, incentive_issue, dispute_review, customer_notify, feedback_collect, performance_log, ledger_update, hub_sync])

# Define the partial order edges
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

print(root)