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

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Sourcing, Curd_Formation, Microbial_Test, Whey_Removal])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Pressing_Cheese, Salt_Application, Aging_Control, Quality_Check])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Eco_Packaging, Inventory_Log, Temp_Monitoring])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Carrier_Booking, Trace_Recording])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Review, Compliance_Audit, Batch_Adjustment])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, skip])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)