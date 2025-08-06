import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()

# Define the workflow steps
raw_milk_sourcing = OperatorPOWL(operator=Operator.PO, children=[Milk_Sourcing, Quality_Testing])
starter_prep = OperatorPOWL(operator=Operator.PO, children=[Starter_Prep, Curd_Cutting])
molding_cheese = OperatorPOWL(operator=Operator.PO, children=[Molding_Cheese, Salting_Process])
aging_control = OperatorPOWL(operator=Operator.PO, children=[Aging_Control, Humidity_Check])
packaging_design = OperatorPOWL(operator=Operator.PO, children=[Packaging_Design, Label_Printing])
inventory_audit = OperatorPOWL(operator=Operator.PO, children=[Inventory_Audit, Cold_Storage])
order_processing = OperatorPOWL(operator=Operator.PO, children=[Order_Processing, Logistics_Planning])
retail_delivery = OperatorPOWL(operator=Operator.PO, children=[Retail_Delivery, Consumer_Feedback])
batch_adjustment = OperatorPOWL(operator=Operator.PO, children=[Batch_Adjustment, Event_Coordination])

# Define the loop nodes
raw_milk_sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[raw_milk_sourcing, starter_prep])
molding_cheese_loop = OperatorPOWL(operator=Operator.LOOP, children=[molding_cheese, aging_control])
packaging_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, inventory_audit])
order_processing_loop = OperatorPOWL(operator=Operator.LOOP, children=[order_processing, retail_delivery])
batch_adjustment_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_adjustment, event_coordination])

# Define the partial order
root = StrictPartialOrder(nodes=[raw_milk_sourcing_loop, molding_cheese_loop, packaging_design_loop, order_processing_loop, batch_adjustment_loop])
root.order.add_edge(raw_milk_sourcing_loop, starter_prep)
root.order.add_edge(starter_prep, molding_cheese)
root.order.add_edge(molding_cheese, aging_control)
root.order.add_edge(aging_control, packaging_design)
root.order.add_edge(packaging_design, inventory_audit)
root.order.add_edge(inventory_audit, order_processing)
root.order.add_edge(order_processing, retail_delivery)
root.order.add_edge(retail_delivery, batch_adjustment)
root.order.add_edge(batch_adjustment, event_coordination)