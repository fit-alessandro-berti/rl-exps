import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

DemandForecast = Transition(label='Demand Forecast')
RiskAssess = Transition(label='Risk Assess')
SupplierAudit = Transition(label='Supplier Audit')
InventoryScan = Transition(label='Inventory Scan')
RouteOptimize = Transition(label='Route Optimize')
OrderPrioritize = Transition(label='Order Prioritize')
ContractReview = Transition(label='Contract Review')
DelayMonitor = Transition(label='Delay Monitor')
ShipmentReroute = Transition(label='Shipment Reroute')
CostAnalyze = Transition(label='Cost Analyze')
ComplianceCheck = Transition(label='Compliance Check')
AlternativeEngage = Transition(label='Alternative Engage')
InventoryReallocate = Transition(label='Inventory Reallocate')
PerformanceTrack = Transition(label='Performance Track')
FeedbackLoop = Transition(label='Feedback Loop')
StrategyUpdate = Transition(label='Strategy Update')

skip = SilentTransition()

# Process nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[DemandForecast, RiskAssess, SupplierAudit, InventoryScan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[RouteOptimize, OrderPrioritize, ContractReview, DelayMonitor])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[ShipmentReroute, CostAnalyze, ComplianceCheck, AlternativeEngage])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[InventoryReallocate, PerformanceTrack, FeedbackLoop, StrategyUpdate])

# Exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])

# Root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)