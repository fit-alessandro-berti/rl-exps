import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
SiteAssess = Transition(label='Site Assess')
StructureCheck = Transition(label='Structure Check')
PermitObtain = Transition(label='Permit Obtain')
MaterialSource = Transition(label='Material Source')
SoilPrepare = Transition(label='Soil Prepare')
WaterproofRoof = Transition(label='Waterproof Roof')
IrrigationSetup = Transition(label='Irrigation Setup')
BedAssemble = Transition(label='Bed Assemble')
CropPlan = Transition(label='Crop Plan')
PestMonitor = Transition(label='Pest Monitor')
NutrientCalibrate = Transition(label='Nutrient Calibrate')
HarvestSchedule = Transition(label='Harvest Schedule')
CommunityTrain = Transition(label='Community Train')
YieldRecord = Transition(label='Yield Record')
ImpactReview = Transition(label='Impact Review')

# Define the silent transition
skip = SilentTransition()

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[CropPlan, PestMonitor, NutrientCalibrate, HarvestSchedule, CommunityTrain, YieldRecord, ImpactReview])

# Define the XOR
xor = OperatorPOWL(operator=Operator.XOR, children=[BedAssemble, skip])

# Define the root
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)