from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
SiteSurvey = Transition(label='Site Survey')
ImpactStudy = Transition(label='Impact Study')
StructureCheck = Transition(label='Structure Check')
SoilTesting = Transition(label='Soil Testing')
SystemDesign = Transition(label='System Design')
SeedSelection = Transition(label='Seed Selection')
IrrigationSetup = Transition(label='Irrigation Setup')
LightingInstall = Transition(label='Lighting Install')
PestControl = Transition(label='Pest Control')
CommunityMeet = Transition(label='Community Meet')
RegulationReview = Transition(label='Regulation Review')
WastePlan = Transition(label='Waste Plan')
CropMonitor = Transition(label='Crop Monitor')
HarvestPrep = Transition(label='Harvest Prep')
MarketLaunch = Transition(label='Market Launch')

# Create a partial order model
root = StrictPartialOrder(nodes=[
    SiteSurvey, ImpactStudy, StructureCheck, SoilTesting, SystemDesign,
    SeedSelection, IrrigationSetup, LightingInstall, PestControl, CommunityMeet,
    RegulationReview, WastePlan, CropMonitor, HarvestPrep, MarketLaunch
])

# Define the dependencies (edges) between the nodes
root.order.add_edge(SiteSurvey, ImpactStudy)
root.order.add_edge(ImpactStudy, StructureCheck)
root.order.add_edge(StructureCheck, SoilTesting)
root.order.add_edge(SoilTesting, SystemDesign)
root.order.add_edge(SystemDesign, SeedSelection)
root.order.add_edge(SeedSelection, IrrigationSetup)
root.order.add_edge(IrrigationSetup, LightingInstall)
root.order.add_edge(LightingInstall, PestControl)
root.order.add_edge(PestControl, CommunityMeet)
root.order.add_edge(CommunityMeet, RegulationReview)
root.order.add_edge(RegulationReview, WastePlan)
root.order.add_edge(WastePlan, CropMonitor)
root.order.add_edge(CropMonitor, HarvestPrep)
root.order.add_edge(HarvestPrep, MarketLaunch)

print(root)