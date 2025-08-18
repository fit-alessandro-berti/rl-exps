import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define nodes for each step
step1 = StrictPartialOrder(nodes=[Milk_Collection, Quality_Testing, Milk_Blending, Starter_Culture])
step2 = StrictPartialOrder(nodes=[Fermentation_Check, Curd_Cutting, Whey_Separation, Molding_Press, Salting_Stage])
step3 = StrictPartialOrder(nodes=[Aging_Control, Packaging_Design])
step4 = StrictPartialOrder(nodes=[Cold_Shipping, Compliance_Audit])
step5 = StrictPartialOrder(nodes=[Blockchain_Log, Market_Pricing])
step6 = StrictPartialOrder(nodes=[Order_Fulfillment, Feedback_Review])

# Define partial order relationships
root = StrictPartialOrder(nodes=[step1, step2, step3, step4, step5, step6])

# Add dependencies between steps
root.order.add_edge(step1, step2)
root.order.add_edge(step2, step3)
root.order.add_edge(step3, step4)
root.order.add_edge(step4, step5)
root.order.add_edge(step5, step6)

# Add dependencies between steps and feedback review
root.order.add_edge(step6, Feedback_Review)

# Print the root model
print(root)