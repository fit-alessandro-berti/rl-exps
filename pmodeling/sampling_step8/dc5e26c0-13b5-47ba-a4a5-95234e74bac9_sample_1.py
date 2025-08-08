from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
ClimateSetup = Transition(label='Climate Setup')
SensorInstall = Transition(label='Sensor Install')
NutrientMix = Transition(label='Nutrient Mix')
AutomationCode = Transition(label='Automation Code')
CropPlanning = Transition(label='Crop Planning')
PestControl = Transition(label='Pest Control')
EnergyAudit = Transition(label='Energy Audit')
WasteSort = Transition(label='Waste Sort')
PlantingTier = Transition(label='Planting Tier')
HarvestPrep = Transition(label='Harvest Prep')
LogisticsPlan = Transition(label='Logistics Plan')
CommunityMeet = Transition(label='Community Meet')
DataReview = Transition(label='Data Review')
SystemUpgrade = Transition(label='System Upgrade')

# Define the silent transition for the loop
skip = SilentTransition()

# Define the loop for the activities that need to be repeated
loop = OperatorPOWL(operator=Operator.LOOP, children=[NutrientMix, AutomationCode, CropPlanning, PestControl, EnergyAudit, WasteSort, PlantingTier, HarvestPrep, LogisticsPlan])

# Define the exclusive choice for the activities that need to be done in parallel
xor = OperatorPOWL(operator=Operator.XOR, children=[CommunityMeet, DataReview, SystemUpgrade])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[SiteSurvey, DesignLayout, ClimateSetup, SensorInstall, loop, xor])
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, ClimateSetup)
root.order.add_edge(ClimateSetup, SensorInstall)
root.order.add_edge(SensorInstall, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, CommunityMeet)
root.order.add_edge(xor, DataReview)
root.order.add_edge(xor, SystemUpgrade)

print(root)