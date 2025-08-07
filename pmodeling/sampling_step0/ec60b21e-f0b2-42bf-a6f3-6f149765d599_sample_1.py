import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.process_tree.utils import operators

# Define the activities
SiteSurvey = Transition(label='Site Survey')
ModularDesign = Transition(label='Modular Design')
SystemBuild = Transition(label='System Build')
EnvControl = Transition(label='Env Control')
SeedSelection = Transition(label='Seed Selection')
NutrientMix = Transition(label='Nutrient Mix')
PlantingSetup = Transition(label='Planting Setup')
GrowthMonitor = Transition(label='Growth Monitor')
PestControl = Transition(label='Pest Control')
WaterCycle = Transition(label='Water Cycle')
DataCapture = Transition(label='Data Capture')
YieldForecast = Transition(label='Yield Forecast')
WasteReuse = Transition(label='Waste Reuse')
StakeholderMeet = Transition(label='Stakeholder Meet')
ComplianceCheck = Transition(label='Compliance Check')
SupplySync = Transition(label='Supply Sync')

# Define the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey,
    ModularDesign,
    SystemBuild,
    EnvControl,
    SeedSelection,
    NutrientMix,
    PlantingSetup,
    GrowthMonitor,
    PestControl,
    WaterCycle,
    DataCapture,
    YieldForecast,
    WasteReuse,
    StakeholderMeet,
    ComplianceCheck,
    SupplySync
])

# Define the partial order's edges
root.order.add_edge(SiteSurvey, ModularDesign)
root.order.add_edge(ModularDesign, SystemBuild)
root.order.add_edge(SystemBuild, EnvControl)
root.order.add_edge(EnvControl, SeedSelection)
root.order.add_edge(SeedSelection, NutrientMix)
root.order.add_edge(NutrientMix, PlantingSetup)
root.order.add_edge(PlantingSetup, GrowthMonitor)
root.order.add_edge(GrowthMonitor, PestControl)
root.order.add_edge(PestControl, WaterCycle)
root.order.add_edge(WaterCycle, DataCapture)
root.order.add_edge(DataCapture, YieldForecast)
root.order.add_edge(YieldForecast, WasteReuse)
root.order.add_edge(WasteReuse, StakeholderMeet)
root.order.add_edge(StakeholderMeet, ComplianceCheck)
root.order.add_edge(ComplianceCheck, SupplySync)