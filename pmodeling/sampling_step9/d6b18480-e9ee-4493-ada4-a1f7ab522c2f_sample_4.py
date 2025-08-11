import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the loops
batch_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, forager_dispatch, authenticity_check, batch_scheduling, artisan_allocation, craft_assembly, quality_inspection, blockchain_update])
logistics_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_review, logistics_planning, distributor_sync, customer_feedback])
seasonal_loop = OperatorPOWL(operator=Operator.LOOP, children=[seasonal_review])

# Define the exclusive choices
demand_choice = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, price_adjustment])
product_choice = OperatorPOWL(operator=Operator.XOR, children=[product_refinement, reputation_audit])

# Define the partial order
root = StrictPartialOrder(nodes=[batch_loop, logistics_loop, seasonal_loop, demand_choice, product_choice])
root.order.add_edge(batch_loop, logistics_loop)
root.order.add_edge(logistics_loop, seasonal_loop)
root.order.add_edge(seasonal_loop, demand_choice)
root.order.add_edge(demand_choice, product_choice)

print(root)