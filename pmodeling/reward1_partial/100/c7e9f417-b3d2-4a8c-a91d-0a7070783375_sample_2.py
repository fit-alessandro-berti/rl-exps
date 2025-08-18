import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities with their labels
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

# Define the structure of the POWL model
root = StrictPartialOrder(
    nodes=[
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
    ],
    order={
        # Define the dependencies between activities
        BrandAudit: [EquityReview, MarketAnalysis],
        EquityReview: [LegalClearance, TrademarkCheck],
        MarketAnalysis: [PortfolioMerge, CustomerSync],
        LegalClearance: [InternalBrief],
        TrademarkCheck: [InternalBrief],
        PortfolioMerge: [CampaignDesign, ResourcePlan],
        CustomerSync: [InternalBrief],
        CulturalAlign: [InternalBrief],
        InternalBrief: [CampaignDesign, ResourcePlan, StakeholderMeet, LaunchPrep],
        CampaignDesign: [ResourcePlan, StakeholderMeet, LaunchPrep],
        ResourcePlan: [StakeholderMeet, LaunchPrep],
        StakeholderMeet: [LaunchPrep],
        LaunchPrep: [FeedbackLoop, PerformanceTrack]
    }
)

# Print the root node to verify the structure
print(root)