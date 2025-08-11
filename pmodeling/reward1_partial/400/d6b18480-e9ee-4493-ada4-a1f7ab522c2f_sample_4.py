import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the relationships between the activities
xor1 = OperatorPOWL(operator=Operator.XOR, children=[authenticity_check, blockchain_update])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, price_adjustment])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[compliance_review, logistics_planning])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[distributor_sync, customer_feedback])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[product_refinement, reputation_audit])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[seasonal_review, material_sourcing])

# Define the loop for the main process
loop = OperatorPOWL(operator=Operator.LOOP, children=[forager_dispatch, xor1, batch_scheduling, xor2, artisan_allocation, xor3, craft_assembly, xor4, quality_inspection, xor5])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor6])
root.order.add_edge(loop, xor6)

print(root)