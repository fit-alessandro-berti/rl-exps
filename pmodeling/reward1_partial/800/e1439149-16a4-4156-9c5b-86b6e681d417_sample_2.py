import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
TrendScan = Transition(label='Trend Scan')
IdeaHarvest = Transition(label='Idea Harvest')
WorkshopHost = Transition(label='Workshop Host')
ConceptFilter = Transition(label='Concept Filter')
PrototypeBuild = Transition(label='Prototype Build')
ExpertReview = Transition(label='Expert Review')
FeasibilityCheck = Transition(label='Feasibility Check')
RiskAssess = Transition(label='Risk Assess')
PilotLaunch = Transition(label='Pilot Launch')
DataCapture = Transition(label='Data Capture')
PerformanceReview = Transition(label='Performance Review')
ScalePlan = Transition(label='Scale Plan')
ResourceAlign = Transition(label='Resource Align')
LearnShare = Transition(label='Learn Share')
CultureEmbed = Transition(label='Culture Embed')

# Define the partial order
root = StrictPartialOrder(nodes=[
    TrendScan,
    IdeaHarvest,
    WorkshopHost,
    ConceptFilter,
    PrototypeBuild,
    ExpertReview,
    FeasibilityCheck,
    RiskAssess,
    PilotLaunch,
    DataCapture,
    PerformanceReview,
    ScalePlan,
    ResourceAlign,
    LearnShare,
    CultureEmbed
])

# Define the dependencies
root.order.add_edge(TrendScan, IdeaHarvest)
root.order.add_edge(IdeaHarvest, WorkshopHost)
root.order.add_edge(WorkshopHost, ConceptFilter)
root.order.add_edge(ConceptFilter, PrototypeBuild)
root.order.add_edge(PrototypeBuild, ExpertReview)
root.order.add_edge(ExpertReview, FeasibilityCheck)
root.order.add_edge(FeasibilityCheck, RiskAssess)
root.order.add_edge(RiskAssess, PilotLaunch)
root.order.add_edge(PilotLaunch, DataCapture)
root.order.add_edge(DataCapture, PerformanceReview)
root.order.add_edge(PerformanceReview, ScalePlan)
root.order.add_edge(ScalePlan, ResourceAlign)
root.order.add_edge(ResourceAlign, LearnShare)
root.order.add_edge(LearnShare, CultureEmbed)

print(root)