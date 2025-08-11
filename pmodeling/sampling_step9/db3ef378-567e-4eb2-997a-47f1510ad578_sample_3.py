import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions (tau labels)
skip = SilentTransition()

# Define the exclusive choice (XOR) between two transitions
xor = OperatorPOWL(operator=Operator.XOR, children=[MoldedCheese, skip])

# Define the loop node (* (A, B)): execute A, then choose to exit or execute B then A again, repeated until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[CulturePrep, CurdFormation])

# Define the POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Save the final result in the variable 'root'