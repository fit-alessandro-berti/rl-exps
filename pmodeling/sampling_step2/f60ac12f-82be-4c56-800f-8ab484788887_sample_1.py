from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Blending = Transition(label='Culture Blending')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Drain = Transition(label='Whey Drain')
Mold_Inoculate = Transition(label='Mold Inoculate')
Press_Cheese = Transition(label='Press Cheese')
Salt_Brine = Transition(label='Salt Brine')
Age_Monitor = Transition(label='Age Monitor')
Quality_Test = Transition(label='Quality Test')
Packaging_Prep = Transition(label='Packaging Prep')
Label_Design = Transition(label='Label Design')
Order_Allocation = Transition(label='Order Allocation')
Transport_Arrange = Transition(label='Transport Arrange')
Retail_Sync = Transition(label='Retail Sync')
Customer_Review = Transition(label='Customer Review')
Feedback_Analyze = Transition(label='Feedback Analyze')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Milk_Sourcing,
    Culture_Blending,
    Milk_Pasteurize,
    Curd_Cutting,
    Whey_Drain,
    Mold_Inoculate,
    Press_Cheese,
    Salt_Brine,
    Age_Monitor,
    Quality_Test,
    Packaging_Prep,
    Label_Design,
    Order_Allocation,
    Transport_Arrange,
    Retail_Sync,
    Customer_Review,
    Feedback_Analyze
])

# Define the dependencies
root.order.add_edge(Milk_Sourcing, Culture_Blending)
root.order.add_edge(Culture_Blending, Milk_Pasteurize)
root.order.add_edge(Milk_Pasteurize, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Whey_Drain)
root.order.add_edge(Whey_Drain, Mold_Inoculate)
root.order.add_edge(Mold_Inoculate, Press_Cheese)
root.order.add_edge(Press_Cheese, Salt_Brine)
root.order.add_edge(Salt_Brine, Age_Monitor)
root.order.add_edge(Age_Monitor, Quality_Test)
root.order.add_edge(Quality_Test, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Label_Design)
root.order.add_edge(Label_Design, Order_Allocation)
root.order.add_edge(Order_Allocation, Transport_Arrange)
root.order.add_edge(Transport_Arrange, Retail_Sync)
root.order.add_edge(Retail_Sync, Customer_Review)
root.order.add_edge(Customer_Review, Feedback_Analyze)

print(root)