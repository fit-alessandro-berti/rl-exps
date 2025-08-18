from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define silent transitions
Skip = SilentTransition()

# Define loops and exclusive choices
cultureLoop = OperatorPOWL(operator=Operator.LOOP, children=[CulturePrep, Skip])
agingLoop = OperatorPOWL(operator=Operator.LOOP, children=[AgingMonitoring, Skip])
marketResearchLoop = OperatorPOWL(operator=Operator.LOOP, children=[MarketResearch, Skip])
customerFeedbackLoop = OperatorPOWL(operator=Operator.LOOP, children=[CustomerFeedback, Skip])

# Define exclusive choices
qualityTestingChoice = OperatorPOWL(operator=Operator.XOR, children=[QualityTesting, Skip])

# Define partial order
root = StrictPartialOrder(nodes=[MilkSourcing, qualityTestingChoice, MilkPasteurize, CurdCutting, WheyDraining, MoldingCheese, PressingBlocks, SaltingProcess, agingLoop, FlavorProfiling, PackagingDesign, ComplianceCheck, marketResearchLoop, DirectShipping, customerFeedbackLoop, RecipeAdjust])
root.order.add_edge(MilkSourcing, qualityTestingChoice)
root.order.add_edge(qualityTestingChoice, MilkPasteurize)
root.order.add_edge(MilkPasteurize, CurdCutting)
root.order.add_edge(CurdCutting, WheyDraining)
root.order.add_edge(WheyDraining, MoldingCheese)
root.order.add_edge(MoldingCheese, PressingBlocks)
root.order.add_edge(PressingBlocks, SaltingProcess)
root.order.add_edge(SaltingProcess, agingLoop)
root.order.add_edge(agingLoop, FlavorProfiling)
root.order.add_edge(FlavorProfiling, PackagingDesign)
root.order.add_edge(PackagingDesign, ComplianceCheck)
root.order.add_edge(ComplianceCheck, marketResearchLoop)
root.order.add_edge(marketResearchLoop, DirectShipping)
root.order.add_edge(DirectShipping, customerFeedbackLoop)
root.order.add_edge(customerFeedbackLoop, RecipeAdjust)