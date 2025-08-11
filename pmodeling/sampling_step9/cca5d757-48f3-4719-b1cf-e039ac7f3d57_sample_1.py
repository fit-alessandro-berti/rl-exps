import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent activities
skip = SilentTransition()

# Define the loop for pest control
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[PestControl, skip])

# Define the choice for community engagement
community_choice = OperatorPOWL(operator=Operator.XOR, children=[CommunityMeet, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[pest_loop, community_choice, TechIntegrate, SiteAssess, LoadTesting, ClimateStudy, MediumPrep, BedInstall, IrrigationSetup, CropSelect, MonitorDeploy, WasteCycle, YieldForecast, MarketLink, WorkshopPlan])
root.order.add_edge(pest_loop, community_choice)
root.order.add_edge(pest_loop, TechIntegrate)
root.order.add_edge(community_choice, TechIntegrate)
root.order.add_edge(TechIntegrate, SiteAssess)
root.order.add_edge(TechIntegrate, LoadTesting)
root.order.add_edge(TechIntegrate, ClimateStudy)
root.order.add_edge(TechIntegrate, MediumPrep)
root.order.add_edge(TechIntegrate, BedInstall)
root.order.add_edge(TechIntegrate, IrrigationSetup)
root.order.add_edge(TechIntegrate, CropSelect)
root.order.add_edge(TechIntegrate, MonitorDeploy)
root.order.add_edge(TechIntegrate, WasteCycle)
root.order.add_edge(TechIntegrate, YieldForecast)
root.order.add_edge(TechIntegrate, MarketLink)
root.order.add_edge(TechIntegrate, WorkshopPlan)

# Print the root
print(root)