import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
SiteSurvey = Transition(label='Site Survey')
StructureReinforce = Transition(label='Structure Reinforce')
HydroponicSetup = Transition(label='Hydroponic Setup')
ClimateInstall = Transition(label='Climate Install')
AIIntegration = Transition(label='AI Integration')
SeedSourcing = Transition(label='Seed Sourcing')
NutrientPrep = Transition(label='Nutrient Prep')
SystemTesting = Transition(label='System Testing')
StaffTraining = Transition(label='Staff Training')
CropPlanting = Transition(label='Crop Planting')
GrowthMonitor = Transition(label='Growth Monitor')
PestControl = Transition(label='Pest Control')
HarvestSchedule = Transition(label='Harvest Schedule')
QualityCheck = Transition(label='Quality Check')
MarketDispatch = Transition(label='Market Dispatch')
WasteRecycle = Transition(label='Waste Recycle')
DataAnalysis = Transition(label='Data Analysis')

# Define the partial order
root = StrictPartialOrder(nodes=[
    SiteSurvey,
    StructureReinforce,
    HydroponicSetup,
    ClimateInstall,
    AIIntegration,
    SeedSourcing,
    NutrientPrep,
    SystemTesting,
    StaffTraining,
    CropPlanting,
    GrowthMonitor,
    PestControl,
    HarvestSchedule,
    QualityCheck,
    MarketDispatch,
    WasteRecycle,
    DataAnalysis
])

# Define the dependencies between the transitions
root.order.add_edge(SiteSurvey, StructureReinforce)
root.order.add_edge(StructureReinforce, HydroponicSetup)
root.order.add_edge(HydroponicSetup, ClimateInstall)
root.order.add_edge(ClimateInstall, AIIntegration)
root.order.add_edge(AIIntegration, SeedSourcing)
root.order.add_edge(SeedSourcing, NutrientPrep)
root.order.add_edge(NutrientPrep, SystemTesting)
root.order.add_edge(SystemTesting, StaffTraining)
root.order.add_edge(StaffTraining, CropPlanting)
root.order.add_edge(CropPlanting, GrowthMonitor)
root.order.add_edge(GrowthMonitor, PestControl)
root.order.add_edge(PestControl, HarvestSchedule)
root.order.add_edge(HarvestSchedule, QualityCheck)
root.order.add_edge(QualityCheck, MarketDispatch)
root.order.add_edge(MarketDispatch, WasteRecycle)
root.order.add_edge(WasteRecycle, DataAnalysis)

# Print the root model
print(root)