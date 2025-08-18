import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define partial order nodes
SiteSurveyNode = OperatorPOWL(operator=Operator.PO, children=[SiteSurvey])
DesignLayoutNode = OperatorPOWL(operator=Operator.PO, children=[DesignLayout])
ClimateSetupNode = OperatorPOWL(operator=Operator.PO, children=[ClimateSetup])
SensorInstallNode = OperatorPOWL(operator=Operator.PO, children=[SensorInstall])
NutrientMixNode = OperatorPOWL(operator=Operator.PO, children=[NutrientMix])
AutomationCodeNode = OperatorPOWL(operator=Operator.PO, children=[AutomationCode])
CropPlanningNode = OperatorPOWL(operator=Operator.PO, children=[CropPlanning])
PestControlNode = OperatorPOWL(operator=Operator.PO, children=[PestControl])
EnergyAuditNode = OperatorPOWL(operator=Operator.PO, children=[EnergyAudit])
WasteSortNode = OperatorPOWL(operator=Operator.PO, children=[WasteSort])
PlantingTierNode = OperatorPOWL(operator=Operator.PO, children=[PlantingTier])
HarvestPrepNode = OperatorPOWL(operator=Operator.PO, children=[HarvestPrep])
LogisticsPlanNode = OperatorPOWL(operator=Operator.PO, children=[LogisticsPlan])
CommunityMeetNode = OperatorPOWL(operator=Operator.PO, children=[CommunityMeet])
DataReviewNode = OperatorPOWL(operator=Operator.PO, children=[DataReview])
SystemUpgradeNode = OperatorPOWL(operator=Operator.PO, children=[SystemUpgrade])

# Define loops and choices
SiteSurveyLoop = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurveyNode, DesignLayoutNode])
ClimateSetupLoop = OperatorPOWL(operator=Operator.LOOP, children=[ClimateSetupNode, SensorInstallNode])
NutrientMixLoop = OperatorPOWL(operator=Operator.LOOP, children=[NutrientMixNode, AutomationCodeNode])
CropPlanningLoop = OperatorPOWL(operator=Operator.LOOP, children=[CropPlanningNode, PestControlNode])
EnergyAuditLoop = OperatorPOWL(operator=Operator.LOOP, children=[EnergyAuditNode, WasteSortNode])
PlantingTierLoop = OperatorPOWL(operator=Operator.LOOP, children=[PlantingTierNode, HarvestPrepNode])
LogisticsPlanLoop = OperatorPOWL(operator=Operator.LOOP, children=[LogisticsPlanNode, CommunityMeetNode])
DataReviewLoop = OperatorPOWL(operator=Operator.LOOP, children=[DataReviewNode, SystemUpgradeNode])

# Define the root partial order
root = StrictPartialOrder(nodes=[SiteSurveyLoop, ClimateSetupLoop, NutrientMixLoop, CropPlanningLoop, EnergyAuditLoop, PlantingTierLoop, LogisticsPlanLoop, DataReviewLoop])
root.order.add_edge(SiteSurveyLoop, DesignLayoutNode)
root.order.add_edge(ClimateSetupLoop, SensorInstallNode)
root.order.add_edge(NutrientMixLoop, AutomationCodeNode)
root.order.add_edge(CropPlanningLoop, PestControlNode)
root.order.add_edge(EnergyAuditLoop, WasteSortNode)
root.order.add_edge(PlantingTierLoop, HarvestPrepNode)
root.order.add_edge(LogisticsPlanLoop, CommunityMeetNode)
root.order.add_edge(DataReviewLoop, SystemUpgradeNode)

# Print the root partial order for verification
print(root)