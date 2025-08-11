import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    material_sourcing, forager_dispatch, authenticity_check, batch_scheduling, artisan_allocation, craft_assembly, quality_inspection, blockchain_update, demand_forecast, price_adjustment, compliance_review, logistics_planning, distributor_sync, customer_feedback, product_refinement, reputation_audit, seasonal_review
])

# Define the dependencies
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

print(root)