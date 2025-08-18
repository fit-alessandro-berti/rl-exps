import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Prep = Transition(label='Starter Prep')
Curd_Cutting = Transition(label='Curd Cutting')
Molding_Cheese = Transition(label='Molding Cheese')
Salting_Process = Transition(label='Salting Process')
Aging_Control = Transition(label='Aging Control')
Humidity_Check = Transition(label='Humidity Check')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Inventory_Audit = Transition(label='Inventory Audit')
Cold_Storage = Transition(label='Cold Storage')
Order_Processing = Transition(label='Order Processing')
Logistics_Planning = Transition(label='Logistics Planning')
Retail_Delivery = Transition(label='Retail Delivery')
Consumer_Feedback = Transition(label='Consumer Feedback')
Batch_Adjustment = Transition(label='Batch Adjustment')
Event_Coordination = Transition(label='Event Coordination')

# Define the partial order
root = StrictPartialOrder()

# Define the dependencies between activities
root.order.add_edge(Milk_Sourcing, Quality_Testing)
root.order.add_edge(Quality_Testing, Starter_Prep)
root.order.add_edge(Starter_Prep, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Molding_Cheese)
root.order.add_edge(Molding_Cheese, Salting_Process)
root.order.add_edge(Salting_Process, Aging_Control)
root.order.add_edge(Aging_Control, Humidity_Check)
root.order.add_edge(Humidity_Check, Packaging_Design)
root.order.add_edge(Packaging_Design, Label_Printing)
root.order.add_edge(Label_Printing, Inventory_Audit)
root.order.add_edge(Inventory_Audit, Cold_Storage)
root.order.add_edge(Cold_Storage, Order_Processing)
root.order.add_edge(Order_Processing, Logistics_Planning)
root.order.add_edge(Logistics_Planning, Retail_Delivery)
root.order.add_edge(Retail_Delivery, Consumer_Feedback)
root.order.add_edge(Consumer_Feedback, Batch_Adjustment)
root.order.add_edge(Batch_Adjustment, Event_Coordination)

# Add a silent transition for the start
root.order.add_edge(None, Milk_Sourcing)

# Add a silent transition for the end
root.order.add_edge(Event_Coordination, None)