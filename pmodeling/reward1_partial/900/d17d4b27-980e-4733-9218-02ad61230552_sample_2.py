import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL nodes
SiteAnalysis = Transition(label='Site Analysis')
ZoningReview = Transition(label='Zoning Review')
ModularDesign = Transition(label='Modular Design')
ClimateSetup = Transition(label='Climate Setup')
NutrientMix = Transition(label='Nutrient Mix')
SeedSelection = Transition(label='Seed Selection')
AI_Monitoring = Transition(label='AI Monitoring')
LightingControl = Transition(label='Lighting Control')
EnergyAudit = Transition(label='Energy Audit')
WaterReclaim = Transition(label='Water Reclaim')
WasteSorting = Transition(label='Waste Sorting')
CommunityMeet = Transition(label='Community Meet')
StaffTraining = Transition(label='Staff Training')
YieldForecast = Transition(label='Yield Forecast')
MarketSync = Transition(label='Market Sync')
SupplyChain = Transition(label='Supply Chain')

# Define the process model
root = StrictPartialOrder(nodes=[
    SiteAnalysis,
    ZoningReview,
    ModularDesign,
    ClimateSetup,
    NutrientMix,
    SeedSelection,
    AI_Monitoring,
    LightingControl,
    EnergyAudit,
    WaterReclaim,
    WasteSorting,
    CommunityMeet,
    StaffTraining,
    YieldForecast,
    MarketSync,
    SupplyChain
])

# Add dependencies between activities
root.order.add_edge(SiteAnalysis, ZoningReview)
root.order.add_edge(ZoningReview, ModularDesign)
root.order.add_edge(ModularDesign, ClimateSetup)
root.order.add_edge(ClimateSetup, NutrientMix)
root.order.add_edge(NutrientMix, SeedSelection)
root.order.add_edge(SeedSelection, AI_Monitoring)
root.order.add_edge(AI_Monitoring, LightingControl)
root.order.add_edge(LightingControl, EnergyAudit)
root.order.add_edge(EnergyAudit, WaterReclaim)
root.order.add_edge(WaterReclaim, WasteSorting)
root.order.add_edge(WasteSorting, CommunityMeet)
root.order.add_edge(CommunityMeet, StaffTraining)
root.order.add_edge(StaffTraining, YieldForecast)
root.order.add_edge(YieldForecast, MarketSync)
root.order.add_edge(MarketSync, SupplyChain)

print(root)