import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
MilkSourcing = Transition(label='Milk Sourcing')
CurdPreparation = Transition(label='Curd Preparation')
starterCulture = Transition(label='starter Culture')
TemperatureControl = Transition(label='Temperature Control')
PressingCheese = Transition(label='Pressing Cheese')
SaltingStage = Transition(label='Salting Stage')
AgingProcess = Transition(label='Aging Process')
MicrobialTest = Transition(label='Microbial Test')
QualityCheck = Transition(label='Quality Check')
EcoPackaging = Transition(label='Eco Packaging')
LabelPrinting = Transition(label='Label Printing')
InventoryAudit = Transition(label='Inventory Audit')
OrderProcessing = Transition(label='Order Processing')
RetailShipping = Transition(label='Retail Shipping')
CustomerFeedback = Transition(label='Customer Feedback')
RecipeUpdate = Transition(label='Recipe Update')
MarketAnalysis = Transition(label='Market Analysis')

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
loopAging = OperatorPOWL(operator=Operator.LOOP, children=[AgingProcess])
loopQualityCheck = OperatorPOWL(operator=Operator.LOOP, children=[QualityCheck])
loopMicrobialTest = OperatorPOWL(operator=Operator.LOOP, children=[MicrobialTest])
loopInventoryAudit = OperatorPOWL(operator=Operator.LOOP, children=[InventoryAudit])
loopOrderProcessing = OperatorPOWL(operator=Operator.LOOP, children=[OrderProcessing])
loopRetailShipping = OperatorPOWL(operator=Operator.LOOP, children=[RetailShipping])
loopCustomerFeedback = OperatorPOWL(operator=Operator.LOOP, children=[CustomerFeedback])
loopRecipeUpdate = OperatorPOWL(operator=Operator.LOOP, children=[RecipeUpdate])
loopMarketAnalysis = OperatorPOWL(operator=Operator.LOOP, children=[MarketAnalysis])

root = StrictPartialOrder(nodes=[
    MilkSourcing, CurdPreparation, starterCulture, TemperatureControl, PressingCheese, SaltingStage,
    loopAging, loopQualityCheck, loopMicrobialTest, loopInventoryAudit, loopOrderProcessing,
    loopRetailShipping, loopCustomerFeedback, loopRecipeUpdate, loopMarketAnalysis,
    EcoPackaging, LabelPrinting, QualityCheck, MicrobialTest, InventoryAudit, OrderProcessing,
    RetailShipping, CustomerFeedback, RecipeUpdate, MarketAnalysis
])

# Define the partial order relationships
root.order.add_edge(MilkSourcing, CurdPreparation)
root.order.add_edge(CurdPreparation, starterCulture)
root.order.add_edge(starterCulture, TemperatureControl)
root.order.add_edge(TemperatureControl, PressingCheese)
root.order.add_edge(PressingCheese, SaltingStage)
root.order.add_edge(SaltingStage, AgingProcess)
root.order.add_edge(AgingProcess, loopAging)
root.order.add_edge(loopAging, AgingProcess)
root.order.add_edge(AgingProcess, loopQualityCheck)
root.order.add_edge(loopQualityCheck, AgingProcess)
root.order.add_edge(AgingProcess, loopMicrobialTest)
root.order.add_edge(loopMicrobialTest, AgingProcess)
root.order.add_edge(AgingProcess, loopInventoryAudit)
root.order.add_edge(loopInventoryAudit, AgingProcess)
root.order.add_edge(AgingProcess, loopOrderProcessing)
root.order.add_edge(loopOrderProcessing, AgingProcess)
root.order.add_edge(AgingProcess, loopRetailShipping)
root.order.add_edge(loopRetailShipping, AgingProcess)
root.order.add_edge(AgingProcess, loopCustomerFeedback)
root.order.add_edge(loopCustomerFeedback, AgingProcess)
root.order.add_edge(AgingProcess, loopRecipeUpdate)
root.order.add_edge(loopRecipeUpdate, AgingProcess)
root.order.add_edge(AgingProcess, loopMarketAnalysis)
root.order.add_edge(loopMarketAnalysis, AgingProcess)
root.order.add_edge(loopAging, EcoPackaging)
root.order.add_edge(EcoPackaging, LabelPrinting)
root.order.add_edge(LabelPrinting, QualityCheck)
root.order.add_edge(QualityCheck, MicrobialTest)
root.order.add_edge(MicrobialTest, InventoryAudit)
root.order.add_edge(InventoryAudit, OrderProcessing)
root.order.add_edge(OrderProcessing, RetailShipping)
root.order.add_edge(RetailShipping, CustomerFeedback)
root.order.add_edge(CustomerFeedback, RecipeUpdate)
root.order.add_edge(RecipeUpdate, MarketAnalysis)
root.order.add_edge(MarketAnalysis, loopRecipeUpdate)

# Print the root node
print(root)