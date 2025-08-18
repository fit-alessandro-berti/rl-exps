import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
farm_visit = Transition(label='Farm Visit')
quality_cupping = Transition(label='Quality Cupping')
sustainability_audit = Transition(label='Sustainability Audit')
contract_draft = Transition(label='Contract Draft')
price_negotiate = Transition(label='Price Negotiate')
sample_testing = Transition(label='Sample Testing')
shipment_plan = Transition(label='Shipment Plan')
customs_clearance = Transition(label='Customs Clear')
inventory_update = Transition(label='Inventory Update')
supplier_review = Transition(label='Supplier Review')
risk_assess = Transition(label='Risk Assess')
forecast_adjust = Transition(label='Forecast Adjust')
payment_process = Transition(label='Payment Process')
relationship_call = Transition(label='Relationship Call')
traceability_log = Transition(label='Traceability Log')
market_research = Transition(label='Market Research')
compliance_check = Transition(label='Compliance Check')

# Define the POWL model structure
root = StrictPartialOrder(
    nodes=[
        farm_visit,
        quality_cupping,
        sustainability_audit,
        contract_draft,
        price_negotiate,
        sample_testing,
        shipment_plan,
        customs_clearance,
        inventory_update,
        supplier_review,
        risk_assess,
        forecast_adjust,
        payment_process,
        relationship_call,
        traceability_log,
        market_research,
        compliance_check
    ],
    order=[
        (farm_visit, quality_cupping),
        (quality_cupping, sustainability_audit),
        (sustainability_audit, contract_draft),
        (contract_draft, price_negotiate),
        (price_negotiate, sample_testing),
        (sample_testing, shipment_plan),
        (shipment_plan, customs_clearance),
        (customs_clearance, inventory_update),
        (inventory_update, supplier_review),
        (supplier_review, risk_assess),
        (risk_assess, forecast_adjust),
        (forecast_adjust, payment_process),
        (payment_process, relationship_call),
        (relationship_call, traceability_log),
        (traceability_log, market_research),
        (market_research, compliance_check)
    ]
)

# Print the root of the POWL model
print(root)