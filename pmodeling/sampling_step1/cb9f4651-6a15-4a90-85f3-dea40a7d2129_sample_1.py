import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

MilkSourcing = Transition(label='Milk Sourcing')
CulturePrep = Transition(label='Culture Prep')
MilkPasteurize = Transition(label='Milk Pasteurize')
MilkInoculate = Transition(label='Milk Inoculate')
CurdFormation = Transition(label='Curd Formation')
CurdCut = Transition(label='Curd Cut')
WheyDrain = Transition(label='Whey Drain')
MoldInoculate = Transition(label='Mold Inoculate')
PressCheese = Transition(label='Press Cheese')
AgingSetup = Transition(label='Aging Setup')
HumidityControl = Transition(label='Humidity Control')
TemperatureMonitor = Transition(label='Temperature Monitor')
QualityTest = Transition(label='Quality Test')
Packaging = Transition(label='Packaging')
OrderFulfill = Transition(label='Order Fulfill')
RetailDeliver = Transition(label='Retail Deliver')
FeedbackCollect = Transition(label='Feedback Collect')

root = StrictPartialOrder(nodes=[
    MilkSourcing, CulturePrep, MilkPasteurize, MilkInoculate, CurdFormation, CurdCut, WheyDrain,
    MoldInoculate, PressCheese, AgingSetup, HumidityControl, TemperatureMonitor, QualityTest, Packaging,
    OrderFulfill, RetailDeliver, FeedbackCollect
])

root.order.add_edge(MilkSourcing, CulturePrep)
root.order.add_edge(CulturePrep, MilkPasteurize)
root.order.add_edge(MilkPasteurize, MilkInoculate)
root.order.add_edge(MilkInoculate, CurdFormation)
root.order.add_edge(CurdFormation, CurdCut)
root.order.add_edge(CurdCut, WheyDrain)
root.order.add_edge(WheyDrain, MoldInoculate)
root.order.add_edge(MoldInoculate, PressCheese)
root.order.add_edge(PressCheese, AgingSetup)
root.order.add_edge(AgingSetup, HumidityControl)
root.order.add_edge(HumidityControl, TemperatureMonitor)
root.order.add_edge(TemperatureMonitor, QualityTest)
root.order.add_edge(QualityTest, Packaging)
root.order.add_edge(Packaging, OrderFulfill)
root.order.add_edge(OrderFulfill, RetailDeliver)
root.order.add_edge(RetailDeliver, FeedbackCollect)