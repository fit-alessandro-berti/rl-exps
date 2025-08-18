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

# Define silent transitions for no actions
skip = SilentTransition()

# Define the partial order model
root = StrictPartialOrder(
    nodes=[
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
    ],
    order={
        demand_forecast: courier_match,
        courier_match: credential_check,
        credential_check: route_design,
        route_design: load_assign,
        load_assign: traffic_scan,
        traffic_scan: package_secure,
        package_secure: dispatch_alert,
        dispatch_alert: real_time_track,
        real_time_track: incentive_issue,
        incentive_issue: dispute_review,
        dispute_review: customer_notify,
        customer_notify: feedback_collect,
        feedback_collect: performance_log,
        performance_log: ledger_update,
        ledger_update: hub_sync
    }
)