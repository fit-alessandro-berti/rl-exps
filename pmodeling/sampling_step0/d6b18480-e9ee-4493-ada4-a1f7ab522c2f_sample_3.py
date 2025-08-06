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

# Define the operators
xor = OperatorPOWL(operator=Operator.XOR, children=[batch_scheduling, artisan_allocation])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quality_inspection, blockchain_update])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning, distributor_sync])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, reputation_audit])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[price_adjustment, demand_forecast])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[compliance_review, seasonal_review])
loop = OperatorPOWL(operator=Operator.LOOP, children=[craft_assembly])

# Define the root POWL model
root = StrictPartialOrder(nodes=[material_sourcing, forager_dispatch, authenticity_check, xor, xor2, xor3, xor4, xor5, xor6, loop])
root.order.add_edge(material_sourcing, forager_dispatch)
root.order.add_edge(material_sourcing, authenticity_check)
root.order.add_edge(forager_dispatch, xor)
root.order.add_edge(authenticity_check, xor2)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)