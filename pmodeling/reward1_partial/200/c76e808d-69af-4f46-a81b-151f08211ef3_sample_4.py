import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

MilkSourcing = Transition(label='Milk Sourcing')
CultureSelection = Transition(label='Culture Selection')
MilkTesting = Transition(label='Milk Testing')
CurdFormation = Transition(label='Curd Formation')
WheySeparation = Transition(label='Whey Separation')
MoldingCheese = Transition(label='Molding Cheese')
SaltingProcess = Transition(label='Salting Process')
AgingSetup = Transition(label='Aging Setup')
EnvMonitoring = Transition(label='Env Monitoring')
FlavorProfiling = Transition(label='Flavor Profiling')
PackagingDesign = Transition(label='Packaging Design')
BlockchainEntry = Transition(label='Blockchain Entry')
QualityAudit = Transition(label='Quality Audit')
RetailSync = Transition(label='Retail Sync')
TransportPrep = Transition(label='Transport Prep')
DeliveryTracking = Transition(label='Delivery Tracking')
CustomerFeedback = Transition(label='Customer Feedback')

skip = SilentTransition()
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, CultureSelection])
loop = OperatorPOWL(operator=Operator.LOOP, children=[MilkTesting, CurdFormation, WheySeparation, MoldingCheese, SaltingProcess, AgingSetup, EnvMonitoring, FlavorProfiling])
xor_loop = OperatorPOWL(operator=Operator.XOR, children=[PackagingDesign, BlockchainEntry, QualityAudit, RetailSync, TransportPrep, DeliveryTracking, CustomerFeedback])
root = StrictPartialOrder(nodes=[loop, xor, xor_loop])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor_loop)