import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
SiteSurvey = Transition(label='Site Survey')
ClimatePlan = Transition(label='Climate Plan')
SystemDesign = Transition(label='System Design')
AISetup = Transition(label='AI Setup')
SeedSourcing = Transition(label='Seed Sourcing')
NutrientMix = Transition(label='Nutrient Mix')
InstallHydro = Transition(label='Install Hydro')
EnergyAudit = Transition(label='Energy Audit')
StaffTraining = Transition(label='Staff Training')
TrialGrowth = Transition(label='Trial Growth')
YieldMeasure = Transition(label='Yield Measure')
WasteCycle = Transition(label='Waste Cycle')
ComplianceCheck = Transition(label='Compliance Check')
MarketStudy = Transition(label='Market Study')
CommunityMeet = Transition(label='Community Meet')
OptimizeEnvironment = Transition(label='Optimize Environment')

# Define partial order
root = StrictPartialOrder(
    nodes=[
        SiteSurvey,
        ClimatePlan,
        SystemDesign,
        AISetup,
        SeedSourcing,
        NutrientMix,
        InstallHydro,
        EnergyAudit,
        StaffTraining,
        TrialGrowth,
        YieldMeasure,
        WasteCycle,
        ComplianceCheck,
        MarketStudy,
        CommunityMeet,
        OptimizeEnvironment
    ]
)

# Define dependencies
root.order.add_edge(SiteSurvey, ClimatePlan)
root.order.add_edge(ClimatePlan, SystemDesign)
root.order.add_edge(SystemDesign, AISetup)
root.order.add_edge(AISetup, SeedSourcing)
root.order.add_edge(SeedSourcing, NutrientMix)
root.order.add_edge(NutrientMix, InstallHydro)
root.order.add_edge(InstallHydro, EnergyAudit)
root.order.add_edge(EnergyAudit, StaffTraining)
root.order.add_edge(StaffTraining, TrialGrowth)
root.order.add_edge(TrialGrowth, YieldMeasure)
root.order.add_edge(YieldMeasure, WasteCycle)
root.order.add_edge(WasteCycle, ComplianceCheck)
root.order.add_edge(ComplianceCheck, MarketStudy)
root.order.add_edge(MarketStudy, CommunityMeet)
root.order.add_edge(CommunityMeet, OptimizeEnvironment)

# Print the POWL model
print(root)