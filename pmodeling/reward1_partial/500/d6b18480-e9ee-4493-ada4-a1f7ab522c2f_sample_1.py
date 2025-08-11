from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
material_sourcing = Transition(label='Material Sourcing')
forager_dispatch = Transition(label='Forager Dispatch')
authenticity_check = Transition(label='Authenticity Check')
batch_scheduling = Transition(label='Batch Scheduling')
artisan_allocation = Transition(label='Artisan Allocation')
craft_assembly = Transition(label='Craft Assembly')
quality_inspection = Transition(label='Quality Inspection')
blockchain_update = Transition(label='Blockchain Update')
demand_forecast = Transition(label='Demand Forecast')
price_adjustment = Transition(label='Price Adjustment')
compliance_review = Transition(label='Compliance Review')
logistics_planning = Transition(label='Logistics Planning')
distributor_sync = Transition(label='Distributor Sync')
customer_feedback = Transition(label='Customer Feedback')
product_refinement = Transition(label='Product Refinement')
reputation_audit = Transition(label='Reputation Audit')
seasonal_review = Transition(label='Seasonal Review')

# Define a partial order model
root = StrictPartialOrder(
    nodes=[
        material_sourcing,
        forager_dispatch,
        authenticity_check,
        batch_scheduling,
        artisan_allocation,
        craft_assembly,
        quality_inspection,
        blockchain_update,
        demand_forecast,
        price_adjustment,
        compliance_review,
        logistics_planning,
        distributor_sync,
        customer_feedback,
        product_refinement,
        reputation_audit,
        seasonal_review
    ],
    order=[
        (material_sourcing, forager_dispatch),
        (forager_dispatch, authenticity_check),
        (authenticity_check, batch_scheduling),
        (batch_scheduling, artisan_allocation),
        (artisan_allocation, craft_assembly),
        (craft_assembly, quality_inspection),
        (quality_inspection, blockchain_update),
        (blockchain_update, demand_forecast),
        (demand_forecast, price_adjustment),
        (price_adjustment, compliance_review),
        (compliance_review, logistics_planning),
        (logistics_planning, distributor_sync),
        (distributor_sync, customer_feedback),
        (customer_feedback, product_refinement),
        (product_refinement, reputation_audit),
        (reputation_audit, seasonal_review)
    ]
)