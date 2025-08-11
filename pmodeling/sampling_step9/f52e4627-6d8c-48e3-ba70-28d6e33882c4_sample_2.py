import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
skip = SilentTransition()

# Define the flow of activities
farm_visit = OperatorPOWL(operator=Operator.PARALLEL, children=[FarmVisit, QualityCupping, SustainabilityAudit])
contract_draft = OperatorPOWL(operator=Operator.PARALLEL, children=[ContractDraft, PriceNegotiate, SampleTesting])
shipment_plan = OperatorPOWL(operator=Operator.PARALLEL, children=[ShipmentPlan, CustomsClear, InventoryUpdate])
supplier_review = OperatorPOWL(operator=Operator.PARALLEL, children=[SupplierReview, RiskAssess, ForecastAdjust])
payment_process = OperatorPOWL(operator=Operator.PARALLEL, children=[PaymentProcess, RelationshipCall, TraceabilityLog])
market_research = OperatorPOWL(operator=Operator.PARALLEL, children=[MarketResearch, ComplianceCheck])

# Define the partial order
root = StrictPartialOrder(nodes=[farm_visit, contract_draft, shipment_plan, supplier_review, payment_process, market_research])
root.order.add_edge(farm_visit, contract_draft)
root.order.add_edge(farm_visit, shipment_plan)
root.order.add_edge(farm_visit, supplier_review)
root.order.add_edge(farm_visit, payment_process)
root.order.add_edge(farm_visit, market_research)

root.order.add_edge(contract_draft, shipment_plan)
root.order.add_edge(contract_draft, supplier_review)
root.order.add_edge(contract_draft, payment_process)
root.order.add_edge(contract_draft, market_research)

root.order.add_edge(shipment_plan, supplier_review)
root.order.add_edge(shipment_plan, payment_process)
root.order.add_edge(shipment_plan, market_research)

root.order.add_edge(supplier_review, payment_process)
root.order.add_edge(supplier_review, market_research)

root.order.add_edge(payment_process, market_research)