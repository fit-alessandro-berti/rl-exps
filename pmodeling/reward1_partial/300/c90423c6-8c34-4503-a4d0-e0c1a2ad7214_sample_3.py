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

# Define the process flow
process = StrictPartialOrder(
    nodes=[farm_selection, sample_testing, trade_negotiation, micro_lot_sorting, fermentation_control,
           sensory_profiling, roast_calibration, blend_creation, sustainability_audit, packaging_design,
           quality_inspection, inventory_sync, logistics_planning, cafe_training, dynamic_pricing,
           customer_feedback, traceability_logging]
)

# Define the dependencies
process.order.add_edge(farm_selection, sample_testing)
process.order.add_edge(sample_testing, trade_negotiation)
process.order.add_edge(trade_negotiation, micro_lot_sorting)
process.order.add_edge(micro_lot_sorting, fermentation_control)
process.order.add_edge(fermentation_control, sensory_profiling)
process.order.add_edge(sensory_profiling, roast_calibration)
process.order.add_edge(roast_calibration, blend_creation)
process.order.add_edge(blend_creation, sustainability_audit)
process.order.add_edge(sustainability_audit, packaging_design)
process.order.add_edge(packaging_design, quality_inspection)
process.order.add_edge(quality_inspection, inventory_sync)
process.order.add_edge(inventory_sync, logistics_planning)
process.order.add_edge(logistics_planning, cafe_training)
process.order.add_edge(cafe_training, dynamic_pricing)
process.order.add_edge(dynamic_pricing, customer_feedback)
process.order.add_edge(customer_feedback, traceability_logging)

# Assign the final result to the variable 'root'
root = process