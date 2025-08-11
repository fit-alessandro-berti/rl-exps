import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the partial order
loopAging = OperatorPOWL(operator=Operator.LOOP, children=[AgingSetup, HumidityControl, MicrobialCheck])
loopPackaging = OperatorPOWL(operator=Operator.LOOP, children=[PackagingDesign, LabelPrinting, TraceLogging])
loopDistribution = OperatorPOWL(operator=Operator.LOOP, children=[DistributionPlan, CustomerReview])
loopInventory = OperatorPOWL(operator=Operator.LOOP, children=[InventoryAudit, SustainabilityAudit])
loopStaff = OperatorPOWL(operator=Operator.LOOP, children=[MilkSourcing, QualityTesting, CurdProcessing, SaltApplication, MoldInoculation, PressMolding, BrineSoaking])

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[loopAging, loopPackaging, loopDistribution, loopInventory, loopStaff])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loopAging, loopPackaging, loopDistribution, loopInventory, loopStaff, xor])
root.order.add_edge(loopAging, xor)
root.order.add_edge(loopPackaging, xor)
root.order.add_edge(loopDistribution, xor)
root.order.add_edge(loopInventory, xor)
root.order.add_edge(loopStaff, xor)

# Print the POWL model
print(root)