import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
IngredientSourcing = Transition(label='Ingredient Sourcing')
QualityTesting = Transition(label='Quality Testing')
ScentBlending = Transition(label='Scent Blending')
MicroBatch = Transition(label='Micro Batch')
SensoryPanel = Transition(label='Sensory Panel')
FormulaAdjust = Transition(label='Formula Adjust')
SafetyReview = Transition(label='Safety Review')
SustainabilityCheck = Transition(label='Sustainability Check')
PackagingDesign = Transition(label='Packaging Design')
PrototypeCreation = Transition(label='Prototype Creation')
ClientFeedback = Transition(label='Client Feedback')
LabelApproval = Transition(label='Label Approval')
FinalProduction = Transition(label='Final Production')
MarketingPlan = Transition(label='Marketing Plan')
DistributionPrep = Transition(label='Distribution Prep')
SalesLaunch = Transition(label='Sales Launch')

# Define the silent transitions (skips)
Skip1 = SilentTransition()
Skip2 = SilentTransition()
Skip3 = SilentTransition()
Skip4 = SilentTransition()
Skip5 = SilentTransition()

# Define the exclusive choice operators
Xor1 = OperatorPOWL(operator=Operator.XOR, children=[SafetyReview, Skip1])
Xor2 = OperatorPOWL(operator=Operator.XOR, children=[SustainabilityCheck, Skip2])
Xor3 = OperatorPOWL(operator=Operator.XOR, children=[PackagingDesign, Skip3])
Xor4 = OperatorPOWL(operator=Operator.XOR, children=[PrototypeCreation, Skip4])
Xor5 = OperatorPOWL(operator=Operator.XOR, children=[ClientFeedback, Skip5])

# Define the loop operators
Loop1 = OperatorPOWL(operator=Operator.LOOP, children=[IngredientSourcing, QualityTesting])
Loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ScentBlending, MicroBatch])
Loop3 = OperatorPOWL(operator=Operator.LOOP, children=[SensoryPanel, FormulaAdjust])
Loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Xor1, Xor2])
Loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Xor3, Xor4])
Loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Xor5, MarketingPlan])
Loop7 = OperatorPOWL(operator=Operator.LOOP, children=[DistributionPrep, SalesLaunch])

# Define the root node
root = StrictPartialOrder(nodes=[Loop1, Loop2, Loop3, Loop4, Loop5, Loop6, Loop7])

# Define the order of nodes
root.order.add_edge(Loop1, Loop2)
root.order.add_edge(Loop2, Loop3)
root.order.add_edge(Loop3, Loop4)
root.order.add_edge(Loop4, Loop5)
root.order.add_edge(Loop5, Loop6)
root.order.add_edge(Loop6, Loop7)
root.order.add_edge(Loop7, MarketingPlan)
root.order.add_edge(Loop7, DistributionPrep)

# Print the root node
print(root)