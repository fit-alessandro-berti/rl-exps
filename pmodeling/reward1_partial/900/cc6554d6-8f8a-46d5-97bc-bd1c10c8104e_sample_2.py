import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Demand_Forecast = Transition(label='Demand Forecast')
Risk_Assess = Transition(label='Risk Assess')
Supplier_Audit = Transition(label='Supplier Audit')
Inventory_Scan = Transition(label='Inventory Scan')
Route_Optimize = Transition(label='Route Optimize')
Order_Prioritize = Transition(label='Order Prioritize')
Contract_Review = Transition(label='Contract Review')
Delay_Monitor = Transition(label='Delay Monitor')
Shipment_Reroute = Transition(label='Shipment Reroute')
Cost_Analyze = Transition(label='Cost Analyze')
Compliance_Check = Transition(label='Compliance Check')
Alternative_Engage = Transition(label='Alternative Engage')
Inventory_Reallocate = Transition(label='Inventory Reallocate')
Performance_Track = Transition(label='Performance Track')
Feedback_Loop = Transition(label='Feedback Loop')
Strategy_Update = Transition(label='Strategy Update')

# Define the control flow
root = StrictPartialOrder(nodes=[
    Demand_Forecast, Risk_Assess, Supplier_Audit, Inventory_Scan, Route_Optimize, Order_Prioritize,
    Contract_Review, Delay_Monitor, Shipment_Reroute, Cost_Analyze, Compliance_Check, Alternative_Engage,
    Inventory_Reallocate, Performance_Track, Feedback_Loop, Strategy_Update
])

# Define the dependencies
root.order.add_edge(Demand_Forecast, Risk_Assess)
root.order.add_edge(Risk_Assess, Supplier_Audit)
root.order.add_edge(Supplier_Audit, Inventory_Scan)
root.order.add_edge(Inventory_Scan, Route_Optimize)
root.order.add_edge(Route_Optimize, Order_Prioritize)
root.order.add_edge(Order_Prioritize, Contract_Review)
root.order.add_edge(Contract_Review, Delay_Monitor)
root.order.add_edge(Delay_Monitor, Shipment_Reroute)
root.order.add_edge(Shipment_Reroute, Cost_Analyze)
root.order.add_edge(Cost_Analyze, Compliance_Check)
root.order.add_edge(Compliance_Check, Alternative_Engage)
root.order.add_edge(Alternative_Engage, Inventory_Reallocate)
root.order.add_edge(Inventory_Reallocate, Performance_Track)
root.order.add_edge(Performance_Track, Feedback_Loop)
root.order.add_edge(Feedback_Loop, Strategy_Update)

# Print the root model
print(root)