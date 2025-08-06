import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
FarmVisit = Transition(label='Farm Visit')
QualityCupping = Transition(label='Quality Cupping')
SustainabilityAudit = Transition(label='Sustainability Audit')
ContractDraft = Transition(label='Contract Draft')
PriceNegotiate = Transition(label='Price Negotiate')
SampleTesting = Transition(label='Sample Testing')
ShipmentPlan = Transition(label='Shipment Plan')
CustomsClear = Transition(label='Customs Clear')
InventoryUpdate = Transition(label='Inventory Update')
SupplierReview = Transition(label='Supplier Review')
RiskAssess = Transition(label='Risk Assess')
ForecastAdjust = Transition(label='Forecast Adjust')
PaymentProcess = Transition(label='Payment Process')
RelationshipCall = Transition(label='Relationship Call')
TraceabilityLog = Transition(label='Traceability Log')
MarketResearch = Transition(label='Market Research')
ComplianceCheck = Transition(label='Compliance Check')

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[FarmVisit, QualityCupping, SustainabilityAudit, ContractDraft, PriceNegotiate, SampleTesting])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ShipmentPlan, CustomsClear, InventoryUpdate, SupplierReview, RiskAssess, ForecastAdjust])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[PaymentProcess, RelationshipCall, TraceabilityLog, MarketResearch, ComplianceCheck])

# Define the choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor1)

# Save the final result in the variable 'root'