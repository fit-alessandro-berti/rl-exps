import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
FarmSelection = Transition(label='Farm Selection')
MilkTesting = Transition(label='Milk Testing')
BatchPasteurize = Transition(label='Batch Pasteurize')
CultureAdd = Transition(label='Culture Add')
CurdCut = Transition(label='Curd Cut')
WheyDrain = Transition(label='Whey Drain')
MoldInoculate = Transition(label='Mold Inoculate')
PressForm = Transition(label='Press Form')
SaltRub = Transition(label='Salt Rub')
AgingMonitor = Transition(label='Aging Monitor')
FlavorAdjust = Transition(label='Flavor Adjust')
PackagingDesign = Transition(label='Packaging Design')
LabelApproval = Transition(label='Label Approval')
OrderProcessing = Transition(label='Order Processing')
ColdStorage = Transition(label='Cold Storage')
DeliverySchedule = Transition(label='Delivery Schedule')
RetailSetup = Transition(label='Retail Setup')
FeedbackCollect = Transition(label='Feedback Collect')

# Define the silent transitions
SkipMilkTesting = SilentTransition(label='Skip Milk Testing')
SkipCultureAdd = SilentTransition(label='Skip Culture Add')
SkipWheyDrain = SilentTransition(label='Skip Whey Drain')
SkipSaltRub = SilentTransition(label='Skip Salt Rub')
SkipLabelApproval = SilentTransition(label='Skip Label Approval')
SkipFeedbackCollect = SilentTransition(label='Skip Feedback Collect')

# Define the loop nodes
AgingLoop = OperatorPOWL(operator=Operator.LOOP, children=[AgingMonitor, FlavorAdjust, PackagingDesign, LabelApproval])
RetailLoop = OperatorPOWL(operator=Operator.LOOP, children=[RetailSetup, FeedbackCollect])

# Define the choice nodes
MilkChoice = OperatorPOWL(operator=Operator.XOR, children=[FarmSelection, SkipMilkTesting])
CultureChoice = OperatorPOWL(operator=Operator.XOR, children=[MilkTesting, SkipCultureAdd])
WheyChoice = OperatorPOWL(operator=Operator.XOR, children=[CultureAdd, SkipWheyDrain])
SaltChoice = OperatorPOWL(operator=Operator.XOR, children=[WheyDrain, SkipSaltRub])
LabelChoice = OperatorPOWL(operator=Operator.XOR, children=[SaltRub, SkipLabelApproval])
FeedbackChoice = OperatorPOWL(operator=Operator.XOR, children=[LabelApproval, SkipFeedbackCollect])

# Define the root POWL model
root = StrictPartialOrder(nodes=[MilkChoice, CultureChoice, WheyChoice, SaltChoice, LabelChoice, FeedbackChoice, AgingLoop, RetailLoop])
root.order.add_edge(MilkChoice, CultureChoice)
root.order.add_edge(CultureChoice, WheyChoice)
root.order.add_edge(WheyChoice, SaltChoice)
root.order.add_edge(SaltChoice, LabelChoice)
root.order.add_edge(LabelChoice, FeedbackChoice)
root.order.add_edge(FeedbackChoice, AgingLoop)
root.order.add_edge(AgingLoop, RetailLoop)
root.order.add_edge(RetailLoop, RetailLoop)

# Print the root POWL model
print(root)