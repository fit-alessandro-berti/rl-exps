import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

MilkSourcing = Transition(label='Milk Sourcing')
QualityTesting = Transition(label='Quality Testing')
StarterCulture = Transition(label='Starter Culture')
MilkFermentation = Transition(label='Milk Fermentation')
CurdCutting = Transition(label='Curd Cutting')
WheyDraining = Transition(label='Whey Draining')
PressingCheese = Transition(label='Pressing Cheese')
CaveAging = Transition(label='Cave Aging')
SampleTasting = Transition(label='Sample Tasting')
FlavorProfiling = Transition(label='Flavor Profiling')
PackagingDesign = Transition(label='Packaging Design')
ColdStorage = Transition(label='Cold Storage')
LogisticsPlanning = Transition(label='Logistics Planning')
PopUpSales = Transition(label='Pop-up Sales')
CustomerFeedback = Transition(label='Customer Feedback')
RecipeAdjusting = Transition(label='Recipe Adjusting')

root = StrictPartialOrder(nodes=[
    MilkSourcing, QualityTesting, StarterCulture, MilkFermentation, CurdCutting, WheyDraining, PressingCheese,
    CaveAging, SampleTasting, FlavorProfiling, PackagingDesign, ColdStorage, LogisticsPlanning, PopUpSales,
    CustomerFeedback, RecipeAdjusting
])

root.order.add_edge(MilkSourcing, QualityTesting)
root.order.add_edge(QualityTesting, StarterCulture)
root.order.add_edge(StarterCulture, MilkFermentation)
root.order.add_edge(MilkFermentation, CurdCutting)
root.order.add_edge(CurdCutting, WheyDraining)
root.order.add_edge(WheyDraining, PressingCheese)
root.order.add_edge(PressingCheese, CaveAging)
root.order.add_edge(CaveAging, SampleTasting)
root.order.add_edge(SampleTasting, FlavorProfiling)
root.order.add_edge(FlavorProfiling, PackagingDesign)
root.order.add_edge(PackagingDesign, ColdStorage)
root.order.add_edge(ColdStorage, LogisticsPlanning)
root.order.add_edge(LogisticsPlanning, PopUpSales)
root.order.add_edge(PopUpSales, CustomerFeedback)
root.order.add_edge(CustomerFeedback, RecipeAdjusting)