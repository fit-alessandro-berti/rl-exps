import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
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

# Define the relationships between activities using the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, forager_dispatch])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[authenticity_check, blockchain_update])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[batch_scheduling, artisan_allocation])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[craft_assembly, quality_inspection])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, price_adjustment])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[compliance_review, logistics_planning])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[distributor_sync, customer_feedback])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[product_refinement, reputation_audit])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[seasonal_review, None])  # None represents the end of the process

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)