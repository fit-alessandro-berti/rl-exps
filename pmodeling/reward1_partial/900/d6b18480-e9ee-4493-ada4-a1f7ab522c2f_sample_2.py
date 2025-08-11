import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
sourcing = Transition(label='Material Sourcing')
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

# Define operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[blockchain_update, demand_forecast])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[price_adjustment, compliance_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning, distributor_sync])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, product_refinement])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[reputation_audit, seasonal_review])

# Define the root model
root = StrictPartialOrder(nodes=[sourcing, forager_dispatch, authenticity_check, batch_scheduling, artisan_allocation, craft_assembly, quality_inspection, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(sourcing, forager_dispatch)
root.order.add_edge(forager_dispatch, authenticity_check)
root.order.add_edge(authenticity_check, batch_scheduling)
root.order.add_edge(batch_scheduling, artisan_allocation)
root.order.add_edge(artisan_allocation, craft_assembly)
root.order.add_edge(craft_assembly, quality_inspection)
root.order.add_edge(quality_inspection, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)