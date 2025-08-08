import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their names
Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Prep = Transition(label='Culture Prep')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Milk_Inoculate = Transition(label='Milk Inoculate')
Curd_Formation = Transition(label='Curd Formation')
Curd_Cut = Transition(label='Curd Cut')
Whey_Drain = Transition(label='Whey Drain')
Mold_Inoculate = Transition(label='Mold Inoculate')
Press_Cheese = Transition(label='Press Cheese')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Control = Transition(label='Humidity Control')
Temperature_Monitor = Transition(label='Temperature Monitor')
Quality_Test = Transition(label='Quality Test')
Packaging = Transition(label='Packaging')
Order_Fulfill = Transition(label='Order Fulfill')
Retail_Deliver = Transition(label='Retail Deliver')
Feedback_Collect = Transition(label='Feedback Collect')

# Define the loop for the aging process
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[Humidity_Control, Temperature_Monitor])

# Define the XOR for the quality testing and packaging
quality_test_packaging_xor = OperatorPOWL(operator=Operator.XOR, children=[Quality_Test, Packaging])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[Milk_Sourcing, Culture_Prep, Milk_Pasteurize, Milk_Inoculate, Curd_Formation, Curd_Cut, Whey_Drain, Mold_Inoculate, Press_Cheese, Aging_Setup, aging_loop, quality_test_packaging_xor, Order_Fulfill, Retail_Deliver, Feedback_Collect])

# Define the order dependencies
root.order.add_edge(Milk_Sourcing, Culture_Prep)
root.order.add_edge(Culture_Prep, Milk_Pasteurize)
root.order.add_edge(Milk_Pasteurize, Milk_Inoculate)
root.order.add_edge(Milk_Inoculate, Curd_Formation)
root.order.add_edge(Curd_Formation, Curd_Cut)
root.order.add_edge(Curd_Cut, Whey_Drain)
root.order.add_edge(Whey_Drain, Mold_Inoculate)
root.order.add_edge(Mold_Inoculate, Press_Cheese)
root.order.add_edge(Press_Cheese, Aging_Setup)
root.order.add_edge(Aging_Setup, aging_loop)
root.order.add_edge(aging_loop, quality_test_packaging_xor)
root.order.add_edge(quality_test_packaging_xor, Order_Fulfill)
root.order.add_edge(Order_Fulfill, Retail_Deliver)
root.order.add_edge(Retail_Deliver, Feedback_Collect)