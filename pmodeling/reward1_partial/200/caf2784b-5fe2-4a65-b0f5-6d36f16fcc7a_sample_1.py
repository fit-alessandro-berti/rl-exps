from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the process
SiteAudit = Transition(label='Site Audit')
ImpactStudy = Transition(label='Impact Study')
DesignModules = Transition(label='Design Modules')
SensorSetup = Transition(label='Sensor Setup')
HydroponicsInstall = Transition(label='Hydroponics Install')
NutrientTest = Transition(label='Nutrient Test')
LightingConfig = Transition(label='Lighting Config')
StaffTraining = Transition(label='Staff Training')
DataCollection = Transition(label='Data Collection')
YieldAnalysis = Transition(label='Yield Analysis')
PestControl = Transition(label='Pest Control')
HarvestPlan = Transition(label='Harvest Plan')
PackagingPrep = Transition(label='Packaging Prep')
MarketDelivery = Transition(label='Market Delivery')
FeedbackLoop = Transition(label='Feedback Loop')

# Define the partial order graph
root = StrictPartialOrder(nodes=[
    SiteAudit,
    ImpactStudy,
    DesignModules,
    SensorSetup,
    HydroponicsInstall,
    NutrientTest,
    LightingConfig,
    StaffTraining,
    DataCollection,
    YieldAnalysis,
    PestControl,
    HarvestPlan,
    PackagingPrep,
    MarketDelivery,
    FeedbackLoop
])

# Define the dependencies between activities (order)
root.order.add_edge(SiteAudit, ImpactStudy)
root.order.add_edge(ImpactStudy, DesignModules)
root.order.add_edge(DesignModules, SensorSetup)
root.order.add_edge(SensorSetup, HydroponicsInstall)
root.order.add_edge(HydroponicsInstall, NutrientTest)
root.order.add_edge(NutrientTest, LightingConfig)
root.order.add_edge(LightingConfig, StaffTraining)
root.order.add_edge(StaffTraining, DataCollection)
root.order.add_edge(DataCollection, YieldAnalysis)
root.order.add_edge(YieldAnalysis, PestControl)
root.order.add_edge(PestControl, HarvestPlan)
root.order.add_edge(HarvestPlan, PackagingPrep)
root.order.add_edge(PackagingPrep, MarketDelivery)
root.order.add_edge(MarketDelivery, FeedbackLoop)

# The process is now defined in the 'root' variable