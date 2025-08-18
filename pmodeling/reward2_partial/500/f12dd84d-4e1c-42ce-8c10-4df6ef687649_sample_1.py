from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
MilkSourcing = Transition(label='Milk Sourcing')
QualityTesting = Transition(label='Quality Testing')
CurdProcessing = Transition(label='Curd Processing')
SaltApplication = Transition(label='Salt Application')
MoldInoculation = Transition(label='Mold Inoculation')
PressMolding = Transition(label='Press Molding')
BrineSoaking = Transition(label='Brine Soaking')
AgingSetup = Transition(label='Aging Setup')
HumidityControl = Transition(label='Humidity Control')
MicrobialCheck = Transition(label='Microbial Check')
PackagingDesign = Transition(label='Packaging Design')
LabelPrinting = Transition(label='Label Printing')
TraceLogging = Transition(label='Trace Logging')
DistributionPlan = Transition(label='Distribution Plan')
CustomerReview = Transition(label='Customer Review')
InventoryAudit = Transition(label='Inventory Audit')
SustainabilityAudit = Transition(label='Sustainability Audit')

# Define the process as a Partial Order (POWL)
root = StrictPartialOrder(nodes=[MilkSourcing, QualityTesting, CurdProcessing, SaltApplication, MoldInoculation, PressMolding, BrineSoaking, AgingSetup, HumidityControl, MicrobialCheck, PackagingDesign, LabelPrinting, TraceLogging, DistributionPlan, CustomerReview, InventoryAudit, SustainabilityAudit])

# Define the order between the activities
root.order.add_edge(MilkSourcing, QualityTesting)
root.order.add_edge(QualityTesting, CurdProcessing)
root.order.add_edge(CurdProcessing, SaltApplication)
root.order.add_edge(SaltApplication, MoldInoculation)
root.order.add_edge(MoldInoculation, PressMolding)
root.order.add_edge(PressMolding, BrineSoaking)
root.order.add_edge(BrineSoaking, AgingSetup)
root.order.add_edge(AgingSetup, HumidityControl)
root.order.add_edge(HumidityControl, MicrobialCheck)
root.order.add_edge(MicrobialCheck, PackagingDesign)
root.order.add_edge(PackagingDesign, LabelPrinting)
root.order.add_edge(LabelPrinting, TraceLogging)
root.order.add_edge(TraceLogging, DistributionPlan)
root.order.add_edge(DistributionPlan, CustomerReview)
root.order.add_edge(CustomerReview, InventoryAudit)
root.order.add_edge(InventoryAudit, SustainabilityAudit)

# The final result is stored in the variable 'root'