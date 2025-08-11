import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
loop = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Sourcing, Quality_Testing, Starter_Prep, Curd_Cutting, Molding_Cheese, Salting_Process, Aging_Control, Humidity_Check, Packaging_Design, Label_Printing, Inventory_Audit, Cold_Storage, Order_Processing, Logistics_Planning, Retail_Delivery, Consumer_Feedback, Batch_Adjustment, Event_Coordination])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)