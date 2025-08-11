import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Material_Sourcing = Transition(label='Material Sourcing')
Supplier_Audit = Transition(label='Supplier Audit')
Credential_Verify = Transition(label='Credential Verify')
Design_Concept = Transition(label='Design Concept')
Prototype_Build = Transition(label='Prototype Build')
Quality_Review = Transition(label='Quality Review')
Artisan_Assign = Transition(label='Artisan Assign')
Batch_Scheduling = Transition(label='Batch Scheduling')
Custom_Approvals = Transition(label='Custom Approvals')
Inventory_Adjust = Transition(label='Inventory Adjust')
Production_Sync = Transition(label='Production Sync')
Shipping_Plan = Transition(label='Shipping Plan')
Compliance_Check = Transition(label='Compliance Check')
Feedback_Loop = Transition(label='Feedback Loop')
Market_Target = Transition(label='Market Target')
Order_Fulfill = Transition(label='Order Fulfill')
Sustainability = Transition(label='Sustainability')
Customer_Engage = Transition(label='Customer Engage')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Material_Sourcing,
    Supplier_Audit,
    Credential_Verify,
    Design_Concept,
    Prototype_Build,
    Quality_Review,
    Artisan_Assign,
    Batch_Scheduling,
    Custom_Approvals,
    Inventory_Adjust,
    Production_Sync,
    Shipping_Plan,
    Compliance_Check,
    Feedback_Loop,
    Market_Target,
    Order_Fulfill,
    Sustainability,
    Customer_Engage
])

# Define the dependencies
root.order.add_edge(Material_Sourcing, Supplier_Audit)
root.order.add_edge(Supplier_Audit, Credential_Verify)
root.order.add_edge(Credential_Verify, Design_Concept)
root.order.add_edge(Design_Concept, Prototype_Build)
root.order.add_edge(Prototype_Build, Quality_Review)
root.order.add_edge(Quality_Review, Artisan_Assign)
root.order.add_edge(Artisan_Assign, Batch_Scheduling)
root.order.add_edge(Batch_Scheduling, Custom_Approvals)
root.order.add_edge(Custom_Approvals, Inventory_Adjust)
root.order.add_edge(Inventory_Adjust, Production_Sync)
root.order.add_edge(Production_Sync, Shipping_Plan)
root.order.add_edge(Shipping_Plan, Compliance_Check)
root.order.add_edge(Compliance_Check, Feedback_Loop)
root.order.add_edge(Feedback_Loop, Market_Target)
root.order.add_edge(Market_Target, Order_Fulfill)
root.order.add_edge(Order_Fulfill, Sustainability)
root.order.add_edge(Sustainability, Customer_Engage)