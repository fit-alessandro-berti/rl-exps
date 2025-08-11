from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
# Material Sourcing
material_sourcing = Transition(label='Material Sourcing')

# Forager Dispatch
forager_dispatch = Transition(label='Forager Dispatch')

# Authenticity Check
authenticity_check = Transition(label='Authenticity Check')

# Batch Scheduling
batch_scheduling = Transition(label='Batch Scheduling')

# Artisan Allocation
artisan_allocation = Transition(label='Artisan Allocation')

# Craft Assembly
craft_assembly = Transition(label='Craft Assembly')

# Quality Inspection
quality_inspection = Transition(label='Quality Inspection')

# Blockchain Update
blockchain_update = Transition(label='Blockchain Update')

# Demand Forecast
demand_forecast = Transition(label='Demand Forecast')

# Price Adjustment
price_adjustment = Transition(label='Price Adjustment')

# Compliance Review
compliance_review = Transition(label='Compliance Review')

# Logistics Planning
logistics_planning = Transition(label='Logistics Planning')

# Distributor Sync
distributor_sync = Transition(label='Distributor Sync')

# Customer Feedback
customer_feedback = Transition(label='Customer Feedback')

# Product Refinement
product_refinement = Transition(label='Product Refinement')

# Reputation Audit
reputation_audit = Transition(label='Reputation Audit')

# Seasonal Review
seasonal_review = Transition(label='Seasonal Review')

# Define the partial order
root = StrictPartialOrder(nodes=[
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
])

# Define the dependencies between nodes
root.order.add_edge(material_sourcing, forager_dispatch)
root.order.add_edge(forager_dispatch, authenticity_check)
root.order.add_edge(authenticity_check, batch_scheduling)
root.order.add_edge(batch_scheduling, artisan_allocation)
root.order.add_edge(artisan_allocation, craft_assembly)
root.order.add_edge(craft_assembly, quality_inspection)
root.order.add_edge(quality_inspection, blockchain_update)
root.order.add_edge(blockchain_update, demand_forecast)
root.order.add_edge(demand_forecast, price_adjustment)
root.order.add_edge(price_adjustment, compliance_review)
root.order.add_edge(compliance_review, logistics_planning)
root.order.add_edge(logistics_planning, distributor_sync)
root.order.add_edge(distributor_sync, customer_feedback)
root.order.add_edge(customer_feedback, product_refinement)
root.order.add_edge(product_refinement, reputation_audit)
root.order.add_edge(reputation_audit, seasonal_review)

# Print the root of the POWL model
print(root)