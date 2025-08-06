import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
MilkSourcing = Transition(label='Milk Sourcing')
QualityTesting = Transition(label='Quality Testing')
BatchSelection = Transition(label='Batch Selection')
CurdPreparation = Transition(label='Curd Preparation')
PressingCheese = Transition(label='Pressing Cheese')
AgingControl = Transition(label='Aging Control')
FlavorProfiling = Transition(label='Flavor Profiling')
PackagingPrep = Transition(label='Packaging Prep')
ClimatePacking = Transition(label='Climate Packing')
ExportLicensing = Transition(label='Export Licensing')
CustomsFiling = Transition(label='Customs Filing')
FreightBooking = Transition(label='Freight Booking')
ColdStorage = Transition(label='Cold Storage')
TransportTracking = Transition(label='Transport Tracking')
RetailDelivery = Transition(label='Retail Delivery')
FeedbackCollection = Transition(label='Feedback Collection')

# Define the silent transitions
Skip = SilentTransition()

# Define the partial order nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[QualityTesting, BatchSelection])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[CurdPreparation, PressingCheese])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[AgingControl, FlavorProfiling])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[PackagingPrep, ClimatePacking])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[ExportLicensing, CustomsFiling])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[FreightBooking, ColdStorage])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[TransportTracking, RetailDelivery])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[FeedbackCollection, Skip])

# Define the exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop3, loop4])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop5, loop6])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop7, loop8])

# Define the root partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor1)