import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Culture = Transition(label='Starter Culture')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salting_Stage = Transition(label='Salting Stage')
Fermentation = Transition(label='Fermentation')
Aging_Control = Transition(label='Aging Control')
Flavor_Tasting = Transition(label='Flavor Tasting')
Packaging_Artisanal = Transition(label='Packaging Artisanal')
Label_Printing = Transition(label='Label Printing')
Order_Processing = Transition(label='Order Processing')
Direct_Delivery = Transition(label='Direct Delivery')
Customer_Feedback = Transition(label='Customer Feedback')

# Define the loop for the fermentation and aging stages
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[Fermentation, Aging_Control])

# Define the exclusive choice for the flavor tasting and packaging stages
flavor_tasting_packaging = OperatorPOWL(operator=Operator.XOR, children=[Flavor_Tasting, Packaging_Artisanal])

# Define the loop for the customer feedback and order processing stages
customer_feedback_order_processing = OperatorPOWL(operator=Operator.LOOP, children=[Customer_Feedback, Order_Processing])

# Define the root process
root = StrictPartialOrder(nodes=[Milk_Sourcing, Quality_Testing, Starter_Culture, Milk_Pasteurize, Curd_Cutting, Whey_Draining, Pressing_Cheese, Salting_Stage, fermentation_loop, flavor_tasting_packaging, Direct_Delivery, customer_feedback_order_processing])
root.order.add_edge(Milk_Sourcing, Quality_Testing)
root.order.add_edge(Quality_Testing, Starter_Culture)
root.order.add_edge(Starter_Culture, Milk_Pasteurize)
root.order.add_edge(Milk_Pasteurize, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Whey_Draining)
root.order.add_edge(Whey_Draining, Pressing_Cheese)
root.order.add_edge(Pressing_Cheese, Salting_Stage)
root.order.add_edge(Salting_Stage, fermentation_loop)
root.order.add_edge(fermentation_loop, flavor_tasting_packaging)
root.order.add_edge(flavor_tasting_packaging, Direct_Delivery)
root.order.add_edge(Direct_Delivery, customer_feedback_order_processing)
root.order.add_edge(customer_feedback_order_processing, Customer_Feedback)

print(root)