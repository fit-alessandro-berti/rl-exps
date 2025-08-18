from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their respective labels
SiteSurvey = Transition(label='Site Survey')
EnvAnalysis = Transition(label='Env Analysis')
ModuleDesign = Transition(label='Module Design')
SeedSelection = Transition(label='Seed Selection')
NutrientMix = Transition(label='Nutrient Mix')
ClimateSetup = Transition(label='Climate Setup')
LEDInstall = Transition(label='LED Install')
SensorDeploy = Transition(label='Sensor Deploy')
PestControl = Transition(label='Pest Control')
WasteRecycle = Transition(label='Waste Recycle')
HydroTest = Transition(label='Hydro Test')
StaffTrain = Transition(label='Staff Train')
YieldForecast = Transition(label='Yield Forecast')
MarketPlan = Transition(label='Market Plan')
DataReview = Transition(label='Data Review')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    SiteSurvey,
    EnvAnalysis,
    ModuleDesign,
    SeedSelection,
    NutrientMix,
    ClimateSetup,
    LEDInstall,
    SensorDeploy,
    PestControl,
    WasteRecycle,
    HydroTest,
    StaffTrain,
    YieldForecast,
    MarketPlan,
    DataReview
])

# Add dependencies between the transitions
root.order.add_edge(SiteSurvey, EnvAnalysis)
root.order.add_edge(EnvAnalysis, ModuleDesign)
root.order.add_edge(ModuleDesign, SeedSelection)
root.order.add_edge(SeedSelection, NutrientMix)
root.order.add_edge(NutrientMix, ClimateSetup)
root.order.add_edge(ClimateSetup, LEDInstall)
root.order.add_edge(LEDInstall, SensorDeploy)
root.order.add_edge(SensorDeploy, PestControl)
root.order.add_edge(PestControl, WasteRecycle)
root.order.add_edge(WasteRecycle, HydroTest)
root.order.add_edge(HydroTest, StaffTrain)
root.order.add_edge(StaffTrain, YieldForecast)
root.order.add_edge(YieldForecast, MarketPlan)
root.order.add_edge(MarketPlan, DataReview)