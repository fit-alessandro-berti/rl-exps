import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Define the sequence of activities
sequence = [SiteAssess, StructureCheck, SoilTest, ClimateEval, PermitObtain, DesignLayout, SeedSourcing, IrrigationSet, NutrientMix, PestControl, SensorInstall, StaffTrain, CropPlanting, YieldMonitor, MarketSetup, Maintenance, WasteManage]

# Create a loop for continuous monitoring and adaptive maintenance
loop = OperatorPOWL(operator=Operator.LOOP, children=[Maintenance, WasteManage])

# Create a choice for the yield monitor and market setup
yield_monitor_market_setup = OperatorPOWL(operator=Operator.XOR, children=[YieldMonitor, MarketSetup])

# Create a partial order for the entire process
root = StrictPartialOrder(nodes=sequence + [loop, yield_monitor_market_setup])
root.order.add_edge(loop, yield_monitor_market_setup)

print(root)