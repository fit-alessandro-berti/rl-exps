import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
ClientBrief = Transition(label='Client Brief')
ConceptSketch = Transition(label='Concept Sketch')
DesignReview = Transition(label='Design Review')
MaterialSourcing = Transition(label='Material Sourcing')
PrototypeBuild = Transition(label='Prototype Build')
VendorCoordination = Transition(label='Vendor Coordination')
QualityCheck = Transition(label='Quality Check')
ClientApproval = Transition(label='Client Approval')
PackagingPrep = Transition(label='Packaging Prep')
ShippingArrange = Transition(label='Shipping Arrange')
FeedbackCollect = Transition(label='Feedback Collect')
PortfolioUpdate = Transition(label='Portfolio Update')
ContractSign = Transition(label='Contract Sign')
IPManagement = Transition(label='IP Management')
FutureSchedule = Transition(label='Future Schedule')
MaintenancePlan = Transition(label='Maintenance Plan')

# Define silent transitions
skip = SilentTransition()

# Define partial order
loop = OperatorPOWL(operator=Operator.LOOP, children=[ClientBrief, ConceptSketch, DesignReview, MaterialSourcing, PrototypeBuild, VendorCoordination, QualityCheck, ClientApproval, PackagingPrep, ShippingArrange, FeedbackCollect, PortfolioUpdate, ContractSign, IPManagement, FutureSchedule, MaintenancePlan])

# Define partial order nodes and their dependencies
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, skip)