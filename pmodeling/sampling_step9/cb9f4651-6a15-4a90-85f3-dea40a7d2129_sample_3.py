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

loop_Milk_Pasteurize = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Pasteurize, Milk_Inoculate])
loop_Curd_Formation = OperatorPOWL(operator=Operator.LOOP, children=[Curd_Formation, Curd_Cut, Whey_Drain])
loop_Mold_Inoculate = OperatorPOWL(operator=Operator.LOOP, children=[Mold_Inoculate])
loop_Press_Cheese = OperatorPOWL(operator=Operator.LOOP, children=[Press_Cheese])
loop_Aging_Setup = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Setup, Humidity_Control, Temperature_Monitor])
loop_Order_Fulfill = OperatorPOWL(operator=Operator.LOOP, children=[Order_Fulfill, Retail_Deliver, Feedback_Collect])

xor_Milk_Pasteurize = OperatorPOWL(operator=Operator.XOR, children=[loop_Milk_Pasteurize, skip])
xor_Curd_Formation = OperatorPOWL(operator=Operator.XOR, children=[loop_Curd_Formation, skip])
xor_Mold_Inoculate = OperatorPOWL(operator=Operator.XOR, children=[loop_Mold_Inoculate, skip])
xor_Press_Cheese = OperatorPOWL(operator=Operator.XOR, children=[loop_Press_Cheese, skip])
xor_Aging_Setup = OperatorPOWL(operator=Operator.XOR, children=[loop_Aging_Setup, skip])
xor_Order_Fulfill = OperatorPOWL(operator=Operator.XOR, children=[loop_Order_Fulfill, skip])

root = StrictPartialOrder(nodes=[xor_Milk_Pasteurize, xor_Curd_Formation, xor_Mold_Inoculate, xor_Press_Cheese, xor_Aging_Setup, xor_Order_Fulfill])
root.order.add_edge(xor_Milk_Pasteurize, xor_Curd_Formation)
root.order.add_edge(xor_Curd_Formation, xor_Mold_Inoculate)
root.order.add_edge(xor_Mold_Inoculate, xor_Press_Cheese)
root.order.add_edge(xor_Press_Cheese, xor_Aging_Setup)
root.order.add_edge(xor_Aging_Setup, xor_Order_Fulfill)