import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SiteSurvey = Transition(label='Site Survey')
PermitFiling = Transition(label='Permit Filing')
StructurePrep = Transition(label='Structure Prep')
SystemInstall = Transition(label='System Install')
NutrientMix = Transition(label='Nutrient Mix')
SensorSetup = Transition(label='Sensor Setup')
AICalibration = Transition(label='AI Calibration')
SeedSourcing = Transition(label='Seed Sourcing')
StaffTraining = Transition(label='Staff Training')
EnergyConnect = Transition(label='Energy Connect')
WaterCycle = Transition(label='Water Cycle')
GrowthMonitor = Transition(label='Growth Monitor')
WasteAudit = Transition(label='Waste Audit')
CommunityMeet = Transition(label='Community Meet')
DataReview = Transition(label='Data Review')
YieldForecast = Transition(label='Yield Forecast')

# Define silent transitions (if applicable)
skip = SilentTransition()

# Define operators for choice and loop structures
xor = OperatorPOWL(operator=Operator.XOR, children=[YieldForecast, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[SiteSurvey, PermitFiling, StructurePrep, SystemInstall, NutrientMix, SensorSetup, AICalibration, SeedSourcing, StaffTraining, EnergyConnect, WaterCycle, GrowthMonitor, WasteAudit, CommunityMeet, DataReview])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)