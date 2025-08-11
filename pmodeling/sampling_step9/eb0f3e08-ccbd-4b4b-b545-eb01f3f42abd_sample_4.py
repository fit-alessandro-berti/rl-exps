import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SensorSetup = Transition(label='Sensor Setup')
DataCollection = Transition(label='Data Collection')
WeatherCheck = Transition(label='Weather Check')
SoilTesting = Transition(label='Soil Testing')
CropSelection = Transition(label='Crop Selection')
ResourceAssign = Transition(label='Resource Assign')
IrrigationAdjust = Transition(label='Irrigation Adjust')
PestScan = Transition(label='Pest Scan')
NutrientMix = Transition(label='Nutrient Mix')
GrowthMonitor = Transition(label='Growth Monitor')
CommunityPoll = Transition(label='Community Poll')
ScheduleUpdate = Transition(label='Schedule Update')
HarvestPlan = Transition(label='Harvest Plan')
WasteSort = Transition(label='Waste Sort')
YieldReport = Transition(label='Yield Report')

skip = SilentTransition()
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[SensorSetup, DataCollection, WeatherCheck, SoilTesting, CropSelection, ResourceAssign, IrrigationAdjust, PestScan, NutrientMix, GrowthMonitor, CommunityPoll, ScheduleUpdate, HarvestPlan, WasteSort, YieldReport])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[WasteSort, YieldReport])
root = StrictPartialOrder(nodes=[loop1, xor1])
root.order.add_edge(loop1, xor1)