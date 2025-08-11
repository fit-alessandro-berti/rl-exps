import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
Milk_Sourcing = Transition(label='Milk Sourcing')
Curd_Preparation = Transition(label='Curd Preparation')
starter_Culture = Transition(label='starter Culture')
Temperature_Control = Transition(label='Temperature Control')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salting_Stage = Transition(label='Salting Stage')
Aging_Process = Transition(label='Aging Process')
Microbial_Test = Transition(label='Microbial Test')
Quality_Check = Transition(label='Quality Check')
Eco_Packaging = Transition(label='Eco Packaging')
Label_Printing = Transition(label='Label Printing')
Inventory_Audit = Transition(label='Inventory Audit')
Order_Processing = Transition(label='Order Processing')
Retail_Shipping = Transition(label='Retail Shipping')
Customer_Feedback = Transition(label='Customer Feedback')
Recipe_Update = Transition(label='Recipe Update')
Market_Analysis = Transition(label='Market Analysis')

# Define the POWL model structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Curd_Preparation, starter_Culture, Temperature_Control, Pressing_Cheese, Salting_Stage, Aging_Process, Microbial_Test, Quality_Check, Eco_Packaging, Label_Printing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Inventory_Audit, Order_Processing, Retail_Shipping])
xor = OperatorPOWL(operator=Operator.XOR, children=[Customer_Feedback, Market_Analysis])
root = StrictPartialOrder(nodes=[loop1, loop2, xor])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)