from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process structure
farm_selection_to_sample_testing = OperatorPOWL(operator=Operator.XOR, children=[trade_negotiation, sample_testing])
sample_testing_to_micro_lot_sorting = OperatorPOWL(operator=Operator.XOR, children=[micro_lot_sorting, fermentation_control])
micro_lot_sorting_to_sensory_profiling = OperatorPOWL(operator=Operator.XOR, children=[sensory_profiling, roast_calibration])
sensory_profiling_to_blend_creation = OperatorPOWL(operator=Operator.XOR, children=[blend_creation, sustainability_audit])
blend_creation_to_packaging_design = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, quality_inspection])
packaging_design_to_inventory_sync = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, logistics_planning])
inventory_sync_to_cafe_training = OperatorPOWL(operator=Operator.XOR, children=[cafe_training, dynamic_pricing])
cafe_training_to_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, traceability_logging])
dynamic_pricing_to_traceability_logging = OperatorPOWL(operator=Operator.XOR, children=[traceability_logging])

# Create the root node
root = StrictPartialOrder(nodes=[farm_selection, sample_testing, trade_negotiation, micro_lot_sorting, fermentation_control, sensory_profiling, roast_calibration, blend_creation, packaging_design, quality_inspection, inventory_sync, logistics_planning, cafe_training, customer_feedback, traceability_logging])
root.order.add_edge(farm_selection, sample_testing_to_micro_lot_sorting)
root.order.add_edge(sample_testing, micro_lot_sorting_to_sensory_profiling)
root.order.add_edge(micro_lot_sorting, sensory_profiling_to_blend_creation)
root.order.add_edge(sensory_profiling, blend_creation_to_packaging_design)
root.order.add_edge(blend_creation, packaging_design_to_inventory_sync)
root.order.add_edge(packaging_design, inventory_sync_to_cafe_training)
root.order.add_edge(inventory_sync, cafe_training_to_customer_feedback)
root.order.add_edge(cafe_training, dynamic_pricing_to_traceability_logging)

# Print the root node
print(root)