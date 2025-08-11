import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
SeedSelect = Transition(label='Seed Select')
ClimateMap = Transition(label='Climate Map')
IoTSetup = Transition(label='IoT Setup')
NutrientMix = Transition(label='Nutrient Mix')
SensorCheck = Transition(label='Sensor Check')
LightAdjust = Transition(label='Light Adjust')
WaterCycle = Transition(label='Water Cycle')
PestScan = Transition(label='Pest Scan')
GrowthAudit = Transition(label='Growth Audit')
HarvestPlan = Transition(label='Harvest Plan')
DemandSync = Transition(label='Demand Sync')
QualityGrade = Transition(label='Quality Grade')
PackItems = Transition(label='Pack Items')
WasteCompost = Transition(label='Waste Compost')
DataReview = Transition(label='Data Review')
CycleReset = Transition(label='Cycle Reset')

# Define silent transitions
Skip = SilentTransition()

# Define loop
Loop = OperatorPOWL(operator=Operator.LOOP, children=[SeedSelect, ClimateMap, IoTSetup, NutrientMix, SensorCheck, LightAdjust, WaterCycle, PestScan, GrowthAudit, HarvestPlan, DemandSync, QualityGrade, PackItems, WasteCompost, DataReview, CycleReset])

# Define XOR
XOR = OperatorPOWL(operator=Operator.XOR, children=[Loop, Skip])

# Define root
root = StrictPartialOrder(nodes=[Loop, XOR])
root.order.add_edge(Loop, XOR)

print(root)