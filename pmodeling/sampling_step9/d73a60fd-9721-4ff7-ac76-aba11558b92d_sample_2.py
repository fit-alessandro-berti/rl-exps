import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SiteSurvey = Transition(label='Site Survey')
StructuralAudit = Transition(label='Structural Audit')
SystemDesign = Transition(label='System Design')
PermitFiling = Transition(label='Permit Filing')
FoundationPrep = Transition(label='Foundation Prep')
FrameBuild = Transition(label='Frame Build')
IrrigationSetup = Transition(label='Irrigation Setup')
LightingInstall = Transition(label='Lighting Install')
ClimateControl = Transition(label='Climate Control')
NutrientMix = Transition(label='Nutrient Mix')
CropPlanting = Transition(label='Crop Planting')
PestScouting = Transition(label='Pest Scouting')
DataMonitoring = Transition(label='Data Monitoring')
WasteSorting = Transition(label='Waste Sorting')
EnergyAudit = Transition(label='Energy Audit')
CommunityMeet = Transition(label='Community Meet')
YieldAnalysis = Transition(label='Yield Analysis')

# Define silent transitions
skip = SilentTransition()

# Define the loop for the pest scouting process
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[PestScouting, skip])

# Define the XOR for data monitoring and community meet
data_xor = OperatorPOWL(operator=Operator.XOR, children=[DataMonitoring, CommunityMeet])

# Define the partial order
root = StrictPartialOrder(nodes=[pest_loop, data_xor])

# Define the order dependencies
root.order.add_edge(pest_loop, data_xor)

# Print the root of the POWL model
print(root)