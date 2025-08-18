import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SiteSelect = Transition(label='Site Select')
EnvAssess = Transition(label='Env Assess')
DesignModules = Transition(label='Design Modules')
HydroponicsSetup = Transition(label='Hydroponics Setup')
SoftwareDev = Transition(label='Software Dev')
SeedChoose = Transition(label='Seed Choose')
LEDInstall = Transition(label='LED Install')
TrainStaff = Transition(label='Train Staff')
ComplianceCheck = Transition(label='Compliance Check')
EngageCommunity = Transition(label='Engage Community')
PlantCrops = Transition(label='Plant Crops')
MonitorGrowth = Transition(label='Monitor Growth')
OptimizeYields = Transition(label='Optimize Yields')
WasteManage = Transition(label='Waste Manage')
EnergyAudit = Transition(label='Energy Audit')
WaterRecycle = Transition(label='Water Recycle')

# Define partial order with dependencies
root = StrictPartialOrder(
    nodes=[
        SiteSelect, EnvAssess, DesignModules, HydroponicsSetup, SoftwareDev, SeedChoose, LEDInstall, TrainStaff,
        ComplianceCheck, EngageCommunity, PlantCrops, MonitorGrowth, OptimizeYields, WasteManage, EnergyAudit,
        WaterRecycle
    ],
    order=[
        (SiteSelect, EnvAssess),
        (EnvAssess, DesignModules),
        (DesignModules, HydroponicsSetup),
        (HydroponicsSetup, SoftwareDev),
        (SoftwareDev, SeedChoose),
        (SeedChoose, LEDInstall),
        (LEDInstall, TrainStaff),
        (TrainStaff, ComplianceCheck),
        (ComplianceCheck, EngageCommunity),
        (EngageCommunity, PlantCrops),
        (PlantCrops, MonitorGrowth),
        (MonitorGrowth, OptimizeYields),
        (OptimizeYields, WasteManage),
        (WasteManage, EnergyAudit),
        (EnergyAudit, WaterRecycle)
    ]
)

print(root)