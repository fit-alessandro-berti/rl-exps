import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition with its label
MilkSourcing = Transition(label='Milk Sourcing')
CurdPreparation = Transition(label='Curd Preparation')
StarterCulture = Transition(label='starter Culture')
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

# Define the partial order workflow
root = StrictPartialOrder(nodes=[
    MilkSourcing, CurdPreparation, StarterCulture, TemperatureControl, PressingCheese, SaltingStage, AgingProcess, MicrobialTest, QualityCheck, EcoPackaging, LabelPrinting, InventoryAudit, OrderProcessing, RetailShipping, CustomerFeedback, RecipeUpdate, MarketAnalysis
])

# Define the dependencies between activities
root.order.add_edge(MilkSourcing, CurdPreparation)
root.order.add_edge(CurdPreparation, StarterCulture)
root.order.add_edge(StarterCulture, TemperatureControl)
root.order.add_edge(TemperatureControl, PressingCheese)
root.order.add_edge(PressingCheese, SaltingStage)
root.order.add_edge(SaltingStage, AgingProcess)
root.order.add_edge(AgingProcess, MicrobialTest)
root.order.add_edge(MicrobialTest, QualityCheck)
root.order.add_edge(QualityCheck, EcoPackaging)
root.order.add_edge(EcoPackaging, LabelPrinting)
root.order.add_edge(LabelPrinting, InventoryAudit)
root.order.add_edge(InventoryAudit, OrderProcessing)
root.order.add_edge(OrderProcessing, RetailShipping)
root.order.add_edge(RetailShipping, CustomerFeedback)
root.order.add_edge(CustomerFeedback, RecipeUpdate)
root.order.add_edge(RecipeUpdate, MarketAnalysis)

# The final result is stored in the variable 'root'