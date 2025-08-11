import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
MaterialSourcing = Transition(label='Material Sourcing')
CulturalVerify = Transition(label='Cultural Verify')
EcoTransport = Transition(label='Eco Transport')
BatchStorytelling = Transition(label='Batch Storytelling')
CraftsmanAssignment = Transition(label='Craftsman Assignment')
ProductCreation = Transition(label='Product Creation')
ProvenanceCatalog = Transition(label='Provenance Catalog')
CommunityMarketing = Transition(label='Community Marketing')
CollectorTargeting = Transition(label='Collector Targeting')
PackageAssembly = Transition(label='Package Assembly')
LocalCooperatives = Transition(label='Local Cooperatives')
EnvironmentalAudit = Transition(label='Environmental Audit')
EthicalLogistics = Transition(label='Ethical Logistics')
GlobalShipping = Transition(label='Global Shipping')
FeedbackCollection = Transition(label='Feedback Collection')

# Create silent transitions
skip = SilentTransition()

# Define the process steps
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[MaterialSourcing, EcoTransport])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[BatchStorytelling, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[CraftsmanAssignment, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[ProductCreation, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ProvenanceCatalog, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[CommunityMarketing, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[CollectorTargeting, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[PackageAssembly, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[LocalCooperatives, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[EnvironmentalAudit, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[EthicalLogistics, skip])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[GlobalShipping, skip])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[FeedbackCollection, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, xor11, xor12])
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, xor11)
root.order.add_edge(xor11, xor12)

# Print the root
print(root)