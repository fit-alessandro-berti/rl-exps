from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
root = StrictPartialOrder()

# Define the transitions for the process
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

# Define the edges in the POWL model
root.add_edge(demand_forecast, courier_match)
root.add_edge(courier_match, credential_check)
root.add_edge(credential_check, route_design)
root.add_edge(route_design, load_assign)
root.add_edge(load_assign, traffic_scan)
root.add_edge(traffic_scan, package_secure)
root.add_edge(package_secure, dispatch_alert)
root.add_edge(dispatch_alert, real_time_track)
root.add_edge(real_time_track, incentive_issue)
root.add_edge(incentive_issue, dispute_review)
root.add_edge(dispute_review, customer_notify)
root.add_edge(customer_notify, feedback_collect)
root.add_edge(feedback_collect, performance_log)
root.add_edge(performance_log, ledger_update)
root.add_edge(ledger_update, hub_sync)

# Print the POWL model
print(root)