import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, authenticity_check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[batch_scheduling, artisan_allocation])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[craft_assembly, quality_inspection])

# Define XOR
xor = OperatorPOWL(operator=Operator.XOR, children=[distributor_sync, skip])

# Define root
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, xor])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)
root.order.add_edge(loop3, xor)

# Print the root POWL model
print(root)