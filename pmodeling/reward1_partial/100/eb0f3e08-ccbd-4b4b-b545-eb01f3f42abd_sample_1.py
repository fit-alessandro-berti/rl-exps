from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) with their labels
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

# Define silent transitions
Skip = SilentTransition()

# Define the partial order structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[DataCollection, WeatherCheck, SoilTesting, CropSelection, ResourceAssign, IrrigationAdjust, PestScan, NutrientMix, GrowthMonitor])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[CommunityPoll, ScheduleUpdate, HarvestPlan, WasteSort])
xor = OperatorPOWL(operator=Operator.XOR, children=[YieldReport, Skip])

# Create the root partial order
root = StrictPartialOrder(nodes=[loop1, loop2, xor])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor)

print(root)