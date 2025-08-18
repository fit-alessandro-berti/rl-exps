from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
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

# Define the partial order with dependencies between activities
root = StrictPartialOrder(nodes=[
    MilkSourcing, QualityTesting, BatchSelection, CurdPreparation, PressingCheese,
    AgingControl, FlavorProfiling, PackagingPrep, ClimatePacking, ExportLicensing,
    CustomsFiling, FreightBooking, ColdStorage, TransportTracking, RetailDelivery,
    FeedbackCollection
])

# Define the order of activities
root.order.add_edge(MilkSourcing, QualityTesting)
root.order.add_edge(QualityTesting, BatchSelection)
root.order.add_edge(BatchSelection, CurdPreparation)
root.order.add_edge(CurdPreparation, PressingCheese)
root.order.add_edge(PressingCheese, AgingControl)
root.order.add_edge(AgingControl, FlavorProfiling)
root.order.add_edge(FlavorProfiling, PackagingPrep)
root.order.add_edge(PackagingPrep, ClimatePacking)
root.order.add_edge(ClimatePacking, ExportLicensing)
root.order.add_edge(ExportLicensing, CustomsFiling)
root.order.add_edge(CustomsFiling, FreightBooking)
root.order.add_edge(FreightBooking, ColdStorage)
root.order.add_edge(ColdStorage, TransportTracking)
root.order.add_edge(TransportTracking, RetailDelivery)
root.order.add_edge(RetailDelivery, FeedbackCollection)

# The final POWL model is stored in the 'root' variable