from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
MilkSourcing = Transition(label='Milk Sourcing')
QualityTesting = Transition(label='Quality Testing')
CulturePrep = Transition(label='Culture Prep')
MilkPasteurize = Transition(label='Milk Pasteurize')
CurdCutting = Transition(label='Curd Cutting')
WheyDraining = Transition(label='Whey Draining')
MoldingCheese = Transition(label='Molding Cheese')
PressingBlocks = Transition(label='Pressing Blocks')
SaltingProcess = Transition(label='Salting Process')
AgingMonitoring = Transition(label='Aging Monitoring')
FlavorProfiling = Transition(label='Flavor Profiling')
PackagingDesign = Transition(label='Packaging Design')
ComplianceCheck = Transition(label='Compliance Check')
MarketResearch = Transition(label='Market Research')
DirectShipping = Transition(label='Direct Shipping')
CustomerFeedback = Transition(label='Customer Feedback')
RecipeAdjust = Transition(label='Recipe Adjust')

# Define the partial order
root = StrictPartialOrder(nodes=[
    MilkSourcing, QualityTesting, CulturePrep, MilkPasteurize, CurdCutting, WheyDraining, MoldingCheese,
    PressingBlocks, SaltingProcess, AgingMonitoring, FlavorProfiling, PackagingDesign, ComplianceCheck,
    MarketResearch, DirectShipping, CustomerFeedback, RecipeAdjust
])

# Define the order between the nodes
root.order.add_edge(MilkSourcing, QualityTesting)
root.order.add_edge(QualityTesting, CulturePrep)
root.order.add_edge(CulturePrep, MilkPasteurize)
root.order.add_edge(MilkPasteurize, CurdCutting)
root.order.add_edge(CurdCutting, WheyDraining)
root.order.add_edge(WheyDraining, MoldingCheese)
root.order.add_edge(MoldingCheese, PressingBlocks)
root.order.add_edge(PressingBlocks, SaltingProcess)
root.order.add_edge(SaltingProcess, AgingMonitoring)
root.order.add_edge(AgingMonitoring, FlavorProfiling)
root.order.add_edge(FlavorProfiling, PackagingDesign)
root.order.add_edge(PackagingDesign, ComplianceCheck)
root.order.add_edge(ComplianceCheck, MarketResearch)
root.order.add_edge(MarketResearch, DirectShipping)
root.order.add_edge(DirectShipping, CustomerFeedback)
root.order.add_edge(CustomerFeedback, RecipeAdjust)

# Print the root
print(root)