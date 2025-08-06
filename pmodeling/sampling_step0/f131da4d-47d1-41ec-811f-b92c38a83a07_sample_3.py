import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
MilkSourcing = Transition(label='Milk Sourcing')
CultureSelection = Transition(label='Culture Selection')
MilkTesting = Transition(label='Milk Testing')
FermentationStart = Transition(label='Fermentation Start')
TemperatureControl = Transition(label='Temperature Control')
pHMonitoring = Transition(label='pH Monitoring')
CurdCutting = Transition(label='Curd Cutting')
WheyDraining = Transition(label='Whey Draining')
MoldingCheese = Transition(label='Molding Cheese')
SaltingProcess = Transition(label='Salting Process')
AgingSetup = Transition(label='Aging Setup')
QualityCheck = Transition(label='Quality Check')
PackagingPrep = Transition(label='Packaging Prep')
LabelDesign = Transition(label='Label Design')
DistributionPlan = Transition(label='Distribution Plan')
RetailDelivery = Transition(label='Retail Delivery')
CustomerFeedback = Transition(label='Customer Feedback')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    MilkSourcing,
    CultureSelection,
    MilkTesting,
    FermentationStart,
    TemperatureControl,
    pHMonitoring,
    CurdCutting,
    WheyDraining,
    MoldingCheese,
    SaltingProcess,
    AgingSetup,
    QualityCheck,
    PackagingPrep,
    LabelDesign,
    DistributionPlan,
    RetailDelivery,
    CustomerFeedback
])

# Define the dependencies (partial order)
root.order.add_edge(MilkSourcing, CultureSelection)
root.order.add_edge(CultureSelection, MilkTesting)
root.order.add_edge(MilkTesting, FermentationStart)
root.order.add_edge(FermentationStart, TemperatureControl)
root.order.add_edge(TemperatureControl, pHMonitoring)
root.order.add_edge(pHMonitoring, CurdCutting)
root.order.add_edge(CurdCutting, WheyDraining)
root.order.add_edge(WheyDraining, MoldingCheese)
root.order.add_edge(MoldingCheese, SaltingProcess)
root.order.add_edge(SaltingProcess, AgingSetup)
root.order.add_edge(AgingSetup, QualityCheck)
root.order.add_edge(QualityCheck, PackagingPrep)
root.order.add_edge(PackagingPrep, LabelDesign)
root.order.add_edge(LabelDesign, DistributionPlan)
root.order.add_edge(DistributionPlan, RetailDelivery)
root.order.add_edge(RetailDelivery, CustomerFeedback)

print(root)