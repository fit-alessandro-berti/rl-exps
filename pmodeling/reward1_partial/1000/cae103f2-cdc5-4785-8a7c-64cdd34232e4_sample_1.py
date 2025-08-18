from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
SiteAcquisition = Transition(label='Site Acquisition')
ImpactAssess = Transition(label='Impact Assess')
ModularSetup = Transition(label='Modular Setup')
CropPlanting = Transition(label='Crop Planting')
NutrientControl = Transition(label='Nutrient Control')
PestControl = Transition(label='Pest Control')
GrowthMonitor = Transition(label='Growth Monitor')
CommunityEngage = Transition(label='Community Engage')
YieldForecast = Transition(label='Yield Forecast')
SupplyCoordinate = Transition(label='Supply Coordinate')
ComplianceCheck = Transition(label='Compliance Check')
WasteRecycle = Transition(label='Waste Recycle')
EnergyOptimize = Transition(label='Energy Optimize')
MarketStrategy = Transition(label='Market Strategy')
PerformanceReview = Transition(label='Performance Review')

# Define the model
root = StrictPartialOrder(nodes=[
    SiteAcquisition, ImpactAssess, ModularSetup, CropPlanting, NutrientControl, PestControl, GrowthMonitor, CommunityEngage, YieldForecast, SupplyCoordinate, ComplianceCheck, WasteRecycle, EnergyOptimize, MarketStrategy, PerformanceReview
])

# Define the dependencies between the activities
root.order.add_edge(SiteAcquisition, ImpactAssess)
root.order.add_edge(ImpactAssess, ModularSetup)
root.order.add_edge(ModularSetup, CropPlanting)
root.order.add_edge(CropPlanting, NutrientControl)
root.order.add_edge(NutrientControl, PestControl)
root.order.add_edge(PestControl, GrowthMonitor)
root.order.add_edge(GrowthMonitor, CommunityEngage)
root.order.add_edge(CommunityEngage, YieldForecast)
root.order.add_edge(YieldForecast, SupplyCoordinate)
root.order.add_edge(SupplyCoordinate, ComplianceCheck)
root.order.add_edge(ComplianceCheck, WasteRecycle)
root.order.add_edge(WasteRecycle, EnergyOptimize)
root.order.add_edge(EnergyOptimize, MarketStrategy)
root.order.add_edge(MarketStrategy, PerformanceReview)

print(root)