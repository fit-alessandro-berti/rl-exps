from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the POWL model structure
root = StrictPartialOrder(nodes=[
    OpportunityScan, 
    IdeaWorkshop, 
    ConceptMerge, 
    ResourceAlign, 
    PrototypeBuild, 
    FeasibilityTest, 
    PilotLaunch, 
    FeedbackGather, 
    DesignAdapt, 
    ComplianceCheck, 
    ScalingPlan, 
    IPManagement, 
    MarketSync, 
    PartnerReview, 
    ExitStrategy
])

# Define the dependencies between activities
root.order.add_edge(OpportunityScan, IdeaWorkshop)
root.order.add_edge(IdeaWorkshop, ConceptMerge)
root.order.add_edge(ConceptMerge, ResourceAlign)
root.order.add_edge(ResourceAlign, PrototypeBuild)
root.order.add_edge(PrototypeBuild, FeasibilityTest)
root.order.add_edge(FeasibilityTest, PilotLaunch)
root.order.add_edge(PilotLaunch, FeedbackGather)
root.order.add_edge(FeedbackGather, DesignAdapt)
root.order.add_edge(DesignAdapt, ComplianceCheck)
root.order.add_edge(ComplianceCheck, ScalingPlan)
root.order.add_edge(ScalingPlan, IPManagement)
root.order.add_edge(IPManagement, MarketSync)
root.order.add_edge(MarketSync, PartnerReview)
root.order.add_edge(PartnerReview, ExitStrategy)

print(root)