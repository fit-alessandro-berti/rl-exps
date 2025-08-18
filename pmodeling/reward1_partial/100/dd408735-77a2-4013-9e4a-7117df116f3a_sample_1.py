import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        SiteAssess,
        StructureCheck,
        SoilTest,
        ClimateEval,
        PermitObtain,
        DesignLayout,
        SeedSourcing,
        IrrigationSet,
        NutrientMix,
        PestControl,
        SensorInstall,
        StaffTrain,
        CropPlanting,
        YieldMonitor,
        MarketSetup,
        Maintenance,
        WasteManage
    ],
    order=[
        (SiteAssess, StructureCheck),
        (SiteAssess, SoilTest),
        (SiteAssess, ClimateEval),
        (SiteAssess, PermitObtain),
        (StructureCheck, DesignLayout),
        (StructureCheck, IrrigationSet),
        (StructureCheck, NutrientMix),
        (SoilTest, DesignLayout),
        (SoilTest, IrrigationSet),
        (SoilTest, NutrientMix),
        (ClimateEval, DesignLayout),
        (ClimateEval, IrrigationSet),
        (ClimateEval, NutrientMix),
        (PermitObtain, DesignLayout),
        (PermitObtain, IrrigationSet),
        (PermitObtain, NutrientMix),
        (DesignLayout, PestControl),
        (DesignLayout, SensorInstall),
        (DesignLayout, StaffTrain),
        (IrrigationSet, PestControl),
        (IrrigationSet, SensorInstall),
        (IrrigationSet, StaffTrain),
        (NutrientMix, PestControl),
        (NutrientMix, SensorInstall),
        (NutrientMix, StaffTrain),
        (PestControl, CropPlanting),
        (PestControl, YieldMonitor),
        (SensorInstall, CropPlanting),
        (SensorInstall, YieldMonitor),
        (StaffTrain, CropPlanting),
        (StaffTrain, YieldMonitor),
        (CropPlanting, MarketSetup),
        (CropPlanting, Maintenance),
        (YieldMonitor, MarketSetup),
        (YieldMonitor, Maintenance),
        (MarketSetup, WasteManage),
        (Maintenance, WasteManage)
    ]
)

# Print the root POWL model
print(root)