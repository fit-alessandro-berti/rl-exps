from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the process
SiteSurvey = Transition(label='Site Survey')
LoadTest = Transition(label='Load Test')
PermitReview = Transition(label='Permit Review')
DesignLayout = Transition(label='Design Layout')
MaterialSourcing = Transition(label='Material Sourcing')
SoilPrep = Transition(label='Soil Prep')
HydroponicSetup = Transition(label='Hydroponic Setup')
CommunityMeet = Transition(label='Community Meet')
CropSelect = Transition(label='Crop Select')
SensorInstall = Transition(label='Sensor Install')
WaterTesting = Transition(label='Water Testing')
PestControl = Transition(label='Pest Control')
GrowthMonitor = Transition(label='Growth Monitor')
HarvestPlan = Transition(label='Harvest Plan')
MarketLaunch = Transition(label='Market Launch')
FeedbackCollect = Transition(label='Feedback Collect')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    SiteSurvey,
    LoadTest,
    PermitReview,
    DesignLayout,
    MaterialSourcing,
    SoilPrep,
    HydroponicSetup,
    CommunityMeet,
    CropSelect,
    SensorInstall,
    WaterTesting,
    PestControl,
    GrowthMonitor,
    HarvestPlan,
    MarketLaunch,
    FeedbackCollect
])

# Add dependencies between activities (if any)
# For example, if SiteSurvey depends on LoadTest, add an edge
root.order.add_edge(SiteSurvey, LoadTest)

# Return the root of the POWL model
print(root)