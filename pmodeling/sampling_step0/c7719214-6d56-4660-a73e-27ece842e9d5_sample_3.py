import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define exclusive choice for aging setup
xorAgingSetup = OperatorPOWL(operator=Operator.XOR, children=[AgingSetup, skip])

# Define loop for culture selection
loopCultureSelection = OperatorPOWL(operator=Operator.LOOP, children=[CultureSelection, xorAgingSetup])

# Define exclusive choice for flavor testing
xorFlavorTesting = OperatorPOWL(operator=Operator.XOR, children=[FlavorTesting, skip])

# Define exclusive choice for packaging design
xorPackagingDesign = OperatorPOWL(operator=Operator.XOR, children=[PackagingDesign, skip])

# Define exclusive choice for event coordination
xorEventCoordination = OperatorPOWL(operator=Operator.XOR, children=[EventCoordination, skip])

# Define exclusive choice for order processing
xorOrderProcessing = OperatorPOWL(operator=Operator.XOR, children=[OrderProcessing, skip])

# Define exclusive choice for retail delivery
xorRetailDelivery = OperatorPOWL(operator=Operator.XOR, children=[RetailDelivery, skip])

# Define exclusive choice for feedback review
xorFeedbackReview = OperatorPOWL(operator=Operator.XOR, children=[FeedbackReview, skip])

# Define exclusive choice for milk sourcing
xorMilkSourcing = OperatorPOWL(operator=Operator.XOR, children=[MilkSourcing, skip])

# Define exclusive choice for diet monitoring
xorDietMonitoring = OperatorPOWL(operator=Operator.XOR, children=[DietMonitoring, skip])

# Define exclusive choice for milk pasteurize
xorMilkPasteurize = OperatorPOWL(operator=Operator.XOR, children=[MilkPasteurize, skip])

# Define exclusive choice for curd cutting
xorCurdCutting = OperatorPOWL(operator=Operator.XOR, children=[CurdCutting, skip])

# Define exclusive choice for whey draining
xorWheyDraining = OperatorPOWL(operator=Operator.XOR, children=[WheyDraining, skip])

# Define exclusive choice for mold inoculate
xorMoldInoculate = OperatorPOWL(operator=Operator.XOR, children=[MoldInoculate, skip])

# Define exclusive choice for press forming
xorPressForming = OperatorPOWL(operator=Operator.XOR, children=[PressForming, skip])

# Define exclusive choice for salt application
xorSaltApplication = OperatorPOWL(operator=Operator.XOR, children=[SaltApplication, skip])

# Define exclusive choice for humidity control
xorHumidityControl = OperatorPOWL(operator=Operator.XOR, children=[HumidityControl, skip])

# Define root process
root = StrictPartialOrder(nodes=[
    xorCultureSelection,
    xorFlavorTesting,
    xorPackagingDesign,
    xorEventCoordination,
    xorOrderProcessing,
    xorRetailDelivery,
    xorFeedbackReview,
    xorMilkSourcing,
    xorDietMonitoring,
    xorMilkPasteurize,
    xorCurdCutting,
    xorWheyDraining,
    xorMoldInoculate,
    xorPressForming,
    xorSaltApplication,
    xorHumidityControl,
    xorAgingSetup
])
root.order.add_edge(xorCultureSelection, xorFlavorTesting)
root.order.add_edge(xorFlavorTesting, xorPackagingDesign)
root.order.add_edge(xorPackagingDesign, xorEventCoordination)
root.order.add_edge(xorEventCoordination, xorOrderProcessing)
root.order.add_edge(xorOrderProcessing, xorRetailDelivery)
root.order.add_edge(xorRetailDelivery, xorFeedbackReview)
root.order.add_edge(xorFeedbackReview, xorMilkSourcing)
root.order.add_edge(xorMilkSourcing, xorDietMonitoring)
root.order.add_edge(xorDietMonitoring, xorMilkPasteurize)
root.order.add_edge(xorMilkPasteurize, xorCurdCutting)
root.order.add_edge(xorCurdCutting, xorWheyDraining)
root.order.add_edge(xorWheyDraining, xorMoldInoculate)
root.order.add_edge(xorMoldInoculate, xorPressForming)
root.order.add_edge(xorPressForming, xorSaltApplication)
root.order.add_edge(xorSaltApplication, xorHumidityControl)
root.order.add_edge(xorHumidityControl, xorAgingSetup)