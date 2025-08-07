import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Milk_Sourcing = Transition(label='Milk Sourcing')
Curd_Formation = Transition(label='Curd Formation')
Microbial_Test = Transition(label='Microbial Test')
Whey_Removal = Transition(label='Whey Removal')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salt_Application = Transition(label='Salt Application')
Aging_Control = Transition(label='Aging Control')
Quality_Check = Transition(label='Quality Check')
Eco_Packaging = Transition(label='Eco Packaging')
Inventory_Log = Transition(label='Inventory Log')
Temp_Monitoring = Transition(label='Temp Monitoring')
Carrier_Booking = Transition(label='Carrier Booking')
Trace_Recording = Transition(label='Trace Recording')
Feedback_Review = Transition(label='Feedback Review')
Compliance_Audit = Transition(label='Compliance Audit')
Batch_Adjustment = Transition(label='Batch Adjustment')

# Choices and Loops
choice1 = OperatorPOWL(operator=Operator.XOR, children=[Microbial_Test, SilentTransition()])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[Pressing_Cheese, Salt_Application])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[Quality_Check, SilentTransition()])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[Eco_Packaging, SilentTransition()])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[Inventory_Log, Temp_Monitoring])
choice6 = OperatorPOWL(operator=Operator.XOR, children=[Carrier_Booking, SilentTransition()])
choice7 = OperatorPOWL(operator=Operator.XOR, children=[Trace_Recording, Feedback_Review])
choice8 = OperatorPOWL(operator=Operator.XOR, children=[Compliance_Audit, Batch_Adjustment])

# Loop and Partial Order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Whey_Removal, Aging_Control])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[choice1, choice2])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[choice3, choice4])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[choice5, choice6])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[choice7, choice8])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[loop1, loop2])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[loop3, loop4])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[loop5, loop6])

root = StrictPartialOrder(nodes=[loop8, loop7, loop6, loop5, loop4, loop3, loop2, loop1])
root.order.add_edge(loop8, loop7)
root.order.add_edge(loop7, loop6)
root.order.add_edge(loop6, loop5)
root.order.add_edge(loop5, loop4)
root.order.add_edge(loop4, loop3)
root.order.add_edge(loop3, loop2)
root.order.add_edge(loop2, loop1)
root.order.add_edge(loop1, loop8)

print(root)