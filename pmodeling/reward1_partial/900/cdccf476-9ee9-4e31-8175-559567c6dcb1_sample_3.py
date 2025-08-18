from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define the process structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Sourcing, Curd_Formation, Microbial_Test, Whey_Removal, Pressing_Cheese, Salt_Application, Aging_Control, Quality_Check, Eco_Packaging])
xor = OperatorPOWL(operator=Operator.XOR, children=[Inventory_Log, Temp_Monitoring, Carrier_Booking])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Trace_Recording, Feedback_Review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Compliance_Audit, Batch_Adjustment])

# Define the partial order
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)

# Print the root to verify
print(root)