import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the silent transitions (tau labels)
skip = SilentTransition()

# Define the process flow using POWL operators
# Demand Forecast -> Courier Match -> Credential Check
demand_courier_credential = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[demand_forecast, courier_match, credential_check])

# Credential Check -> Route Design -> Load Assign
credential_route_load = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[credential_check, route_design, load_assign])

# Load Assign -> Traffic Scan -> Package Secure
load_traffic_secure = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[load_assign, traffic_scan, package_secure])

# Package Secure -> Dispatch Alert -> Real-time Track
package_dispatch_track = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[package_secure, dispatch_alert, real_time_track])

# Dispatch Alert -> Incentive Issue -> Dispute Review
dispatch_incentive_dispute = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[dispatch_alert, incentive_issue, dispute_review])

# Incentive Issue -> Customer Notify -> Feedback Collect
incentive_notify_collect = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[incentive_issue, customer_notify, feedback_collect])

# Customer Notify -> Performance Log -> Ledger Update
notify_performance_ledger = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[customer_notify, performance_log, ledger_update])

# Performance Log -> Hub Sync
performance_hub = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[performance_log, hub_sync])

# Create the root POWL model
root = StrictPartialOrder(nodes=[
    demand_courier_credential,
    credential_route_load,
    load_traffic_secure,
    package_dispatch_track,
    dispatch_incentive_dispute,
    incentive_notify_collect,
    notify_performance_ledger,
    performance_hub
])

# Define the dependencies (edges) between the nodes
root.order.add_edge(demand_courier_credential, credential_route_load)
root.order.add_edge(credential_route_load, load_traffic_secure)
root.order.add_edge(load_traffic_secure, package_dispatch_track)
root.order.add_edge(package_dispatch_track, dispatch_incentive_dispute)
root.order.add_edge(dispatch_incentive_dispute, incentive_notify_collect)
root.order.add_edge(incentive_notify_collect, notify_performance_ledger)
root.order.add_edge(notify_performance_ledger, performance_hub)

print(root)