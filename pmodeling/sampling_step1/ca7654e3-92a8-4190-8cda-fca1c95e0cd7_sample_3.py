import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the process flow
root = StrictPartialOrder(nodes=[
    Milk_Sourcing, Curd_Preparation, starter_Culture, Temperature_Control, Pressing_Cheese,
    Salting_Stage, Aging_Process, Microbial_Test, Quality_Check, Eco_Packaging, Label_Printing,
    Inventory_Audit, Order_Processing, Retail_Shipping, Customer_Feedback, Recipe_Update,
    Market_Analysis
])

# Add dependencies between nodes
root.order.add_edge(Milk_Sourcing, Curd_Preparation)
root.order.add_edge(Curd_Preparation, starter_Culture)
root.order.add_edge(starter_Culture, Temperature_Control)
root.order.add_edge(Temperature_Control, Pressing_Cheese)
root.order.add_edge(Pressing_Cheese, Salting_Stage)
root.order.add_edge(Salting_Stage, Aging_Process)
root.order.add_edge(Aging_Process, Microbial_Test)
root.order.add_edge(Microbial_Test, Quality_Check)
root.order.add_edge(Quality_Check, Eco_Packaging)
root.order.add_edge(Eco_Packaging, Label_Printing)
root.order.add_edge(Label_Printing, Inventory_Audit)
root.order.add_edge(Inventory_Audit, Order_Processing)
root.order.add_edge(Order_Processing, Retail_Shipping)
root.order.add_edge(Retail_Shipping, Customer_Feedback)
root.order.add_edge(Customer_Feedback, Recipe_Update)
root.order.add_edge(Recipe_Update, Market_Analysis)

# Print the root node to confirm the POWL model
print(root)