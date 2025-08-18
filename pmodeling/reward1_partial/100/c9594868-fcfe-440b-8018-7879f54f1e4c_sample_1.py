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
root = StrictPartialOrder(
    nodes=[SiteSurvey, LoadTest, PermitReview, DesignLayout, MaterialSourcing, SoilPrep, HydroponicSetup,
           CommunityMeet, CropSelect, SensorInstall, WaterTesting, PestControl, GrowthMonitor, HarvestPlan,
           MarketLaunch, FeedbackCollect]
)

# Define the dependencies between activities
root.order.add_edge(SiteSurvey, LoadTest)
root.order.add_edge(SiteSurvey, PermitReview)
root.order.add_edge(LoadTest, DesignLayout)
root.order.add_edge(PermitReview, DesignLayout)
root.order.add_edge(DesignLayout, MaterialSourcing)
root.order.add_edge(DesignLayout, SoilPrep)
root.order.add_edge(DesignLayout, HydroponicSetup)
root.order.add_edge(MaterialSourcing, CommunityMeet)
root.order.add_edge(MaterialSourcing, CropSelect)
root.order.add_edge(SoilPrep, SensorInstall)
root.order.add_edge(SoilPrep, WaterTesting)
root.order.add_edge(SoilPrep, PestControl)
root.order.add_edge(HydroponicSetup, SensorInstall)
root.order.add_edge(HydroponicSetup, WaterTesting)
root.order.add_edge(HydroponicSetup, PestControl)
root.order.add_edge(SensorInstall, GrowthMonitor)
root.order.add_edge(WaterTesting, GrowthMonitor)
root.order.add_edge(PestControl, GrowthMonitor)
root.order.add_edge(GrowthMonitor, HarvestPlan)
root.order.add_edge(GrowthMonitor, FeedbackCollect)
root.order.add_edge(HarvestPlan, MarketLaunch)
root.order.add_edge(FeedbackCollect, MarketLaunch)

print(root)