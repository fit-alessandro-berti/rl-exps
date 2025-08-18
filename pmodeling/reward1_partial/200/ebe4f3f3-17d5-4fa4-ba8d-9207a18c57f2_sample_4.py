import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Milk_Sourcing = Transition(label='Milk Sourcing')
Farm_Audit = Transition(label='Farm Audit')
Milk_Testing = Transition(label='Milk Testing')
Batch_Forming = Transition(label='Batch Forming')
Curd_Cutting = Transition(label='Curd Cutting')
Molding_Cheese = Transition(label='Molding Cheese')
Salting_Process = Transition(label='Salting Process')
Aging_Control = Transition(label='Aging Control')
Quality_Check = Transition(label='Quality Check')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Inventory_Update = Transition(label='Inventory Update')
Order_Receiving = Transition(label='Order Receiving')
Retail_Coordination = Transition(label='Retail Coordination')
Shipping_Prep = Transition(label='Shipping Prep')
Customer_Feedback = Transition(label='Customer Feedback')
Demand_Forecast = Transition(label='Demand Forecast')
Limited_Release = Transition(label='Limited Release')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Milk_Sourcing,
    Farm_Audit,
    Milk_Testing,
    Batch_Forming,
    Curd_Cutting,
    Molding_Cheese,
    Salting_Process,
    Aging_Control,
    Quality_Check,
    Packaging_Design,
    Label_Printing,
    Inventory_Update,
    Order_Receiving,
    Retail_Coordination,
    Shipping_Prep,
    Customer_Feedback,
    Demand_Forecast,
    Limited_Release
])

# Add dependencies based on the process description
root.order.add_edge(Milk_Sourcing, Farm_Audit)
root.order.add_edge(Farm_Audit, Milk_Testing)
root.order.add_edge(Milk_Testing, Batch_Forming)
root.order.add_edge(Batch_Forming, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Molding_Cheese)
root.order.add_edge(Molding_Cheese, Salting_Process)
root.order.add_edge(Salting_Process, Aging_Control)
root.order.add_edge(Aging_Control, Quality_Check)
root.order.add_edge(Quality_Check, Packaging_Design)
root.order.add_edge(Packaging_Design, Label_Printing)
root.order.add_edge(Label_Printing, Inventory_Update)
root.order.add_edge(Inventory_Update, Order_Receiving)
root.order.add_edge(Order_Receiving, Retail_Coordination)
root.order.add_edge(Retail_Coordination, Shipping_Prep)
root.order.add_edge(Shipping_Prep, Customer_Feedback)
root.order.add_edge(Customer_Feedback, Demand_Forecast)
root.order.add_edge(Demand_Forecast, Limited_Release)