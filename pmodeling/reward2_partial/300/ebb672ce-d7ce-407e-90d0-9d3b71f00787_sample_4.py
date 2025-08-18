from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
ModularBuild = Transition(label='Modular Build')
InstallPumps = Transition(label='Install Pumps')
SetupSensors = Transition(label='Setup Sensors')
CalibrateLights = Transition(label='Calibrate Lights')
NutrientMix = Transition(label='Nutrient Mix')
PlantSeeding = Transition(label='Plant Seeding')
WaterCycling = Transition(label='Water Cycling')
EnergyAudit = Transition(label='Energy Audit')
PestControl = Transition(label='Pest Control')
GrowthMonitor = Transition(label='Growth Monitor')
DataAnalysis = Transition(label='Data Analysis')
YieldForecast = Transition(label='Yield Forecast')
SupplyOrder = Transition(label='Supply Order')
WasteRecycle = Transition(label='Waste Recycle')
SystemUpgrade = Transition(label='System Upgrade')

# Define the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey,
    DesignLayout,
    ModularBuild,
    InstallPumps,
    SetupSensors,
    CalibrateLights,
    NutrientMix,
    PlantSeeding,
    WaterCycling,
    EnergyAudit,
    PestControl,
    GrowthMonitor,
    DataAnalysis,
    YieldForecast,
    SupplyOrder,
    WasteRecycle,
    SystemUpgrade
])

# Define the order between activities
root.order.add_edge(SiteSurvey, DesignLayout)
root.order.add_edge(DesignLayout, ModularBuild)
root.order.add_edge(ModularBuild, InstallPumps)
root.order.add_edge(InstallPumps, SetupSensors)
root.order.add_edge(SetupSensors, CalibrateLights)
root.order.add_edge(CalibrateLights, NutrientMix)
root.order.add_edge(NutrientMix, PlantSeeding)
root.order.add_edge(PlantSeeding, WaterCycling)
root.order.add_edge(WaterCycling, EnergyAudit)
root.order.add_edge(EnergyAudit, PestControl)
root.order.add_edge(PestControl, GrowthMonitor)
root.order.add_edge(GrowthMonitor, DataAnalysis)
root.order.add_edge(DataAnalysis, YieldForecast)
root.order.add_edge(YieldForecast, SupplyOrder)
root.order.add_edge(SupplyOrder, WasteRecycle)
root.order.add_edge(WasteRecycle, SystemUpgrade)