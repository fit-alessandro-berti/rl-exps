import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

root = StrictPartialOrder(nodes=[
    MilkSourcing,
    CurdPreparation,
    starterCulture,
    TemperatureControl,
    PressingCheese,
    SaltingStage,
    AgingProcess,
    MicrobialTest,
    QualityCheck,
    EcoPackaging,
    LabelPrinting,
    InventoryAudit,
    OrderProcessing,
    RetailShipping,
    CustomerFeedback,
    RecipeUpdate,
    MarketAnalysis
])