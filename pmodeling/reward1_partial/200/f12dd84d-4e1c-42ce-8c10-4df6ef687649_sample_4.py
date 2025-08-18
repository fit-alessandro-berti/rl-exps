import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Define the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[MilkSourcing, QualityTesting])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[CurdProcessing, SaltApplication, MoldInoculation])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[PressMolding, BrineSoaking, AgingSetup])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[HumidityControl, MicrobialCheck])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[PackagingDesign, LabelPrinting])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[TraceLogging, DistributionPlan, CustomerReview, InventoryAudit, SustainabilityAudit])

# Connect the loops
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)