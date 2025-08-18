from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Milk_Collection,
    Quality_Testing,
    Milk_Blending,
    Starter_Culture,
    Fermentation_Check,
    Curd_Cutting,
    Whey_Separation,
    Molding_Press,
    Salting_Stage,
    Aging_Control,
    Packaging_Design,
    Cold_Shipping,
    Compliance_Audit,
    Blockchain_Log,
    Market_Pricing,
    Order_Fulfillment,
    Feedback_Review
])

# Define the partial order dependencies
root.order.add_edge(Milk_Collection, Quality_Testing)
root.order.add_edge(Quality_Testing, Milk_Blending)
root.order.add_edge(Milk_Blending, Starter_Culture)
root.order.add_edge(Starter_Culture, Fermentation_Check)
root.order.add_edge(Fermentation_Check, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Whey_Separation)
root.order.add_edge(Whey_Separation, Molding_Press)
root.order.add_edge(Molding_Press, Salting_Stage)
root.order.add_edge(Salting_Stage, Aging_Control)
root.order.add_edge(Aging_Control, Packaging_Design)
root.order.add_edge(Packaging_Design, Cold_Shipping)
root.order.add_edge(Cold_Shipping, Compliance_Audit)
root.order.add_edge(Compliance_Audit, Blockchain_Log)
root.order.add_edge(Blockchain_Log, Market_Pricing)
root.order.add_edge(Market_Pricing, Order_Fulfillment)
root.order.add_edge(Order_Fulfillment, Feedback_Review)

# Print the final POWL model
print(root)