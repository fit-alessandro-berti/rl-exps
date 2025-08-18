import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SiteAssess = Transition(label='Site Assess')
StructureCheck = Transition(label='Structure Check')
SoilTest = Transition(label='Soil Test')
ClimateEval = Transition(label='Climate Eval')
PermitObtain = Transition(label='Permit Obtain')
DesignLayout = Transition(label='Design Layout')
SeedSourcing = Transition(label='Seed Sourcing')
IrrigationSet = Transition(label='Irrigation Set')
NutrientMix = Transition(label='Nutrient Mix')
PestControl = Transition(label='Pest Control')
SensorInstall = Transition(label='Sensor Install')
StaffTrain = Transition(label='Staff Train')
CropPlanting = Transition(label='Crop Planting')
YieldMonitor = Transition(label='Yield Monitor')
MarketSetup = Transition(label='Market Setup')
Maintenance = Transition(label='Maintenance')
WasteManage = Transition(label='Waste Manage')

# Define silent transitions (e.g., for skipping steps)
skip = SilentTransition()

# Define loops and choices
loopSiteAssess = OperatorPOWL(operator=Operator.LOOP, children=[SiteAssess, StructureCheck, SoilTest, ClimateEval])
loopPermit = OperatorPOWL(operator=Operator.LOOP, children=[PermitObtain, DesignLayout, SeedSourcing, IrrigationSet, NutrientMix, PestControl, SensorInstall, StaffTrain, CropPlanting, YieldMonitor, MarketSetup])
loopMaintenance = OperatorPOWL(operator=Operator.LOOP, children=[Maintenance, WasteManage])

# Define the root model
root = StrictPartialOrder(nodes=[loopSiteAssess, loopPermit, loopMaintenance])
root.order.add_edge(loopSiteAssess, loopPermit)
root.order.add_edge(loopPermit, loopMaintenance)

# Print the root model
print(root)