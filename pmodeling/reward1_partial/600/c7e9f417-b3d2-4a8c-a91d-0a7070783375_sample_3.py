import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with exact names as given
BrandAudit = Transition(label='Brand Audit')
EquityReview = Transition(label='Equity Review')
MarketAnalysis = Transition(label='Market Analysis')
LegalClearance = Transition(label='Legal Clearance')
TrademarkCheck = Transition(label='Trademark Check')
PortfolioMerge = Transition(label='Portfolio Merge')
CustomerSync = Transition(label='Customer Sync')
CulturalAlign = Transition(label='Cultural Align')
InternalBrief = Transition(label='Internal Brief')
CampaignDesign = Transition(label='Campaign Design')
ResourcePlan = Transition(label='Resource Plan')
StakeholderMeet = Transition(label='Stakeholder Meet')
LaunchPrep = Transition(label='Launch Prep')
FeedbackLoop = Transition(label='Feedback Loop')
PerformanceTrack = Transition(label='Performance Track')

# Define silent transitions
skip = SilentTransition()

# Define nodes and edges
root = StrictPartialOrder(nodes=[
    BrandAudit,
    EquityReview,
    MarketAnalysis,
    LegalClearance,
    TrademarkCheck,
    PortfolioMerge,
    CustomerSync,
    CulturalAlign,
    InternalBrief,
    CampaignDesign,
    ResourcePlan,
    StakeholderMeet,
    LaunchPrep,
    FeedbackLoop,
    PerformanceTrack
])

# Define dependencies
root.order.add_edge(BrandAudit, EquityReview)
root.order.add_edge(EquityReview, MarketAnalysis)
root.order.add_edge(MarketAnalysis, LegalClearance)
root.order.add_edge(LegalClearance, TrademarkCheck)
root.order.add_edge(TrademarkCheck, PortfolioMerge)
root.order.add_edge(PortfolioMerge, CustomerSync)
root.order.add_edge(CustomerSync, CulturalAlign)
root.order.add_edge(CulturalAlign, InternalBrief)
root.order.add_edge(InternalBrief, CampaignDesign)
root.order.add_edge(CampaignDesign, ResourcePlan)
root.order.add_edge(ResourcePlan, StakeholderMeet)
root.order.add_edge(StakeholderMeet, LaunchPrep)
root.order.add_edge(LaunchPrep, FeedbackLoop)
root.order.add_edge(FeedbackLoop, PerformanceTrack)

# Print the POWL model
print(root)