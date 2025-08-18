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

root = StrictPartialOrder(nodes=[
    Demand_Forecast,
    Courier_Match,
    Credential_Check,
    Route_Design,
    Load_Assign,
    Traffic_Scan,
    Package_Secure,
    Dispatch_Alert,
    Real_time_Track,
    Incentive_Issue,
    Dispute_Review,
    Customer_Notify,
    Feedback_Collect,
    Performance_Log,
    Ledger_Update,
    Hub_Sync
])
root.order.add_edge(Demand_Forecast, Courier_Match)
root.order.add_edge(Courier_Match, Credential_Check)
root.order.add_edge(Credential_Check, Route_Design)
root.order.add_edge(Route_Design, Load_Assign)
root.order.add_edge(Load_Assign, Traffic_Scan)
root.order.add_edge(Traffic_Scan, Package_Secure)
root.order.add_edge(Package_Secure, Dispatch_Alert)
root.order.add_edge(Dispatch_Alert, Real_time_Track)
root.order.add_edge(Real_time_Track, Incentive_Issue)
root.order.add_edge(Incentive_Issue, Dispute_Review)
root.order.add_edge(Dispute_Review, Customer_Notify)
root.order.add_edge(Customer_Notify, Feedback_Collect)
root.order.add_edge(Feedback_Collect, Performance_Log)
root.order.add_edge(Performance_Log, Ledger_Update)
root.order.add_edge(Ledger_Update, Hub_Sync)