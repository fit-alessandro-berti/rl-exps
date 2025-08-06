import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Prep = Transition(label='Starter Prep')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Molding_Press = Transition(label='Molding Press')
Fermentation_Control = Transition(label='Fermentation Control')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Check = Transition(label='Humidity Check')
Packaging_Design = Transition(label='Packaging Design')
Label_Approval = Transition(label='Label Approval')
Inventory_Audit = Transition(label='Inventory Audit')
Order_Scheduling = Transition(label='Order Scheduling')
Market_Delivery = Transition(label='Market Delivery')
Feedback_Review = Transition(label='Feedback Review')
Compliance_Check = Transition(label='Compliance Check')
Marketing_Sync = Transition(label='Marketing Sync')

# Define silent transitions for choices and loops
skip = SilentTransition()
skip2 = SilentTransition()

# Define loops for repetitive activities
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Testing, Starter_Prep])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Curd_Cutting, Whey_Draining])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Molding_Press, Fermentation_Control])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Setup, Humidity_Check])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Packaging_Design, Label_Approval])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Inventory_Audit, Order_Scheduling])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[Market_Delivery, Feedback_Review])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[Compliance_Check, Marketing_Sync])

# Define exclusive choices for branching activities
xor1 = OperatorPOWL(operator=Operator.XOR, children=[skip, skip2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, skip2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[skip, skip2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[skip, skip2])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[skip, skip2])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[skip, skip2])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[skip, skip2])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[skip, skip2])

# Define partial order structure
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)
root.order.add_edge(loop5, xor5)
root.order.add_edge(loop6, xor6)
root.order.add_edge(loop7, xor7)
root.order.add_edge(loop8, xor8)