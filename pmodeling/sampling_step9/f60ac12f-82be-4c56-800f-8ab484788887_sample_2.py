import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
MilkSourcing = Transition(label='Milk Sourcing')
CultureBlending = Transition(label='Culture Blending')
MilkPasteurize = Transition(label='Milk Pasteurize')
CurdCutting = Transition(label='Curd Cutting')
WheyDrain = Transition(label='Whey Drain')
MoldInoculate = Transition(label='Mold Inoculate')
PressCheese = Transition(label='Press Cheese')
SaltBrine = Transition(label='Salt Brine')
AgeMonitor = Transition(label='Age Monitor')
QualityTest = Transition(label='Quality Test')
PackagingPrep = Transition(label='Packaging Prep')
LabelDesign = Transition(label='Label Design')
OrderAllocation = Transition(label='Order Allocation')
TransportArrange = Transition(label='Transport Arrange')
RetailSync = Transition(label='Retail Sync')
CustomerReview = Transition(label='Customer Review')
FeedbackAnalyze = Transition(label='Feedback Analyze')

# Define the silent transitions
skip = SilentTransition()

# Define the loop node
loop = OperatorPOWL(operator=Operator.LOOP, children=[MilkSourcing, CultureBlending, MilkPasteurize, CurdCutting, WheyDrain, MoldInoculate, PressCheese, SaltBrine, AgeMonitor, QualityTest, PackagingPrep, LabelDesign, OrderAllocation, TransportArrange, RetailSync, CustomerReview, FeedbackAnalyze])

# Define the partial order
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])

# Define the root
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root
print(root)