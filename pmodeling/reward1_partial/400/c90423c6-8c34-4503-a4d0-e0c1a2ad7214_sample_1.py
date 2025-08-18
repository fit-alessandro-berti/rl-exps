import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control-flow operators
xor_trade_negotiation = OperatorPOWL(operator=Operator.XOR, children=[trade_negotiation, farm_selection])
xor_sensory_profiling = OperatorPOWL(operator=Operator.XOR, children=[sensory_profiling, micro_lot_sorting])
xor_fermentation_control = OperatorPOWL(operator=Operator.XOR, children=[fermentation_control, roast_calibration])
xor_blend_creation = OperatorPOWL(operator=Operator.XOR, children=[blend_creation, sustainability_audit])
xor_inventory_sync = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, logistics_planning])
xor_cafe_training = OperatorPOWL(operator=Operator.XOR, children=[cafe_training, dynamic_pricing])
xor_dynamic_pricing = OperatorPOWL(operator=Operator.XOR, children=[dynamic_pricing, customer_feedback])
xor_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, traceability_logging])

# Define the partial order
root = StrictPartialOrder(nodes=[farm_selection, sample_testing, xor_trade_negotiation, xor_sensory_profiling, xor_fermentation_control, xor_blend_creation, packaging_design, quality_inspection, xor_inventory_sync, xor_cafe_training, xor_dynamic_pricing, xor_customer_feedback, traceability_logging])
root.order.add_edge(farm_selection, sample_testing)
root.order.add_edge(sample_testing, xor_trade_negotiation)
root.order.add_edge(sample_testing, xor_sensory_profiling)
root.order.add_edge(xor_trade_negotiation, xor_fermentation_control)
root.order.add_edge(xor_sensory_profiling, xor_blend_creation)
root.order.add_edge(xor_fermentation_control, packaging_design)
root.order.add_edge(xor_blend_creation, quality_inspection)
root.order.add_edge(quality_inspection, xor_inventory_sync)
root.order.add_edge(xor_inventory_sync, xor_cafe_training)
root.order.add_edge(xor_cafe_training, xor_dynamic_pricing)
root.order.add_edge(xor_dynamic_pricing, xor_customer_feedback)
root.order.add_edge(xor_customer_feedback, traceability_logging)

# Print the POWL model
print(root)