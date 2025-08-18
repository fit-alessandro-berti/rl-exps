import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
SiteAnalysis = Transition(label='Site Analysis')
LoadTest = Transition(label='Load Test')
SunlightMap = Transition(label='Sunlight Map')
MediumSelect = Transition(label='Medium Select')
HydroDesign = Transition(label='Hydro Design')
ProcureSeeds = Transition(label='Procure Seeds')
InstallIrrigation = Transition(label='Install Irrigation')
SetupClimate = Transition(label='Setup Climate')
CreateSchedule = Transition(label='Create Schedule')
PestControl = Transition(label='Pest Control')
MonitorGrowth = Transition(label='Monitor Growth')
AdjustSystems = Transition(label='Adjust Systems')
HarvestCrops = Transition(label='Harvest Crops')
PackageProduce = Transition(label='Package Produce')
EngageCommunity = Transition(label='Engage Community')
HostWorkshops = Transition(label='Host Workshops')

# Define the loop for pest control and system adjustment
PestControlLoop = OperatorPOWL(operator=Operator.LOOP, children=[PestControl, AdjustSystems])

# Define the exclusive choice for monitor growth and adjust systems
MonitorGrowthChoice = OperatorPOWL(operator=Operator.XOR, children=[MonitorGrowth, PestControlLoop])

# Define the partial order
root = StrictPartialOrder(nodes=[SiteAnalysis, LoadTest, SunlightMap, MediumSelect, HydroDesign, ProcureSeeds, InstallIrrigation, SetupClimate, CreateSchedule, PestControl, PestControlLoop, MonitorGrowthChoice, HarvestCrops, PackageProduce, EngageCommunity, HostWorkshops])
root.order.add_edge(SiteAnalysis, LoadTest)
root.order.add_edge(LoadTest, SunlightMap)
root.order.add_edge(SunlightMap, MediumSelect)
root.order.add_edge(MediumSelect, HydroDesign)
root.order.add_edge(HydroDesign, ProcureSeeds)
root.order.add_edge(ProcureSeeds, InstallIrrigation)
root.order.add_edge(InstallIrrigation, SetupClimate)
root.order.add_edge(SetupClimate, CreateSchedule)
root.order.add_edge(CreateSchedule, PestControl)
root.order.add_edge(PestControl, PestControlLoop)
root.order.add_edge(PestControlLoop, MonitorGrowthChoice)
root.order.add_edge(MonitorGrowthChoice, HarvestCrops)
root.order.add_edge(HarvestCrops, PackageProduce)
root.order.add_edge(PackageProduce, EngageCommunity)
root.order.add_edge(EngageCommunity, HostWorkshops)