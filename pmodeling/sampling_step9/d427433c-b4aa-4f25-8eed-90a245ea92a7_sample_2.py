import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
Milk_Collection = Transition(label='Milk Collection')
Quality_Testing = Transition(label='Quality Testing')
Milk_Blending = Transition(label='Milk Blending')
Starter_Culture = Transition(label='Starter Culture')
Fermentation_Check = Transition(label='Fermentation Check')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Separation = Transition(label='Whey Separation')
Molding_Press = Transition(label='Molding Press')
Salting_Stage = Transition(label='Salting Stage')
Aging_Control = Transition(label='Aging Control')
Packaging_Design = Transition(label='Packaging Design')
Cold_Shipping = Transition(label='Cold Shipping')
Compliance_Audit = Transition(label='Compliance Audit')
Blockchain_Log = Transition(label='Blockchain Log')
Market_Pricing = Transition(label='Market Pricing')
Order_Fulfillment = Transition(label='Order Fulfillment')
Feedback_Review = Transition(label='Feedback Review')

# Define the silent transitions
skip = SilentTransition()

# Define the partial order nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Collection, Quality_Testing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Blending, Starter_Culture])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Fermentation_Check, Curd_Cutting])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Whey_Separation, Molding_Press])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Salting_Stage, Aging_Control])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Packaging_Design, Cold_Shipping])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[Compliance_Audit, Blockchain_Log])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[Market_Pricing, Order_Fulfillment])
loop9 = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Review, skip])

# Define the XOR node
xor = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8, loop9])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)
root.order.add_edge(loop3, xor)
root.order.add_edge(loop4, xor)
root.order.add_edge(loop5, xor)
root.order.add_edge(loop6, xor)
root.order.add_edge(loop7, xor)
root.order.add_edge(loop8, xor)
root.order.add_edge(loop9, xor)

# Save the final result in the variable 'root'