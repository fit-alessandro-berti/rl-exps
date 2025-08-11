import pm4py
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
skip = SilentTransition()

# Define the loop and choice nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, courier_match])
xor = OperatorPOWL(operator=Operator.XOR, children=[credential_check, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[route_design, load_assign])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[traffic_scan, package_secure])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[dispatch_alert, real_time_track])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[incentive_issue, dispute_review])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[customer_notify, feedback_collect])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[performance_log, ledger_update])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[hub_sync, skip])

# Create the root node
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, loop)