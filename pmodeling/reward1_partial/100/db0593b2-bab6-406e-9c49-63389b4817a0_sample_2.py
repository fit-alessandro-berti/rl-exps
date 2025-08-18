import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
SiteAssess = Transition(label='Site Assess')
EnvAnalysis = Transition(label='Env Analysis')
ModularInstall = Transition(label='Modular Install')
IrrigationSetup = Transition(label='Irrigation Setup')
CropSelection = Transition(label='Crop Selection')
NutrientMix = Transition(label='Nutrient Mix')
LightingCalibrate = Transition(label='Lighting Calibrate')
PestMonitor = Transition(label='Pest Monitor')
StaffTraining = Transition(label='Staff Training')
EnergyIntegrate = Transition(label='Energy Integrate')
DataAnalytics = Transition(label='Data Analytics')
WasteRecycle = Transition(label='Waste Recycle')
MarketDevelop = Transition(label='Market Develop')
YieldOptimize = Transition(label='Yield Optimize')
ClimateSimulate = Transition(label='Climate Simulate')

# Define silent transitions
Skip1 = SilentTransition()
Skip2 = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        SiteAssess, EnvAnalysis, ModularInstall, IrrigationSetup, CropSelection, NutrientMix, LightingCalibrate,
        PestMonitor, StaffTraining, EnergyIntegrate, DataAnalytics, WasteRecycle, MarketDevelop, YieldOptimize,
        ClimateSimulate, Skip1, Skip2
    ],
    order={
        SiteAssess: EnvAnalysis,
        EnvAnalysis: ModularInstall,
        ModularInstall: IrrigationSetup,
        IrrigationSetup: CropSelection,
        CropSelection: NutrientMix,
        NutrientMix: LightingCalibrate,
        LightingCalibrate: PestMonitor,
        PestMonitor: StaffTraining,
        StaffTraining: EnergyIntegrate,
        EnergyIntegrate: DataAnalytics,
        DataAnalytics: WasteRecycle,
        WasteRecycle: MarketDevelop,
        MarketDevelop: YieldOptimize,
        YieldOptimize: ClimateSimulate
    }
)

# Add edges to the POWL model
root.order.add_edge(SiteAssess, EnvAnalysis)
root.order.add_edge(EnvAnalysis, ModularInstall)
root.order.add_edge(ModularInstall, IrrigationSetup)
root.order.add_edge(IrrigationSetup, CropSelection)
root.order.add_edge(CropSelection, NutrientMix)
root.order.add_edge(NutrientMix, LightingCalibrate)
root.order.add_edge(LightingCalibrate, PestMonitor)
root.order.add_edge(PestMonitor, StaffTraining)
root.order.add_edge(StaffTraining, EnergyIntegrate)
root.order.add_edge(EnergyIntegrate, DataAnalytics)
root.order.add_edge(DataAnalytics, WasteRecycle)
root.order.add_edge(WasteRecycle, MarketDevelop)
root.order.add_edge(MarketDevelop, YieldOptimize)
root.order.add_edge(YieldOptimize, ClimateSimulate)

# Note: The 'ClimateSimulate' transition has no outgoing edge, so it's not directly connected to other nodes.