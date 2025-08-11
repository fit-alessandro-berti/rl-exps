import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define loops and choices
authenticity_loop = OperatorPOWL(operator=Operator.LOOP, children=[authenticity_check])
batch_scheduling_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_scheduling, artisan_allocation, craft_assembly, quality_inspection, blockchain_update])
demand_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, price_adjustment, compliance_review])
logistics_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_planning, distributor_sync, customer_feedback, product_refinement, reputation_audit, seasonal_review])

# Define root POWL model
root = StrictPartialOrder(nodes=[material_sourcing, forager_dispatch, authenticity_loop, batch_scheduling_loop, demand_forecast_loop, logistics_loop])
root.order.add_edge(material_sourcing, forager_dispatch)
root.order.add_edge(forager_dispatch, authenticity_loop)
root.order.add_edge(authenticity_loop, batch_scheduling_loop)
root.order.add_edge(batch_scheduling_loop, demand_forecast_loop)
root.order.add_edge(demand_forecast_loop, logistics_loop)
root.order.add_edge(logistics_loop, material_sourcing)  # Loop back to start for continuous process