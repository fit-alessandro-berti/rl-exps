import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteAssess, StructureCheck])
xor = OperatorPOWL(operator=Operator.XOR, children=[PermitObtain, skip])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[MaterialSource, SoilPrepare])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[WaterproofRoof, skip])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[IrrigationSetup, BedAssemble])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[CropPlan, skip])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[PestMonitor, NutrientCalibrate])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[HarvestSchedule, skip])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[CommunityTrain, YieldRecord])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[ImpactReview, skip])

root = StrictPartialOrder(nodes=[loop, xor, loop2, xor2, loop3, xor3, loop4, xor4, loop5, xor5])
root.order.add_edge(loop, xor)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)
root.order.add_edge(loop5, xor5)