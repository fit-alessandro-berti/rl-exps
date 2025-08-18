import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

MilkSourcing = Transition(label='Milk Sourcing')
DietMonitoring = Transition(label='Diet Monitoring')
CultureSelection = Transition(label='Culture Selection')
MilkPasteurize = Transition(label='Milk Pasteurize')
CurdCutting = Transition(label='Curd Cutting')
WheyDraining = Transition(label='Whey Draining')
MoldInoculate = Transition(label='Mold Inoculate')
PressForming = Transition(label='Press Forming')
SaltApplication = Transition(label='Salt Application')
AgingSetup = Transition(label='Aging Setup')
HumidityControl = Transition(label='Humidity Control')
FlavorTesting = Transition(label='Flavor Testing')
PackagingDesign = Transition(label='Packaging Design')
OrderProcessing = Transition(label='Order Processing')
RetailDelivery = Transition(label='Retail Delivery')
EventCoordination = Transition(label='Event Coordination')
FeedbackReview = Transition(label='Feedback Review')

root = StrictPartialOrder(nodes=[
    MilkSourcing, DietMonitoring, CultureSelection, MilkPasteurize, CurdCutting,
    WheyDraining, MoldInoculate, PressForming, SaltApplication, AgingSetup,
    HumidityControl, FlavorTesting, PackagingDesign, OrderProcessing, RetailDelivery,
    EventCoordination, FeedbackReview
])

# Define dependencies for the process
root.order.add_edge(MilkSourcing, DietMonitoring)
root.order.add_edge(DietMonitoring, CultureSelection)
root.order.add_edge(CultureSelection, MilkPasteurize)
root.order.add_edge(MilkPasteurize, CurdCutting)
root.order.add_edge(CurdCutting, WheyDraining)
root.order.add_edge(WheyDraining, MoldInoculate)
root.order.add_edge(MoldInoculate, PressForming)
root.order.add_edge(PressForming, SaltApplication)
root.order.add_edge(SaltApplication, AgingSetup)
root.order.add_edge(AgingSetup, HumidityControl)
root.order.add_edge(HumidityControl, FlavorTesting)
root.order.add_edge(FlavorTesting, PackagingDesign)
root.order.add_edge(PackagingDesign, OrderProcessing)
root.order.add_edge(OrderProcessing, RetailDelivery)
root.order.add_edge(RetailDelivery, EventCoordination)
root.order.add_edge(EventCoordination, FeedbackReview)