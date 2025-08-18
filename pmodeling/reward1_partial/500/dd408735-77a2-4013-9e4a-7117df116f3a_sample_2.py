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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    SiteAssess, StructureCheck, SoilTest, ClimateEval, PermitObtain, DesignLayout, SeedSourcing, IrrigationSet, NutrientMix, PestControl, SensorInstall, StaffTrain, CropPlanting, YieldMonitor, MarketSetup, Maintenance, WasteManage
])

# Define the dependencies (partial order)
root.order.add_edge(SiteAssess, StructureCheck)
root.order.add_edge(StructureCheck, SoilTest)
root.order.add_edge(SoilTest, ClimateEval)
root.order.add_edge(ClimateEval, PermitObtain)
root.order.add_edge(PermitObtain, DesignLayout)
root.order.add_edge(DesignLayout, SeedSourcing)
root.order.add_edge(SeedSourcing, IrrigationSet)
root.order.add_edge(IrrigationSet, NutrientMix)
root.order.add_edge(NutrientMix, PestControl)
root.order.add_edge(PestControl, SensorInstall)
root.order.add_edge(SensorInstall, StaffTrain)
root.order.add_edge(StaffTrain, CropPlanting)
root.order.add_edge(CropPlanting, YieldMonitor)
root.order.add_edge(YieldMonitor, MarketSetup)
root.order.add_edge(MarketSetup, Maintenance)
root.order.add_edge(Maintenance, WasteManage)

# Print the final POWL model
print(root)