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

# Define silent transitions
Skip = SilentTransition()

# Define loops and choices
SiteSetupLoop = OperatorPOWL(operator=Operator.LOOP, children=[SiteAnalysis, InfrastructureSetup])
SeedNutrientLoop = OperatorPOWL(operator=Operator.LOOP, children=[SeedSelection, NutrientMix])
PlantingPestLoop = OperatorPOWL(operator=Operator.LOOP, children=[PlantingCycle, ClimateAdjust, PestControl])
QualityHarvestLoop = OperatorPOWL(operator=Operator.LOOP, children=[QualityCheck, HarvestingMode])
PackagingColdLoop = OperatorPOWL(operator=Operator.LOOP, children=[PackagingPhase, ColdStorage])
OrderWasteLoop = OperatorPOWL(operator=Operator.LOOP, children=[OrderDispatch, WasteRecycling])
MaintainLoop = OperatorPOWL(operator=Operator.LOOP, children=[SystemMaintain])

# Define XOR for non-loop activities
SiteSetupXOR = OperatorPOWL(operator=Operator.XOR, children=[SiteSetupLoop, Skip])
SeedNutrientXOR = OperatorPOWL(operator=Operator.XOR, children=[SeedNutrientLoop, Skip])
PlantingPestXOR = OperatorPOWL(operator=Operator.XOR, children=[PlantingPestLoop, Skip])
QualityHarvestXOR = OperatorPOWL(operator=Operator.XOR, children=[QualityHarvestLoop, Skip])
PackagingColdXOR = OperatorPOWL(operator=Operator.XOR, children=[PackagingColdLoop, Skip])
OrderWasteXOR = OperatorPOWL(operator=Operator.XOR, children=[OrderWasteLoop, Skip])
MaintainXOR = OperatorPOWL(operator=Operator.XOR, children=[MaintainLoop, Skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[SiteSetupXOR, SeedNutrientXOR, PlantingPestXOR, QualityHarvestXOR, PackagingColdXOR, OrderWasteXOR, MaintainXOR])
root.order.add_edge(SiteSetupXOR, SeedNutrientXOR)
root.order.add_edge(SeedNutrientXOR, PlantingPestXOR)
root.order.add_edge(PlantingPestXOR, QualityHarvestXOR)
root.order.add_edge(QualityHarvestXOR, PackagingColdXOR)
root.order.add_edge(PackagingColdXOR, OrderWasteXOR)
root.order.add_edge(OrderWasteXOR, MaintainXOR)