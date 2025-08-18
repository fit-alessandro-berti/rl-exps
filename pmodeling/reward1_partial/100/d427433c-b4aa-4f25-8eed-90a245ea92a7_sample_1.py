import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
MilkCollection = Transition(label='Milk Collection')
QualityTesting = Transition(label='Quality Testing')
MilkBlending = Transition(label='Milk Blending')
StarterCulture = Transition(label='Starter Culture')
FermentationCheck = Transition(label='Fermentation Check')
CurdCutting = Transition(label='Curd Cutting')
WheySeparation = Transition(label='Whey Separation')
MoldingPress = Transition(label='Molding Press')
SaltingStage = Transition(label='Salting Stage')
AgingControl = Transition(label='Aging Control')
PackagingDesign = Transition(label='Packaging Design')
ColdShipping = Transition(label='Cold Shipping')
ComplianceAudit = Transition(label='Compliance Audit')
BlockchainLog = Transition(label='Blockchain Log')
MarketPricing = Transition(label='Market Pricing')
OrderFulfillment = Transition(label='Order Fulfillment')
FeedbackReview = Transition(label='Feedback Review')

# Define the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[MilkCollection, QualityTesting])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[MilkBlending, StarterCulture, FermentationCheck])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[CurdCutting, WheySeparation])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[MoldingPress, SaltingStage])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[AgingControl, PackagingDesign])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ColdShipping, ComplianceAudit])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[BlockchainLog, MarketPricing])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[OrderFulfillment, FeedbackReview])

# Construct the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, xor1, xor2, xor3, xor4, xor5, xor6])

# Define the dependencies
root.order.add_edge(loop1, QualityTesting)
root.order.add_edge(loop2, MilkBlending)
root.order.add_edge(loop2, StarterCulture)
root.order.add_edge(loop2, FermentationCheck)
root.order.add_edge(xor1, CurdCutting)
root.order.add_edge(xor1, WheySeparation)
root.order.add_edge(xor2, MoldingPress)
root.order.add_edge(xor2, SaltingStage)
root.order.add_edge(xor3, AgingControl)
root.order.add_edge(xor3, PackagingDesign)
root.order.add_edge(xor4, ColdShipping)
root.order.add_edge(xor4, ComplianceAudit)
root.order.add_edge(xor5, BlockchainLog)
root.order.add_edge(xor5, MarketPricing)
root.order.add_edge(xor6, OrderFulfillment)
root.order.add_edge(xor6, FeedbackReview)

# Ensure all nodes are connected
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor1)

print(root)