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

# Define the process structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Collection, Quality_Testing, Milk_Blending, Starter_Culture, Fermentation_Check, Curd_Cutting, Whey_Separation, Molding_Press, Salting_Stage, Aging_Control, Packaging_Design])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Cold_Shipping, Compliance_Audit, Blockchain_Log, Market_Pricing, Order_Fulfillment, Feedback_Review])

# Create the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2])
root.order.add_edge(loop1, loop2)

# Print the root POWL model
print(root)