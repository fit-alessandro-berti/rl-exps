import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order structure
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

# Define the dependencies between activities
root.order.add_edge(material_sourcing, forager_dispatch)
root.order.add_edge(material_sourcing, authenticity_check)
root.order.add_edge(material_sourcing, batch_scheduling)
root.order.add_edge(material_sourcing, artisan_allocation)
root.order.add_edge(material_sourcing, craft_assembly)
root.order.add_edge(material_sourcing, quality_inspection)
root.order.add_edge(material_sourcing, blockchain_update)
root.order.add_edge(material_sourcing, demand_forecast)
root.order.add_edge(material_sourcing, price_adjustment)
root.order.add_edge(material_sourcing, compliance_review)
root.order.add_edge(material_sourcing, logistics_planning)
root.order.add_edge(material_sourcing, distributor_sync)
root.order.add_edge(material_sourcing, customer_feedback)
root.order.add_edge(material_sourcing, product_refinement)
root.order.add_edge(material_sourcing, reputation_audit)
root.order.add_edge(material_sourcing, seasonal_review)

print(root)