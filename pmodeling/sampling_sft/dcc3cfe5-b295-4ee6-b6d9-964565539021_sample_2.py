import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
demand_forecast    = Transition(label='Demand Forecast')
courier_match      = Transition(label='Courier Match')
credential_check   = Transition(label='Credential Check')
route_design       = Transition(label='Route Design')
load_assign        = Transition(label='Load Assign')
traffic_scan       = Transition(label='Traffic Scan')
package_secure     = Transition(label='Package Secure')
dispatch_alert     = Transition(label='Dispatch Alert')
realtime_track     = Transition(label='Real-time Track')
incentive_issue    = Transition(label='Incentive Issue')
dispute_review     = Transition(label='Dispute Review')
customer_notify    = Transition(label='Customer Notify')
feedback_collect   = Transition(label='Feedback Collect')
performance_log    = Transition(label='Performance Log')
ledger_update      = Transition(label='Ledger Update')
hub_sync           = Transition(label='Hub Sync')

# Define the main processing sub-process as a partial order
nodes_main = [
    demand_forecast,
    courier_match,
    credential_check,
    route_design,
    load_assign,
    traffic_scan,
    package_secure,
    dispatch_alert,
    realtime_track,
    incentive_issue,
    dispute_review,
    customer_notify,
    feedback_collect,
    performance_log,
    ledger_update,
    hub_sync
]
po_main = StrictPartialOrder(nodes=nodes_main)

# Define the order edges for the main sub-process
po_main.order.add_edge(demand_forecast, courier_match)
po_main.order.add_edge(courier_match, credential_check)
po_main.order.add_edge(credential_check, route_design)
po_main.order.add_edge(route_design, load_assign)
po_main.order.add_edge(load_assign, traffic_scan)
po_main.order.add_edge(traffic_scan, package_secure)
po_main.order.add_edge(package_secure, dispatch_alert)
po_main.order.add_edge(dispatch_alert, realtime_track)
po_main.order.add_edge(realtime_track, incentive_issue)
po_main.order.add_edge(incentive_issue, dispute_review)
po_main.order.add_edge(dispute_review, customer_notify)
po_main.order.add_edge(customer_notify, feedback_collect)
po_main.order.add_edge(feedback_collect, performance_log)
po_main.order.add_edge(performance_log, ledger_update)
po_main.order.add_edge(ledger_update, hub_sync)

# Define the loop body (excluding ledger_update & hub_sync)
loop_body = StrictPartialOrder(nodes=[
    demand_forecast,
    courier_match,
    credential_check,
    route_design,
    load_assign,
    traffic_scan,
    package_secure,
    dispatch_alert,
    realtime_track,
    incentive_issue,
    dispute_review,
    customer_notify,
    feedback_collect,
    performance_log
])
loop_body.order.add_edge(demand_forecast, courier_match)
loop_body.order.add_edge(courier_match, credential_check)
loop_body.order.add_edge(credential_check, route_design)
loop_body.order.add_edge(route_design, load_assign)
loop_body.order.add_edge(load_assign, traffic_scan)
loop_body.order.add_edge(traffic_scan, package_secure)
loop_body.order.add_edge(package_secure, dispatch_alert)
loop_body.order.add_edge(dispatch_alert, realtime_track)
loop_body.order.add_edge(realtime_track, incentive_issue)
loop_body.order.add_edge(incentive_issue, dispute_review)
loop_body.order.add_edge(dispute_review, customer_notify)
loop_body.order.add_edge(customer_notify, feedback_collect)
loop_body.order.add_edge(feedback_collect, performance_log)

# Define the loop: repeat the body until ledger_update & hub_sync are executed
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, po_main])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, ledger_update)
root.order.add_edge(loop, hub_sync)

print(root)