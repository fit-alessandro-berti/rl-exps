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

# Define the loop for aging and quality testing
age_loop = OperatorPOWL(operator=Operator.LOOP, children=[AgeMonitor, QualityTest])

# Define the XOR for packaging and retail sync
packaging_xor = OperatorPOWL(operator=Operator.XOR, children=[PackagingPrep, RetailSync])

# Define the XOR for customer review and feedback analyze
customer_review_xor = OperatorPOWL(operator=Operator.XOR, children=[CustomerReview, FeedbackAnalyze])

# Define the partial order
root = StrictPartialOrder(nodes=[MilkSourcing, CultureBlending, MilkPasteurize, CurdCutting, WheyDrain, MoldInoculate, PressCheese, SaltBrine, age_loop, packaging_xor, customer_review_xor])
root.order.add_edge(MilkSourcing, CultureBlending)
root.order.add_edge(CultureBlending, MilkPasteurize)
root.order.add_edge(MilkPasteurize, CurdCutting)
root.order.add_edge(CurdCutting, WheyDrain)
root.order.add_edge(WheyDrain, MoldInoculate)
root.order.add_edge(MoldInoculate, PressCheese)
root.order.add_edge(PressCheese, SaltBrine)
root.order.add_edge(SaltBrine, AgeMonitor)
root.order.add_edge(AgeMonitor, QualityTest)
root.order.add_edge(QualityTest, PackagingPrep)
root.order.add_edge(PackagingPrep, RetailSync)
root.order.add_edge(RetailSync, CustomerReview)
root.order.add_edge(CustomerReview, FeedbackAnalyze)