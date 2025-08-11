import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transition
skip = SilentTransition()

# Define the loop for aging setup and humidity control
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[AgingSetup, HumidityControl])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[MicrobialCheck, skip])

# Define the XOR for quality testing and packaging design
xor = OperatorPOWL(operator=Operator.XOR, children=[QualityTesting, PackagingDesign])

# Define the XOR for customer review and inventory audit
xor2 = OperatorPOWL(operator=Operator.XOR, children=[CustomerReview, InventoryAudit])

# Define the XOR for sustainability audit and trace logging
xor3 = OperatorPOWL(operator=Operator.XOR, children=[SustainabilityAudit, TraceLogging])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, xor, xor2, xor3])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor, xor3)

# Save the final result in the variable 'root'