from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) as nodes in the POWL model
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

# Define the control flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, courier_match])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[credential_check, route_design, load_assign, traffic_scan, package_secure, dispatch_alert, real_time_track, incentive_issue, dispute_review, customer_notify, feedback_collect, performance_log, ledger_update, hub_sync])

# Define the root node as a partial order
root = StrictPartialOrder(nodes=[exclusive_choice, loop1])
root.order.add_edge(exclusive_choice, loop1)

print(root)