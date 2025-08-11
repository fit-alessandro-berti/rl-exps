import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
MaterialSourcing = Transition(label='Material Sourcing')
ArtisanVetting = Transition(label='Artisan Vetting')
SampleReview = Transition(label='Sample Review')
DesignFinalize = Transition(label='Design Finalize')
BatchScheduling = Transition(label='Batch Scheduling')
QualityCheck = Transition(label='Quality Check')
CustomPackaging = Transition(label='Custom Packaging')
DemandForecast = Transition(label='Demand Forecast')
PriceAdjust = Transition(label='Price Adjust')
InventorySync = Transition(label='Inventory Sync')
OrderProcessing = Transition(label='Order Processing')
CraftCoordination = Transition(label='Craft Coordination')
ShipmentPlan = Transition(label='Shipment Plan')
MarketAnalysis = Transition(label='Market Analysis')
FeedbackLoop = Transition(label='Feedback Loop')
TrendMonitor = Transition(label='Trend Monitor')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for quality check and custom packaging
qualityChoice = OperatorPOWL(operator=Operator.XOR, children=[QualityCheck, CustomPackaging])

# Define exclusive choice for price adjust and inventory sync
priceChoice = OperatorPOWL(operator=Operator.XOR, children=[PriceAdjust, InventorySync])

# Define loop for batch scheduling and order processing
batchLoop = OperatorPOWL(operator=Operator.LOOP, children=[BatchScheduling, OrderProcessing])

# Define loop for craft coordination and shipment plan
craftLoop = OperatorPOWL(operator=Operator.LOOP, children=[CraftCoordination, ShipmentPlan])

# Define loop for market analysis and feedback loop
marketLoop = OperatorPOWL(operator=Operator.LOOP, children=[MarketAnalysis, FeedbackLoop])

# Define the root POWL model
root = StrictPartialOrder(nodes=[MaterialSourcing, ArtisanVetting, SampleReview, DesignFinalize, BatchScheduling, QualityCheck, CustomPackaging, DemandForecast, PriceAdjust, InventorySync, OrderProcessing, CraftCoordination, ShipmentPlan, MarketAnalysis, FeedbackLoop, TrendMonitor])
root.order.add_edge(MaterialSourcing, ArtisanVetting)
root.order.add_edge(ArtisanVetting, SampleReview)
root.order.add_edge(SampleReview, DesignFinalize)
root.order.add_edge(DesignFinalize, BatchScheduling)
root.order.add_edge(BatchScheduling, qualityChoice)
root.order.add_edge(qualityChoice, batchLoop)
root.order.add_edge(batchLoop, priceChoice)
root.order.add_edge(priceChoice, craftLoop)
root.order.add_edge(craftLoop, marketLoop)
root.order.add_edge(marketLoop, TrendMonitor)