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

skip = SilentTransition()

# Define the process model using POWL
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Sourcing, Curd_Formation])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Microbial_Test, Whey_Removal])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Pressing_Cheese, Salt_Application])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Control, Quality_Check])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Eco_Packaging, Inventory_Log])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Temp_Monitoring, Carrier_Booking])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[Trace_Recording, Feedback_Review])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[Compliance_Audit, Batch_Adjustment])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop6, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[loop7, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[loop8, skip])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)

print(root)