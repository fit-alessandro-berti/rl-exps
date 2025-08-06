import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

LoadAssess = Transition(label='Load Assess')
PermitReview = Transition(label='Permit Review')
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
SoilMix = Transition(label='Soil Mix')
InstallBeds = Transition(label='Install Beds')
IrrigationSet = Transition(label='Irrigation Set')
ClimateTest = Transition(label='Climate Test')
SensorDeploy = Transition(label='Sensor Deploy')
EnergySetup = Transition(label='Energy Setup')
CropSelect = Transition(label='Crop Select')
PlantSeeding = Transition(label='Plant Seeding')
CommunityMeet = Transition(label='Community Meet')
ComplianceCheck = Transition(label='Compliance Check')
GrowthMonitor = Transition(label='Growth Monitor')
HarvestPlan = Transition(label='Harvest Plan')
WasteRecycle = Transition(label='Waste Recycle')

skip = SilentTransition()

# Define the loop nodes for Permit Review and Site Survey
loop_PermitReview = OperatorPOWL(operator=Operator.LOOP, children=[PermitReview])
loop_SiteSurvey = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey])

# Define the exclusive choice nodes for Load Assess and Permit Review
xor_LoadAssess = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, loop_PermitReview])

# Define the exclusive choice nodes for Site Survey and Compliance Check
xor_SiteSurvey_ComplianceCheck = OperatorPOWL(operator=Operator.XOR, children=[loop_SiteSurvey, ComplianceCheck])

# Define the exclusive choice nodes for Design Layout and Soil Mix
xor_DesignLayout_SoilMix = OperatorPOWL(operator=Operator.XOR, children=[DesignLayout, SoilMix])

# Define the exclusive choice nodes for Install Beds and Irrigation Set
xor_InstallBeds_IrrigationSet = OperatorPOWL(operator=Operator.XOR, children=[InstallBeds, IrrigationSet])

# Define the exclusive choice nodes for Climate Test and Sensor Deploy
xor_ClimateTest_SensorDeploy = OperatorPOWL(operator=Operator.XOR, children=[ClimateTest, SensorDeploy])

# Define the exclusive choice nodes for Energy Setup and Crop Select
xor_EnergySetup_CropSelect = OperatorPOWL(operator=Operator.XOR, children=[EnergySetup, CropSelect])

# Define the exclusive choice nodes for Plant Seeding and Community Meet
xor_PlantSeeding_CommunityMeet = OperatorPOWL(operator=Operator.XOR, children=[PlantSeeding, CommunityMeet])

# Define the exclusive choice nodes for Growth Monitor and Harvest Plan
xor_GrowthMonitor_HarvestPlan = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, HarvestPlan])

# Define the exclusive choice nodes for Waste Recycle and Growth Monitor
xor_WasteRecycle_GrowthMonitor = OperatorPOWL(operator=Operator.XOR, children=[WasteRecycle, GrowthMonitor])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_WasteRecycle = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, WasteRecycle])

# Define the exclusive choice nodes for Growth Monitor and Waste Recycle
xor_GrowthMonitor_Waste