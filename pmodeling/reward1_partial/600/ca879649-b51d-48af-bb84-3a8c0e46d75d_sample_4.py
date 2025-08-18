import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[MilkSourcing, QualityTesting])
xor = OperatorPOWL(operator=Operator.XOR, children=[BatchSelection, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[CurdPreparation, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[PressingCheese, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[AgingControl, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[FlavorProfiling, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[PackagingPrep, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[ClimatePacking, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[ExportLicensing, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[CustomsFiling, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[FreightBooking, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[ColdStorage, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[TransportTracking, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[RetailDelivery, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[FeedbackCollection, xor])

root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, xor)