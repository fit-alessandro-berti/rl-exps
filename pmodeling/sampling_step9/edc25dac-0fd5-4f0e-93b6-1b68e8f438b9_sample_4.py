import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loop node for Permit Review and Compliance Check
loop = OperatorPOWL(operator=Operator.LOOP, children=[PermitReview, ComplianceCheck])

# Define XOR node for Site Survey and Design Layout
xor = OperatorPOWL(operator=Operator.XOR, children=[SiteSurvey, DesignLayout])

# Define XOR node for Soil Mix and Install Beds
xor2 = OperatorPOWL(operator=Operator.XOR, children=[SoilMix, InstallBeds])

# Define XOR node for Irrigation Set and Climate Test
xor3 = OperatorPOWL(operator=Operator.XOR, children=[IrrigationSet, ClimateTest])

# Define XOR node for Sensor Deploy and Energy Setup
xor4 = OperatorPOWL(operator=Operator.XOR, children=[SensorDeploy, EnergySetup])

# Define XOR node for Crop Select and Plant Seeding
xor5 = OperatorPOWL(operator=Operator.XOR, children=[CropSelect, PlantSeeding])

# Define XOR node for Community Meet and Compliance Check
xor6 = OperatorPOWL(operator=Operator.XOR, children=[CommunityMeet, ComplianceCheck])

# Define XOR node for Growth Monitor and Harvest Plan
xor7 = OperatorPOWL(operator=Operator.XOR, children=[GrowthMonitor, HarvestPlan])

# Define XOR node for Waste Recycle and Permit Review
xor8 = OperatorPOWL(operator=Operator.XOR, children=[WasteRecycle, PermitReview])

# Define XOR node for Crop Select and Plant Seeding
xor9 = OperatorPOWL(operator=Operator.XOR, children=[CropSelect, PlantSeeding])

# Define XOR node for Sensor Deploy and Energy Setup
xor10 = OperatorPOWL(operator=Operator.XOR, children=[SensorDeploy, EnergySetup])

# Define XOR node for Irrigation Set and Climate Test
xor11 = OperatorPOWL(operator=Operator.XOR, children=[IrrigationSet, ClimateTest])

# Define XOR node for Soil Mix and Install Beds
xor12 = OperatorPOWL(operator=Operator.XOR, children=[SoilMix, InstallBeds])

# Define XOR node for Permit Review and Compliance Check
xor13 = OperatorPOWL(operator=Operator.XOR, children=[PermitReview, ComplianceCheck])

# Define XOR node for Site Survey and Design Layout
xor14 = OperatorPOWL(operator=Operator.XOR, children=[SiteSurvey, DesignLayout])

# Define XOR node for Load Assess and Permit Review
xor15 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, PermitReview])

# Define XOR node for Load Assess and Site Survey
xor16 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SiteSurvey])

# Define XOR node for Load Assess and Design Layout
xor17 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, DesignLayout])

# Define XOR node for Load Assess and Soil Mix
xor18 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SoilMix])

# Define XOR node for Load Assess and Install Beds
xor19 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, InstallBeds])

# Define XOR node for Load Assess and Irrigation Set
xor20 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, IrrigationSet])

# Define XOR node for Load Assess and Climate Test
xor21 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, ClimateTest])

# Define XOR node for Load Assess and Sensor Deploy
xor22 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SensorDeploy])

# Define XOR node for Load Assess and Energy Setup
xor23 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, EnergySetup])

# Define XOR node for Load Assess and Crop Select
xor24 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, CropSelect])

# Define XOR node for Load Assess and Plant Seeding
xor25 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, PlantSeeding])

# Define XOR node for Load Assess and Community Meet
xor26 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, CommunityMeet])

# Define XOR node for Load Assess and Compliance Check
xor27 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, ComplianceCheck])

# Define XOR node for Load Assess and Growth Monitor
xor28 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, GrowthMonitor])

# Define XOR node for Load Assess and Harvest Plan
xor29 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, HarvestPlan])

# Define XOR node for Load Assess and Waste Recycle
xor30 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, WasteRecycle])

# Define XOR node for Load Assess and Permit Review
xor31 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, PermitReview])

# Define XOR node for Load Assess and Site Survey
xor32 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SiteSurvey])

# Define XOR node for Load Assess and Design Layout
xor33 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, DesignLayout])

# Define XOR node for Load Assess and Soil Mix
xor34 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SoilMix])

# Define XOR node for Load Assess and Install Beds
xor35 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, InstallBeds])

# Define XOR node for Load Assess and Irrigation Set
xor36 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, IrrigationSet])

# Define XOR node for Load Assess and Climate Test
xor37 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, ClimateTest])

# Define XOR node for Load Assess and Sensor Deploy
xor38 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SensorDeploy])

# Define XOR node for Load Assess and Energy Setup
xor39 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, EnergySetup])

# Define XOR node for Load Assess and Crop Select
xor40 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, CropSelect])

# Define XOR node for Load Assess and Plant Seeding
xor41 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, PlantSeeding])

# Define XOR node for Load Assess and Community Meet
xor42 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, CommunityMeet])

# Define XOR node for Load Assess and Compliance Check
xor43 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, ComplianceCheck])

# Define XOR node for Load Assess and Growth Monitor
xor44 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, GrowthMonitor])

# Define XOR node for Load Assess and Harvest Plan
xor45 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, HarvestPlan])

# Define XOR node for Load Assess and Waste Recycle
xor46 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, WasteRecycle])

# Define XOR node for Load Assess and Permit Review
xor47 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, PermitReview])

# Define XOR node for Load Assess and Site Survey
xor48 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SiteSurvey])

# Define XOR node for Load Assess and Design Layout
xor49 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, DesignLayout])

# Define XOR node for Load Assess and Soil Mix
xor50 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SoilMix])

# Define XOR node for Load Assess and Install Beds
xor51 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, InstallBeds])

# Define XOR node for Load Assess and Irrigation Set
xor52 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, IrrigationSet])

# Define XOR node for Load Assess and Climate Test
xor53 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, ClimateTest])

# Define XOR node for Load Assess and Sensor Deploy
xor54 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SensorDeploy])

# Define XOR node for Load Assess and Energy Setup
xor55 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, EnergySetup])

# Define XOR node for Load Assess and Crop Select
xor56 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, CropSelect])

# Define XOR node for Load Assess and Plant Seeding
xor57 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, PlantSeeding])

# Define XOR node for Load Assess and Community Meet
xor58 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, CommunityMeet])

# Define XOR node for Load Assess and Compliance Check
xor59 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, ComplianceCheck])

# Define XOR node for Load Assess and Growth Monitor
xor60 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, GrowthMonitor])

# Define XOR node for Load Assess and Harvest Plan
xor61 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, HarvestPlan])

# Define XOR node for Load Assess and Waste Recycle
xor62 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, WasteRecycle])

# Define XOR node for Load Assess and Permit Review
xor63 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, PermitReview])

# Define XOR node for Load Assess and Site Survey
xor64 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SiteSurvey])

# Define XOR node for Load Assess and Design Layout
xor65 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, DesignLayout])

# Define XOR node for Load Assess and Soil Mix
xor66 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SoilMix])

# Define XOR node for Load Assess and Install Beds
xor67 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, InstallBeds])

# Define XOR node for Load Assess and Irrigation Set
xor68 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, IrrigationSet])

# Define XOR node for Load Assess and Climate Test
xor69 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, ClimateTest])

# Define XOR node for Load Assess and Sensor Deploy
xor70 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SensorDeploy])

# Define XOR node for Load Assess and Energy Setup
xor71 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, EnergySetup])

# Define XOR node for Load Assess and Crop Select
xor72 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, CropSelect])

# Define XOR node for Load Assess and Plant Seeding
xor73 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, PlantSeeding])

# Define XOR node for Load Assess and Community Meet
xor74 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, CommunityMeet])

# Define XOR node for Load Assess and Compliance Check
xor75 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, ComplianceCheck])

# Define XOR node for Load Assess and Growth Monitor
xor76 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, GrowthMonitor])

# Define XOR node for Load Assess and Harvest Plan
xor77 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, HarvestPlan])

# Define XOR node for Load Assess and Waste Recycle
xor78 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, WasteRecycle])

# Define XOR node for Load Assess and Permit Review
xor79 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, PermitReview])

# Define XOR node for Load Assess and Site Survey
xor80 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SiteSurvey])

# Define XOR node for Load Assess and Design Layout
xor81 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, DesignLayout])

# Define XOR node for Load Assess and Soil Mix
xor82 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SoilMix])

# Define XOR node for Load Assess and Install Beds
xor83 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, InstallBeds])

# Define XOR node for Load Assess and Irrigation Set
xor84 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, IrrigationSet])

# Define XOR node for Load Assess and Climate Test
xor85 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, ClimateTest])

# Define XOR node for Load Assess and Sensor Deploy
xor86 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SensorDeploy])

# Define XOR node for Load Assess and Energy Setup
xor87 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, EnergySetup])

# Define XOR node for Load Assess and Crop Select
xor88 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, CropSelect])

# Define XOR node for Load Assess and Plant Seeding
xor89 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, PlantSeeding])

# Define XOR node for Load Assess and Community Meet
xor90 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, CommunityMeet])

# Define XOR node for Load Assess and Compliance Check
xor91 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, ComplianceCheck])

# Define XOR node for Load Assess and Growth Monitor
xor92 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, GrowthMonitor])

# Define XOR node for Load Assess and Harvest Plan
xor93 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, HarvestPlan])

# Define XOR node for Load Assess and Waste Recycle
xor94 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, WasteRecycle])

# Define XOR node for Load Assess and Permit Review
xor95 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, PermitReview])

# Define XOR node for Load Assess and Site Survey
xor96 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SiteSurvey])

# Define XOR node for Load Assess and Design Layout
xor97 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, DesignLayout])

# Define XOR node for Load Assess and Soil Mix
xor98 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SoilMix])

# Define XOR node for Load Assess and Install Beds
xor99 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, InstallBeds])

# Define XOR node for Load Assess and Irrigation Set
xor100 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, IrrigationSet])

# Define XOR node for Load Assess and Climate Test
xor101 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, ClimateTest])

# Define XOR node for Load Assess and Sensor Deploy
xor102 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SensorDeploy])

# Define XOR node for Load Assess and Energy Setup
xor103 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, EnergySetup])

# Define XOR node for Load Assess and Crop Select
xor104 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, CropSelect])

# Define XOR node for Load Assess and Plant Seeding
xor105 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, PlantSeeding])

# Define XOR node for Load Assess and Community Meet
xor106 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, CommunityMeet])

# Define XOR node for Load Assess and Compliance Check
xor107 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, ComplianceCheck])

# Define XOR node for Load Assess and Growth Monitor
xor108 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, GrowthMonitor])

# Define XOR node for Load Assess and Harvest Plan
xor109 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, HarvestPlan])

# Define XOR node for Load Assess and Waste Recycle
xor110 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, WasteRecycle])

# Define XOR node for Load Assess and Permit Review
xor111 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, PermitReview])

# Define XOR node for Load Assess and Site Survey
xor112 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SiteSurvey])

# Define XOR node for Load Assess and Design Layout
xor113 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, DesignLayout])

# Define XOR node for Load Assess and Soil Mix
xor114 = OperatorPOWL(operator=Operator.XOR, children=[LoadAssess, SoilMix])

# Define XOR node for Load Assess and Install Beds
xor115 = OperatorPOWL(operator