from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process tree
demand_forecast_to_courier_match = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, courier_match])
credential_check_to_route_design = OperatorPOWL(operator=Operator.XOR, children=[credential_check, route_design])
load_assign_to_traffic_scan = OperatorPOWL(operator=Operator.XOR, children=[load_assign, traffic_scan])
package_secure_to_dispatch_alert = OperatorPOWL(operator=Operator.XOR, children=[package_secure, dispatch_alert])
real_time_track_to_incentive_issue = OperatorPOWL(operator=Operator.XOR, children=[real_time_track, incentive_issue])
dispute_review_to_customer_notify = OperatorPOWL(operator=Operator.XOR, children=[dispute_review, customer_notify])
feedback_collect_to_performance_log = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, performance_log])
ledger_update_to_hub_sync = OperatorPOWL(operator=Operator.XOR, children=[ledger_update, hub_sync])

# Define the partial order
root = StrictPartialOrder(nodes=[demand_forecast_to_courier_match, credential_check_to_route_design, load_assign_to_traffic_scan, package_secure_to_dispatch_alert, real_time_track_to_incentive_issue, dispute_review_to_customer_notify, feedback_collect_to_performance_log, ledger_update_to_hub_sync])

# Define the dependencies
root.order.add_edge(demand_forecast_to_courier_match, credential_check_to_route_design)
root.order.add_edge(credential_check_to_route_design, load_assign_to_traffic_scan)
root.order.add_edge(load_assign_to_traffic_scan, package_secure_to_dispatch_alert)
root.order.add_edge(package_secure_to_dispatch_alert, real_time_track_to_incentive_issue)
root.order.add_edge(real_time_track_to_incentive_issue, dispute_review_to_customer_notify)
root.order.add_edge(dispute_review_to_customer_notify, feedback_collect_to_performance_log)
root.order.add_edge(feedback_collect_to_performance_log, ledger_update_to_hub_sync)

# Print the root model
print(root)