import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SiteAnalysis = Transition(label='Site Analysis')
InfrastructureSetup = Transition(label='Infrastructure Setup')
SeedSelection = Transition(label='Seed Selection')
NutrientMix = Transition(label='Nutrient Mix')
PlantingCycle = Transition(label='Planting Cycle')
ClimateAdjust = Transition(label='Climate Adjust')
GrowthMonitor = Transition(label='Growth Monitor')
PestControl = Transition(label='Pest Control')
HarvestingMode = Transition(label='Harvesting Mode')
QualityCheck = Transition(label='Quality Check')
PackagingPhase = Transition(label='Packaging Phase')
ColdStorage = Transition(label='Cold Storage')
OrderDispatch = Transition(label='Order Dispatch')
WasteRecycling = Transition(label='Waste Recycling')
SystemMaintain = Transition(label='System Maintain')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    SiteAnalysis, InfrastructureSetup, SeedSelection, NutrientMix, PlantingCycle, 
    ClimateAdjust, GrowthMonitor, PestControl, HarvestingMode, QualityCheck, 
    PackagingPhase, ColdStorage, OrderDispatch, WasteRecycling, SystemMaintain
])

# Define the order between nodes
root.order.add_edge(SiteAnalysis, InfrastructureSetup)
root.order.add_edge(InfrastructureSetup, SeedSelection)
root.order.add_edge(SeedSelection, NutrientMix)
root.order.add_edge(NutrientMix, PlantingCycle)
root.order.add_edge(PlantingCycle, ClimateAdjust)
root.order.add_edge(ClimateAdjust, GrowthMonitor)
root.order.add_edge(GrowthMonitor, PestControl)
root.order.add_edge(PestControl, HarvestingMode)
root.order.add_edge(HarvestingMode, QualityCheck)
root.order.add_edge(QualityCheck, PackagingPhase)
root.order.add_edge(PackagingPhase, ColdStorage)
root.order.add_edge(ColdStorage, OrderDispatch)
root.order.add_edge(OrderDispatch, WasteRecycling)
root.order.add_edge(WasteRecycling, SystemMaintain)

print(root)