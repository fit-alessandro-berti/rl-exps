import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the workflow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[CulturePrep, CurdFormation, WheySeparation, MoldingCheese, SaltingProcess, InitialAging, HumidityControl, TemperatureCheck, FlavorTesting, FinalAging])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[InventoryAudit, OrderFulfillment])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[SubscriptionSetup, EventMarketing])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[LabelPrinting, PackagingArtisanal])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[MilkCollection, xor1, xor2, xor3])

# Define the root
root = StrictPartialOrder(nodes=[loop1, xor1, xor2, xor3, xor4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)

# Print the root
print(root)