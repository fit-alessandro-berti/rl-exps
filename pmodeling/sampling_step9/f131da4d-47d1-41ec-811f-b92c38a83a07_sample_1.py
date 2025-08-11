import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[MilkSourcing, CultureSelection, MilkTesting, FermentationStart, TemperatureControl, pHMonitoring, CurdCutting, WheyDraining, MoldingCheese, SaltingProcess, AgingSetup, QualityCheck, PackagingPrep, LabelDesign, DistributionPlan, RetailDelivery, CustomerFeedback])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, CustomerFeedback])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)