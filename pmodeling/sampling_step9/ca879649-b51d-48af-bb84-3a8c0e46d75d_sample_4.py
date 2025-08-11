import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[MilkSourcing, QualityTesting, BatchSelection, CurdPreparation, PressingCheese, AgingControl, FlavorProfiling, PackagingPrep, ClimatePacking, ExportLicensing, CustomsFiling, FreightBooking, ColdStorage, TransportTracking, RetailDelivery, FeedbackCollection])
xor = OperatorPOWL(operator=Operator.XOR, children=[RetailDelivery, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the resulting POWL model
print(root)