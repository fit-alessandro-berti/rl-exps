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

# Define silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()

# Define the process tree
xor1 = OperatorPOWL(operator=Operator.XOR, children=[credential_check, skip1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[load_assign, skip2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[package_secure, skip3])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, xor1])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[loop1, xor2])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[loop2, xor3])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[loop3, dispatch_alert])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[loop4, real_time_track])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[loop5, incentive_issue])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[loop6, dispute_review])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[loop7, customer_notify])
loop9 = OperatorPOWL(operator=Operator.LOOP, children=[loop8, feedback_collect])
loop10 = OperatorPOWL(operator=Operator.LOOP, children=[loop9, performance_log])
loop11 = OperatorPOWL(operator=Operator.LOOP, children=[loop10, ledger_update])
loop12 = OperatorPOWL(operator=Operator.LOOP, children=[loop11, hub_sync])

root = StrictPartialOrder(nodes=[loop12])
root.order.add_edge(loop12, loop12)

# Print the root of the POWL model
print(root)