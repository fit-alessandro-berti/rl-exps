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

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[CropPlan, PestMonitor, NutrientCalibrate])

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[WaterproofRoof, IrrigationSetup, BedAssemble])

# Create the root node
root = StrictPartialOrder(nodes=[SiteAssess, StructureCheck, PermitObtain, MaterialSource, SoilPrepare, xor, loop, CommunityTrain, YieldRecord, ImpactReview])

# Define the dependencies
root.order.add_edge(SiteAssess, StructureCheck)
root.order.add_edge(SiteAssess, PermitObtain)
root.order.add_edge(SiteAssess, MaterialSource)
root.order.add_edge(SiteAssess, SoilPrepare)
root.order.add_edge(StructureCheck, PermitObtain)
root.order.add_edge(StructureCheck, MaterialSource)
root.order.add_edge(StructureCheck, SoilPrepare)
root.order.add_edge(PermitObtain, WaterproofRoof)
root.order.add_edge(PermitObtain, IrrigationSetup)
root.order.add_edge(PermitObtain, BedAssemble)
root.order.add_edge(MaterialSource, WaterproofRoof)
root.order.add_edge(MaterialSource, IrrigationSetup)
root.order.add_edge(MaterialSource, BedAssemble)
root.order.add_edge(SoilPrepare, WaterproofRoof)
root.order.add_edge(SoilPrepare, IrrigationSetup)
root.order.add_edge(SoilPrepare, BedAssemble)
root.order.add_edge(WaterproofRoof, CropPlan)
root.order.add_edge(IrrigationSetup, CropPlan)
root.order.add_edge(BedAssemble, CropPlan)
root.order.add_edge(CropPlan, PestMonitor)
root.order.add_edge(CropPlan, NutrientCalibrate)
root.order.add_edge(PestMonitor, NutrientCalibrate)
root.order.add_edge(NutrientCalibrate, HarvestSchedule)
root.order.add_edge(HarvestSchedule, CommunityTrain)
root.order.add_edge(CommunityTrain, YieldRecord)
root.order.add_edge(YieldRecord, ImpactReview)

# Print the root node
print(root)