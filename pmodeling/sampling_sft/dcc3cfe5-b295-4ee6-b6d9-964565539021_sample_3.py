import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
demand_forecast   = Transition(label='Demand Forecast')
courier_match     = Transition(label='Courier Match')
credential_check  = Transition(label='Credential Check')
route_design      = Transition(label='Route Design')
load_assign       = Transition(label='Load Assign')
traffic_scan      = Transition(label='Traffic Scan')
package_secure    = Transition(label='Package Secure')
dispatch_alert    = Transition(label='Dispatch Alert')
real_time_track   = Transition(label='Real-time Track')
incentive_issue   = Transition(label='Incentive Issue')
dispute_review    = Transition(label='Dispute Review')
customer_notify   = Transition(label='Customer Notify')
feedback_collect  = Transition(label='Feedback Collect')
performance_log   = Transition(label='Performance Log')
ledger_update     = Transition(label='Ledger Update')
hub_sync          = Transition(label='Hub Sync')

# Define the loop body for continuous real-time operations
body = StrictPartialOrder(nodes=[
    traffic_scan,
    package_secure,
    dispatch_alert,
    real_time_track,
    incentive_issue,
    dispute_review,
    customer_notify,
    feedback_collect
])
body.order.add_edge(traffic_scan, package_secure)
body.order.add_edge(package_secure, dispatch_alert)
body.order.add_edge(dispatch_alert, real_time_track)
body.order.add_edge(real_time_track, incentive_issue)
body.order.add_edge(incentive_issue, dispute_review)
body.order.add_edge(dispute_review, customer_notify)
body.order.add_edge(customer_notify, feedback_collect)

# Define the LOOP operator: do the initial Demand Forecast, then do body, then repeat
delivery_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[demand_forecast, body]
)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    delivery_loop,
    credential_check,
    route_design,
    load_assign,
    performance_log,
    ledger_update,
    hub_sync
])

# Define the control-flow dependencies
root.order.add_edge(demand_forecast, credential_check)
root.order.add_edge(demand_forecast, route_design)
root.order.add_edge(demand_forecast, load_assign)
root.order.add_edge(credential_check, performance_log)
root.order.add_edge(route_design, performance_log)
root.order.add_edge(load_assign, performance_log)
root.order.add_edge(performance_log, ledger_update)
root.order.add_edge(performance_log, hub_sync)