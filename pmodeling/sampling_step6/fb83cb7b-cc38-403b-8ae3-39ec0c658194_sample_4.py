import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their exact names
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

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[SiteAssess, StructureCheck, PermitObtain, MaterialSource, SoilPrepare, WaterproofRoof, IrrigationSetup, BedAssemble, CropPlan, PestMonitor, NutrientCalibrate, HarvestSchedule, CommunityTrain, YieldRecord, ImpactReview])

# The order of the nodes is defined by the sequence of the nodes in the list above.
# No additional edges are needed as the activities are listed in a sequential manner.