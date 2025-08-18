import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
SiteSurvey = Transition(label='Site Survey')
StructuralCheck = Transition(label='Structural Check')
EnvControl = Transition(label='Env Control')
HydroSetup = Transition(label='Hydro Setup')
CropSelect = Transition(label='Crop Select')
IoTInstall = Transition(label='IoT Install')
SensorCalibrate = Transition(label='Sensor Calibrate')
WaterCycle = Transition(label='Water Cycle')
NutrientMix = Transition(label='Nutrient Mix')
LightingAdjust = Transition(label='Lighting Adjust')
StaffTrain = Transition(label='Staff Train')
WasteManage = Transition(label='Waste Manage')
EnergyAudit = Transition(label='Energy Audit')
HarvestPlan = Transition(label='Harvest Plan')
DeliverySetup = Transition(label='Delivery Setup')
MarketAlign = Transition(label='Market Align')

# Define the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey,
    StructuralCheck,
    EnvControl,
    HydroSetup,
    CropSelect,
    IoTInstall,
    SensorCalibrate,
    WaterCycle,
    NutrientMix,
    LightingAdjust,
    StaffTrain,
    WasteManage,
    EnergyAudit,
    HarvestPlan,
    DeliverySetup,
    MarketAlign
])

# Define the dependencies between activities
root.order.add_edge(SiteSurvey, StructuralCheck)
root.order.add_edge(SiteSurvey, EnvControl)
root.order.add_edge(SiteSurvey, HydroSetup)
root.order.add_edge(SiteSurvey, CropSelect)
root.order.add_edge(SiteSurvey, IoTInstall)
root.order.add_edge(SiteSurvey, SensorCalibrate)
root.order.add_edge(SiteSurvey, WaterCycle)
root.order.add_edge(SiteSurvey, NutrientMix)
root.order.add_edge(SiteSurvey, LightingAdjust)
root.order.add_edge(SiteSurvey, StaffTrain)
root.order.add_edge(SiteSurvey, WasteManage)
root.order.add_edge(SiteSurvey, EnergyAudit)
root.order.add_edge(SiteSurvey, HarvestPlan)
root.order.add_edge(SiteSurvey, DeliverySetup)
root.order.add_edge(SiteSurvey, MarketAlign)

# Add the edges to establish the partial order
root.order.add_edge(StructuralCheck, EnvControl)
root.order.add_edge(StructuralCheck, HydroSetup)
root.order.add_edge(StructuralCheck, CropSelect)
root.order.add_edge(StructuralCheck, IoTInstall)
root.order.add_edge(StructuralCheck, SensorCalibrate)
root.order.add_edge(StructuralCheck, WaterCycle)
root.order.add_edge(StructuralCheck, NutrientMix)
root.order.add_edge(StructuralCheck, LightingAdjust)
root.order.add_edge(StructuralCheck, StaffTrain)
root.order.add_edge(StructuralCheck, WasteManage)
root.order.add_edge(StructuralCheck, EnergyAudit)
root.order.add_edge(StructuralCheck, HarvestPlan)
root.order.add_edge(StructuralCheck, DeliverySetup)
root.order.add_edge(StructuralCheck, MarketAlign)

root.order.add_edge(EnvControl, HydroSetup)
root.order.add_edge(EnvControl, CropSelect)
root.order.add_edge(EnvControl, IoTInstall)
root.order.add_edge(EnvControl, SensorCalibrate)
root.order.add_edge(EnvControl, WaterCycle)
root.order.add_edge(EnvControl, NutrientMix)
root.order.add_edge(EnvControl, LightingAdjust)
root.order.add_edge(EnvControl, StaffTrain)
root.order.add_edge(EnvControl, WasteManage)
root.order.add_edge(EnvControl, EnergyAudit)
root.order.add_edge(EnvControl, HarvestPlan)
root.order.add_edge(EnvControl, DeliverySetup)
root.order.add_edge(EnvControl, MarketAlign)

root.order.add_edge(HydroSetup, CropSelect)
root.order.add_edge(HydroSetup, IoTInstall)
root.order.add_edge(HydroSetup, SensorCalibrate)
root.order.add_edge(HydroSetup, WaterCycle)
root.order.add_edge(HydroSetup, NutrientMix)
root.order.add_edge(HydroSetup, LightingAdjust)
root.order.add_edge(HydroSetup, StaffTrain)
root.order.add_edge(HydroSetup, WasteManage)
root.order.add_edge(HydroSetup, EnergyAudit)
root.order.add_edge(HydroSetup, HarvestPlan)
root.order.add_edge(HydroSetup, DeliverySetup)
root.order.add_edge(HydroSetup, MarketAlign)

root.order.add_edge(CropSelect, IoTInstall)
root.order.add_edge(CropSelect, SensorCalibrate)
root.order.add_edge(CropSelect, WaterCycle)
root.order.add_edge(CropSelect, NutrientMix)
root.order.add_edge(CropSelect, LightingAdjust)
root.order.add_edge(CropSelect, StaffTrain)
root.order.add_edge(CropSelect, WasteManage)
root.order.add_edge(CropSelect, EnergyAudit)
root.order.add_edge(CropSelect, HarvestPlan)
root.order.add_edge(CropSelect, DeliverySetup)
root.order.add_edge(CropSelect, MarketAlign)

root.order.add_edge(IoTInstall, SensorCalibrate)
root.order.add_edge(IoTInstall, WaterCycle)
root.order.add_edge(IoTInstall, NutrientMix)
root.order.add_edge(IoTInstall, LightingAdjust)
root.order.add_edge(IoTInstall, StaffTrain)
root.order.add_edge(IoTInstall, WasteManage)
root.order.add_edge(IoTInstall, EnergyAudit)
root.order.add_edge(IoTInstall, HarvestPlan)
root.order.add_edge(IoTInstall, DeliverySetup)
root.order.add_edge(IoTInstall, MarketAlign)

root.order.add_edge(SensorCalibrate, WaterCycle)
root.order.add_edge(SensorCalibrate, NutrientMix)
root.order.add_edge(SensorCalibrate, LightingAdjust)
root.order.add_edge(SensorCalibrate, StaffTrain)
root.order.add_edge(SensorCalibrate, WasteManage)
root.order.add_edge(SensorCalibrate, EnergyAudit)
root.order.add_edge(SensorCalibrate, HarvestPlan)
root.order.add_edge(SensorCalibrate, DeliverySetup)
root.order.add_edge(SensorCalibrate, MarketAlign)

root.order.add_edge(WaterCycle, NutrientMix)
root.order.add_edge(WaterCycle, LightingAdjust)
root.order.add_edge(WaterCycle, StaffTrain)
root.order.add_edge(WaterCycle, WasteManage)
root.order.add_edge(WaterCycle, EnergyAudit)
root.order.add_edge(WaterCycle, HarvestPlan)
root.order.add_edge(WaterCycle, DeliverySetup)
root.order.add_edge(WaterCycle, MarketAlign)

root.order.add_edge(NutrientMix, LightingAdjust)
root.order.add_edge(NutrientMix, StaffTrain)
root.order.add_edge(NutrientMix, WasteManage)
root.order.add_edge(NutrientMix, EnergyAudit)
root.order.add_edge(NutrientMix, HarvestPlan)
root.order.add_edge(NutrientMix, DeliverySetup)
root.order.add_edge(NutrientMix, MarketAlign)

root.order.add_edge(LightingAdjust, StaffTrain)
root.order.add_edge(LightingAdjust, WasteManage)
root.order.add_edge(LightingAdjust, EnergyAudit)
root.order.add_edge(LightingAdjust, HarvestPlan)
root.order.add_edge(LightingAdjust, DeliverySetup)
root.order.add_edge(LightingAdjust, MarketAlign)

root.order.add_edge(StaffTrain, WasteManage)
root.order.add_edge(StaffTrain, EnergyAudit)
root.order.add_edge(StaffTrain, HarvestPlan)
root.order.add_edge(StaffTrain, DeliverySetup)
root.order.add_edge(StaffTrain, MarketAlign)

root.order.add_edge(WasteManage, EnergyAudit)
root.order.add_edge(WasteManage, HarvestPlan)
root.order.add_edge(WasteManage, DeliverySetup)
root.order.add_edge(WasteManage, MarketAlign)

root.order.add_edge(EnergyAudit, HarvestPlan)
root.order.add_edge(EnergyAudit, DeliverySetup)
root.order.add_edge(EnergyAudit, MarketAlign)

root.order.add_edge(HarvestPlan, DeliverySetup)
root.order.add_edge(HarvestPlan, MarketAlign)

root.order.add_edge(DeliverySetup, MarketAlign)

print(root)