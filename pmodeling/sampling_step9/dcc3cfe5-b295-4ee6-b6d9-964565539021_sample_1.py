import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Demand_Forecast = Transition(label='Demand Forecast')
Courier_Match = Transition(label='Courier Match')
Credential_Check = Transition(label='Credential Check')
Route_Design = Transition(label='Route Design')
Load_Assign = Transition(label='Load Assign')
Traffic_Scan = Transition(label='Traffic Scan')
Package_Secure = Transition(label='Package Secure')
Dispatch_Alert = Transition(label='Dispatch Alert')
Real_time_Track = Transition(label='Real-time Track')
Incentive_Issue = Transition(label='Incentive Issue')
Dispute_Review = Transition(label='Dispute Review')
Customer_Notify = Transition(label='Customer Notify')
Feedback_Collect = Transition(label='Feedback Collect')
Performance_Log = Transition(label='Performance Log')
Ledger_Update = Transition(label='Ledger Update')
Hub_Sync = Transition(label='Hub Sync')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Demand_Forecast, Credential_Check])
xor = OperatorPOWL(operator=Operator.XOR, children=[Route_Design, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)