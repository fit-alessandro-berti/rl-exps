import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
farm_selection = Transition(label='Farm Selection')
sample_testing = Transition(label='Sample Testing')
trade_negotiation = Transition(label='Trade Negotiation')
micro_lot_sorting = Transition(label='Micro-Lot Sorting')
fermentation_control = Transition(label='Fermentation Control')
sensory_profiling = Transition(label='Sensory Profiling')
roast_calibration = Transition(label='Roast Calibration')
blend_creation = Transition(label='Blend Creation')
sustainability_audit = Transition(label='Sustainability Audit')
packaging_design = Transition(label='Packaging Design')
quality_inspection = Transition(label='Quality Inspection')
inventory_sync = Transition(label='Inventory Sync')
logistics_planning = Transition(label='Logistics Planning')
cafe_training = Transition(label='Cafe Training')
dynamic_pricing = Transition(label='Dynamic Pricing')
customer_feedback = Transition(label='Customer Feedback')
traceability_logging = Transition(label='Traceability Logging')

# Define silent activities
skip = SilentTransition()

# Define loops and choices
micro_lot_loop = OperatorPOWL(operator=Operator.LOOP, children=[micro_lot_sorting, fermentation_control, sensory_profiling, roast_calibration, blend_creation])
sustainability_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_audit])
inventory_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_sync])
logistics_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_planning])

# Define XOR for dynamic pricing
dynamic_pricing_xor = OperatorPOWL(operator=Operator.XOR, children=[dynamic_pricing, skip])

# Define XOR for customer feedback
customer_feedback_xor = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip])

# Define XOR for traceability logging
traceability_logging_xor = OperatorPOWL(operator=Operator.XOR, children=[traceability_logging, skip])

# Define root POWL model
root = StrictPartialOrder(nodes=[farm_selection, sample_testing, trade_negotiation, micro_lot_loop, sustainability_audit_loop, inventory_sync_loop, logistics_plan_loop, cafe_training, dynamic_pricing_xor, customer_feedback_xor, traceability_logging_xor])
root.order.add_edge(farm_selection, sample_testing)
root.order.add_edge(sample_testing, trade_negotiation)
root.order.add_edge(trade_negotiation, micro_lot_loop)
root.order.add_edge(micro_lot_loop, sustainability_audit_loop)
root.order.add_edge(sustainability_audit_loop, inventory_sync_loop)
root.order.add_edge(inventory_sync_loop, logistics_plan_loop)
root.order.add_edge(logistics_plan_loop, cafe_training)
root.order.add_edge(cafe_training, dynamic_pricing_xor)
root.order.add_edge(dynamic_pricing_xor, customer_feedback_xor)
root.order.add_edge(customer_feedback_xor, traceability_logging_xor)

# Print the root POWL model
print(root)