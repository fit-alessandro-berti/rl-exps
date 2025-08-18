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

# Define the structure of the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[CropPlan, PestMonitor, NutrientCalibrate])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[CommunityTrain, YieldRecord, ImpactReview])

root = StrictPartialOrder(nodes=[SiteAssess, StructureCheck, PermitObtain, MaterialSource, SoilPrepare, WaterproofRoof, IrrigationSetup, BedAssemble, loop1, loop2])
root.order.add_edge(SiteAssess, StructureCheck)
root.order.add_edge(StructureCheck, PermitObtain)
root.order.add_edge(PermitObtain, MaterialSource)
root.order.add_edge(MaterialSource, SoilPrepare)
root.order.add_edge(SoilPrepare, WaterproofRoof)
root.order.add_edge(WaterproofRoof, IrrigationSetup)
root.order.add_edge(IrrigationSetup, BedAssemble)
root.order.add_edge(BedAssemble, loop1)
root.order.add_edge(BedAssemble, loop2)