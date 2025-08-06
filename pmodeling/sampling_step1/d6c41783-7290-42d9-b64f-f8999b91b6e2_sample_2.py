from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
QuantumModeling = Transition(label='Quantum Modeling')
DataEncoding = Transition(label='Data Encoding')
RouteSimulation = Transition(label='Route Simulation')
DemandForecast = Transition(label='Demand Forecast')
SupplierSync = Transition(label='Supplier Sync')
EntangleNodes = Transition(label='Entangle Nodes')
RiskAnalysis = Transition(label='Risk Analysis')
InventoryScan = Transition(label='Inventory Scan')
LatencyCheck = Transition(label='Latency Check')
TransportPlan = Transition(label='Transport Plan')
QuantumCompute = Transition(label='Quantum Compute')
ScenarioTest = Transition(label='Scenario Test')
ResourceAlign = Transition(label='Resource Align')
ProtocolUpdate = Transition(label='Protocol Update')
FeedbackLoop = Transition(label='Feedback Loop')
CostOptimize = Transition(label='Cost Optimize')
ImpactReview = Transition(label='Impact Review')

# Define the partial order
root = StrictPartialOrder(nodes=[
    QuantumModeling, DataEncoding, RouteSimulation, DemandForecast, SupplierSync,
    EntangleNodes, RiskAnalysis, InventoryScan, LatencyCheck, TransportPlan,
    QuantumCompute, ScenarioTest, ResourceAlign, ProtocolUpdate, FeedbackLoop,
    CostOptimize, ImpactReview
])

# Define the order
root.order.add_edge(QuantumModeling, DataEncoding)
root.order.add_edge(DataEncoding, RouteSimulation)
root.order.add_edge(RouteSimulation, DemandForecast)
root.order.add_edge(DemandForecast, SupplierSync)
root.order.add_edge(SupplierSync, EntangleNodes)
root.order.add_edge(EntangleNodes, RiskAnalysis)
root.order.add_edge(RiskAnalysis, InventoryScan)
root.order.add_edge(InventoryScan, LatencyCheck)
root.order.add_edge(LatencyCheck, TransportPlan)
root.order.add_edge(TransportPlan, QuantumCompute)
root.order.add_edge(QuantumCompute, ScenarioTest)
root.order.add_edge(ScenarioTest, ResourceAlign)
root.order.add_edge(ResourceAlign, ProtocolUpdate)
root.order.add_edge(ProtocolUpdate, FeedbackLoop)
root.order.add_edge(FeedbackLoop, CostOptimize)
root.order.add_edge(CostOptimize, ImpactReview)

print(root)