import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

MilkSourcing = Transition(label='Milk Sourcing')
QualityTesting = Transition(label='Quality Testing')
StarterCulture = Transition(label='Starter Culture')
MilkPasteurize = Transition(label='Milk Pasteurize')
CurdCutting = Transition(label='Curd Cutting')
WheyDraining = Transition(label='Whey Draining')
PressingCheese = Transition(label='Pressing Cheese')
SaltingStage = Transition(label='Salting Stage')
Fermentation = Transition(label='Fermentation')
AgingControl = Transition(label='Aging Control')
FlavorTasting = Transition(label='Flavor Tasting')
PackagingArtisanal = Transition(label='Packaging Artisanal')
LabelPrinting = Transition(label='Label Printing')
OrderProcessing = Transition(label='Order Processing')
DirectDelivery = Transition(label='Direct Delivery')
CustomerFeedback = Transition(label='Customer Feedback')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[MilkSourcing, QualityTesting, StarterCulture, MilkPasteurize, CurdCutting, WheyDraining, PressingCheese, SaltingStage, Fermentation, AgingControl, FlavorTasting, PackagingArtisanal, LabelPrinting])
xor = OperatorPOWL(operator=Operator.XOR, children=[OrderProcessing, DirectDelivery])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[CustomerFeedback, skip])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor, xor2])
root = StrictPartialOrder(nodes=[loop, loop2])
root.order.add_edge(loop, loop2)