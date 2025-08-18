import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process
root = StrictPartialOrder(nodes=[SiteSurvey, DesignLayout, ClimateSetup, SensorInstall, NutrientMix, AutomationCode, CropPlanning, PestControl, EnergyAudit, WasteSort, PlantingTier, HarvestPrep, LogisticsPlan, CommunityMeet, DataReview, SystemUpgrade])
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, ClimateSetup)
root.order.add_edge(ClimateSetup, SensorInstall)
root.order.add_edge(SensorInstall, NutrientMix)
root.order.add_edge(NutrientMix, AutomationCode)
root.order.add_edge(AutomationCode, CropPlanning)
root.order.add_edge(CropPlanning, PestControl)
root.order.add_edge(PestControl, EnergyAudit)
root.order.add_edge(EnergyAudit, WasteSort)
root.order.add_edge(WasteSort, PlantingTier)
root.order.add_edge(PlantingTier, HarvestPrep)
root.order.add_edge(HarvestPrep, LogisticsPlan)
root.order.add_edge(LogisticsPlan, CommunityMeet)
root.order.add_edge(CommunityMeet, DataReview)
root.order.add_edge(DataReview, SystemUpgrade)