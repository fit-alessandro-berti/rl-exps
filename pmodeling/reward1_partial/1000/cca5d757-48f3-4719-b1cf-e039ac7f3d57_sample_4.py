import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
SiteAssess = Transition(label='Site Assess')
LoadTesting = Transition(label='Load Testing')
ClimateStudy = Transition(label='Climate Study')
MediumPrep = Transition(label='Medium Prep')
BedInstall = Transition(label='Bed Install')
IrrigationSetup = Transition(label='Irrigation Setup')
CropSelect = Transition(label='Crop Select')
PestControl = Transition(label='Pest Control')
CommunityMeet = Transition(label='Community Meet')
MonitorDeploy = Transition(label='Monitor Deploy')
WasteCycle = Transition(label='Waste Cycle')
YieldForecast = Transition(label='Yield Forecast')
MarketLink = Transition(label='Market Link')
WorkshopPlan = Transition(label='Workshop Plan')
TechIntegrate = Transition(label='Tech Integrate')

# Define the partial order and its dependencies
root = StrictPartialOrder(nodes=[SiteAssess, LoadTesting, ClimateStudy, MediumPrep, BedInstall, IrrigationSetup, CropSelect, PestControl, CommunityMeet, MonitorDeploy, WasteCycle, YieldForecast, MarketLink, WorkshopPlan, TechIntegrate])
root.order.add_edge(SiteAssess, LoadTesting)
root.order.add_edge(LoadTesting, ClimateStudy)
root.order.add_edge(ClimateStudy, MediumPrep)
root.order.add_edge(MediumPrep, BedInstall)
root.order.add_edge(BedInstall, IrrigationSetup)
root.order.add_edge(IrrigationSetup, CropSelect)
root.order.add_edge(CropSelect, PestControl)
root.order.add_edge(PestControl, CommunityMeet)
root.order.add_edge(CommunityMeet, MonitorDeploy)
root.order.add_edge(MonitorDeploy, WasteCycle)
root.order.add_edge(WasteCycle, YieldForecast)
root.order.add_edge(YieldForecast, MarketLink)
root.order.add_edge(MarketLink, WorkshopPlan)
root.order.add_edge(WorkshopPlan, TechIntegrate)