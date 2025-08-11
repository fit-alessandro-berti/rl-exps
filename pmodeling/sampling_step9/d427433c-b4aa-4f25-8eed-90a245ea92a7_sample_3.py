import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Collection, Quality_Testing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Blending, Starter_Culture])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Fermentation_Check, Curd_Cutting])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Whey_Separation, Molding_Press])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Salting_Stage, Aging_Control])

# Define partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, Packaging_Design, Cold_Shipping, Compliance_Audit, Blockchain_Log, Market_Pricing, Order_Fulfillment, Feedback_Review])
root.order.add_edge(loop1, Packaging_Design)
root.order.add_edge(loop2, Packaging_Design)
root.order.add_edge(loop3, Packaging_Design)
root.order.add_edge(loop4, Packaging_Design)
root.order.add_edge(loop5, Packaging_Design)
root.order.add_edge(Packaging_Design, Cold_Shipping)
root.order.add_edge(Cold_Shipping, Compliance_Audit)
root.order.add_edge(Compliance_Audit, Blockchain_Log)
root.order.add_edge(Blockchain_Log, Market_Pricing)
root.order.add_edge(Market_Pricing, Order_Fulfillment)
root.order.add_edge(Order_Fulfillment, Feedback_Review)
root.order.add_edge(Feedback_Review, loop1)
root.order.add_edge(Feedback_Review, loop2)
root.order.add_edge(Feedback_Review, loop3)
root.order.add_edge(Feedback_Review, loop4)
root.order.add_edge(Feedback_Review, loop5)

print(root)