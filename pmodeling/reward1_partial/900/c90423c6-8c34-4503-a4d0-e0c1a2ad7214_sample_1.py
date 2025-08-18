import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

farm_selection_to_sample_testing = OperatorPOWL(operator=Operator.XOR, children=[farm_selection, sample_testing])
sample_testing_to_trade_negotiation = OperatorPOWL(operator=Operator.XOR, children=[sample_testing, trade_negotiation])
trade_negotiation_to_micro_lot_sorting = OperatorPOWL(operator=Operator.XOR, children=[trade_negotiation, micro_lot_sorting])
micro_lot_sorting_to_fermentation_control = OperatorPOWL(operator=Operator.XOR, children=[micro_lot_sorting, fermentation_control])
fermentation_control_to_sensory_profiling = OperatorPOWL(operator=Operator.XOR, children=[fermentation_control, sensory_profiling])
sensory_profiling_to_roast_calibration = OperatorPOWL(operator=Operator.XOR, children=[sensory_profiling, roast_calibration])
roast_calibration_to_blend_creation = OperatorPOWL(operator=Operator.XOR, children=[roast_calibration, blend_creation])
blend_creation_to_sustainability_audit = OperatorPOWL(operator=Operator.XOR, children=[blend_creation, sustainability_audit])
sustainability_audit_to_packaging_design = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit, packaging_design])
packaging_design_to_quality_inspection = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, quality_inspection])
quality_inspection_to_inventory_sync = OperatorPOWL(operator=Operator.XOR, children=[quality_inspection, inventory_sync])
inventory_sync_to_logistics_planning = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, logistics_planning])
logistics_planning_to_cafe_training = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning, cafe_training])
cafe_training_to_dynamic_pricing = OperatorPOWL(operator=Operator.XOR, children=[cafe_training, dynamic_pricing])
dynamic_pricing_to_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[dynamic_pricing, customer_feedback])
customer_feedback_to_traceability_logging = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, traceability_logging])

root = StrictPartialOrder(nodes=[
    farm_selection_to_sample_testing,
    sample_testing_to_trade_negotiation,
    trade_negotiation_to_micro_lot_sorting,
    micro_lot_sorting_to_fermentation_control,
    fermentation_control_to_sensory_profiling,
    sensory_profiling_to_roast_calibration,
    roast_calibration_to_blend_creation,
    blend_creation_to_sustainability_audit,
    sustainability_audit_to_packaging_design,
    packaging_design_to_quality_inspection,
    quality_inspection_to_inventory_sync,
    inventory_sync_to_logistics_planning,
    logistics_planning_to_cafe_training,
    cafe_training_to_dynamic_pricing,
    dynamic_pricing_to_customer_feedback,
    customer_feedback_to_traceability_logging
])

root.order.add_edge(farm_selection_to_sample_testing, sample_testing_to_trade_negotiation)
root.order.add_edge(sample_testing_to_trade_negotiation, trade_negotiation_to_micro_lot_sorting)
root.order.add_edge(trade_negotiation_to_micro_lot_sorting, micro_lot_sorting_to_fermentation_control)
root.order.add_edge(micro_lot_sorting_to_fermentation_control, fermentation_control_to_sensory_profiling)
root.order.add_edge(fermentation_control_to_sensory_profiling, sensory_profiling_to_roast_calibration)
root.order.add_edge(sensory_profiling_to_roast_calibration, roast_calibration_to_blend_creation)
root.order.add_edge(roast_calibration_to_blend_creation, blend_creation_to_sustainability_audit)
root.order.add_edge(blend_creation_to_sustainability_audit, sustainability_audit_to_packaging_design)
root.order.add_edge(sustainability_audit_to_packaging_design, packaging_design_to_quality_inspection)
root.order.add_edge(packaging_design_to_quality_inspection, quality_inspection_to_inventory_sync)
root.order.add_edge(quality_inspection_to_inventory_sync, inventory_sync_to_logistics_planning)
root.order.add_edge(inventory_sync_to_logistics_planning, logistics_planning_to_cafe_training)
root.order.add_edge(logistics_planning_to_cafe_training, cafe_training_to_dynamic_pricing)
root.order.add_edge(cafe_training_to_dynamic_pricing, dynamic_pricing_to_customer_feedback)
root.order.add_edge(dynamic_pricing_to_customer_feedback, customer_feedback_to_traceability_logging)