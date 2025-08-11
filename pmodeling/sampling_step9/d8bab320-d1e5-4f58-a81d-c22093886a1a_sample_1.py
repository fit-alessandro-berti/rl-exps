import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

MilkSourcing = Transition(label='Milk Sourcing')
CultureSelection = Transition(label='Culture Selection')
MilkPasteurize = Transition(label='Milk Pasteurize')
CurdFormation = Transition(label='Curd Formation')
WheySeparation = Transition(label='Whey Separation')
MoldInoculate = Transition(label='Mold Inoculate')
CheesePressing = Transition(label='Cheese Pressing')
AgingSetup = Transition(label='Aging Setup')
HumidityControl = Transition(label='Humidity Control')
FlavorTesting = Transition(label='Flavor Testing')
PackagingDesign = Transition(label='Packaging Design')
LabelApproval = Transition(label='Label Approval')
OrderForecast = Transition(label='Order Forecast')
RegulationAudit = Transition(label='Regulation Audit')
WasteRecycling = Transition(label='Waste Recycling')
MarketDelivery = Transition(label='Market Delivery')
CustomerFeedback = Transition(label='Customer Feedback')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[MilkSourcing, CultureSelection])
xor = OperatorPOWL(operator=Operator.XOR, children=[CheesePressing, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)