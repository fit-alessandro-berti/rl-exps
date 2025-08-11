import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Sourcing, Culture_Prep, Milk_Pasteurize, Milk_Inoculate, Curd_Formation, Curd_Cut, Whey_Drain, Mold_Inoculate, Press_Cheese, Aging_Setup])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Humidity_Control, Temperature_Monitor])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Test, Packaging, Order_Fulfill, Retail_Deliver])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Collect])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop3, loop4])

root = StrictPartialOrder(nodes=[xor1, xor2])
root.order.add_edge(xor1, xor2)