from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
MilkCollection = Transition(label='Milk Collection')
CulturePrep = Transition(label='Culture Prep')
CurdFormation = Transition(label='Curd Formation')
WheySeparation = Transition(label='Whey Separation')
MoldingCheese = Transition(label='Molding Cheese')
SaltingProcess = Transition(label='Salting Process')
InitialAging = Transition(label='Initial Aging')
HumidityControl = Transition(label='Humidity Control')
TemperatureCheck = Transition(label='Temperature Check')
FlavorTesting = Transition(label='Flavor Testing')
FinalAging = Transition(label='Final Aging')
PackagingArtisanal = Transition(label='Packaging Artisanal')
LabelPrinting = Transition(label='Label Printing')
InventoryAudit = Transition(label='Inventory Audit')
OrderFulfillment = Transition(label='Order Fulfillment')
SubscriptionSetup = Transition(label='Subscription Setup')
EventMarketing = Transition(label='Event Marketing')

# Define silent activities
skip = SilentTransition()

# Define loops
initialAgingLoop = OperatorPOWL(operator=Operator.LOOP, children=[HumidityControl, TemperatureCheck, FlavorTesting])
finalAgingLoop = OperatorPOWL(operator=Operator.LOOP, children=[FinalAging])

# Define choices
culturePrepChoice = OperatorPOWL(operator=Operator.XOR, children=[CulturePrep, skip])
moldingCheeseChoice = OperatorPOWL(operator=Operator.XOR, children=[MoldingCheese, skip])

# Define POWL model
root = StrictPartialOrder(nodes=[MilkCollection, CulturePrepChoice, CurdFormation, WheySeparation, MoldCheeseChoice, SaltingProcess, InitialAgingLoop, PackagingArtisanal, LabelPrinting, InventoryAudit, OrderFulfillment, SubscriptionSetup, EventMarketing, FinalAgingLoop])
root.order.add_edge(MilkCollection, CulturePrepChoice)
root.order.add_edge(CulturePrepChoice, CurdFormation)
root.order.add_edge(CurdFormation, WheySeparation)
root.order.add_edge(WheySeparation, MoldCheeseChoice)
root.order.add_edge(MoldingCheeseChoice, SaltingProcess)
root.order.add_edge(SaltingProcess, InitialAgingLoop)
root.order.add_edge(InitialAgingLoop, PackagingArtisanal)
root.order.add_edge(PackagingArtisanal, LabelPrinting)
root.order.add_edge(LabelPrinting, InventoryAudit)
root.order.add_edge(InventoryAudit, OrderFulfillment)
root.order.add_edge(OrderFulfillment, SubscriptionSetup)
root.order.add_edge(SubscriptionSetup, EventMarketing)
root.order.add_edge(EventMarketing, FinalAgingLoop)
root.order.add_edge(FinalAgingLoop, FinalAging)
root.order.add_edge(FinalAging, PackagingArtisanal)

# Print the POWL model
print(root)