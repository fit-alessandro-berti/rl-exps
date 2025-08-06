import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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
Skip = SilentTransition()

# Define the partial order
loop_Aging = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Setup, Humidity_Control, Temperature_Monitor, Quality_Test])
loop_Packaging = OperatorPOWL(operator=Operator.LOOP, children=[Packaging, Order_Fulfill, Retail_Deliver, Feedback_Collect])

xor_Milk_Production = OperatorPOWL(operator=Operator.XOR, children=[Milk_Sourcing, Culture_Prep, Milk_Pasteurize, Milk_Inoculate, Curd_Formation, Curd_Cut, Whey_Drain, Mold_Inoculate, Press_Cheese])

root = StrictPartialOrder(nodes=[loop_Aging, loop_Packaging, xor_Milk_Production])
root.order.add_edge(loop_Aging, loop_Packaging)
root.order.add_edge(loop_Aging, xor_Milk_Production)
root.order.add_edge(loop_Packaging, xor_Milk_Production)

# Print the root of the POWL model
print(root)