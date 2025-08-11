import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
OpportunityScan = Transition(label='Opportunity Scan')
IdeaWorkshop = Transition(label='Idea Workshop')
ConceptMerge = Transition(label='Concept Merge')
ResourceAlign = Transition(label='Resource Align')
PrototypeBuild = Transition(label='Prototype Build')
FeasibilityTest = Transition(label='Feasibility Test')
PilotLaunch = Transition(label='Pilot Launch')
FeedbackGather = Transition(label='Feedback Gather')
DesignAdapt = Transition(label='Design Adapt')
ComplianceCheck = Transition(label='Compliance Check')
ScalingPlan = Transition(label='Scaling Plan')
IPManagement = Transition(label='IP Management')
MarketSync = Transition(label='Market Sync')
PartnerReview = Transition(label='Partner Review')
ExitStrategy = Transition(label='Exit Strategy')

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[IdeaWorkshop, ResourceAlign])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ConceptMerge, PrototypeBuild])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[FeasibilityTest, PilotLaunch])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[FeedbackGather, DesignAdapt])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[ComplianceCheck, ScalingPlan])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[IPManagement, MarketSync])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[PartnerReview, ExitStrategy])

# Define the partial order
root = StrictPartialOrder(nodes=[OpportunityScan, xor1, xor2, xor3, xor4, xor5, xor6, xor7])

# Define the dependencies
root.order.add_edge(OpportunityScan, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)

# Print the root POWL model
print(root)