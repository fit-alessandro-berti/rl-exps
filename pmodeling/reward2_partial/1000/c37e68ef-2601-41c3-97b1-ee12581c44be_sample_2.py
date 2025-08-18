import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Prep = Transition(label='Starter Prep')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Molding_Press = Transition(label='Molding Press')
Fermentation_Control = Transition(label='Fermentation Control')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Check = Transition(label='Humidity Check')
Packaging_Design = Transition(label='Packaging Design')
Label_Approval = Transition(label='Label Approval')
Inventory_Audit = Transition(label='Inventory Audit')
Order_Scheduling = Transition(label='Order Scheduling')
Market_Delivery = Transition(label='Market Delivery')
Feedback_Review = Transition(label='Feedback Review')
Compliance_Check = Transition(label='Compliance Check')
Marketing_Sync = Transition(label='Marketing Sync')

root = StrictPartialOrder(nodes=[
    Milk_Sourcing, Quality_Testing, Starter_Prep, Curd_Cutting, Whey_Draining, Molding_Press, Fermentation_Control,
    Aging_Setup, Humidity_Check, Packaging_Design, Label_Approval, Inventory_Audit, Order_Scheduling, Market_Delivery,
    Feedback_Review, Compliance_Check, Marketing_Sync
])

# Define the partial order relationships
root.order.add_edge(Milk_Sourcing, Quality_Testing)
root.order.add_edge(Quality_Testing, Starter_Prep)
root.order.add_edge(Starter_Prep, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Whey_Draining)
root.order.add_edge(Whey_Draining, Molding_Press)
root.order.add_edge(Molding_Press, Fermentation_Control)
root.order.add_edge(Fermentation_Control, Aging_Setup)
root.order.add_edge(Aging_Setup, Humidity_Check)
root.order.add_edge(Humidity_Check, Packaging_Design)
root.order.add_edge(Packaging_Design, Label_Approval)
root.order.add_edge(Label_Approval, Inventory_Audit)
root.order.add_edge(Inventory_Audit, Order_Scheduling)
root.order.add_edge(Order_Scheduling, Market_Delivery)
root.order.add_edge(Market_Delivery, Feedback_Review)
root.order.add_edge(Feedback_Review, Compliance_Check)
root.order.add_edge(Compliance_Check, Marketing_Sync)