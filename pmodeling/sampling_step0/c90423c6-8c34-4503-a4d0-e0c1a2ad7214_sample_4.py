from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transition
skip = SilentTransition()

# Define the loops and exclusive choices
farm_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[farm_selection, sample_testing])
trade_negotiation_loop = OperatorPOWL(operator=Operator.LOOP, children=[trade_negotiation, skip])
micro_lot_sorting_loop = OperatorPOWL(operator=Operator.LOOP, children=[micro_lot_sorting, skip])
fermentation_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_control, skip])
sensory_profiling_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensory_profiling, skip])
roast_calibration_loop = OperatorPOWL(operator=Operator.LOOP, children=[roast_calibration, skip])
blend_creation_loop = OperatorPOWL(operator=Operator.LOOP, children=[blend_creation, skip])
sustainability_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_audit, skip])
packaging_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, skip])
quality_inspection_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspection, skip])
inventory_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_sync, skip])
logistics_planning_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_planning, skip])
cafe_training_loop = OperatorPOWL(operator=Operator.LOOP, children=[cafe_training, skip])
dynamic_pricing_loop = OperatorPOWL(operator=Operator.LOOP, children=[dynamic_pricing, skip])
customer_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, skip])
traceability_logging_loop = OperatorPOWL(operator=Operator.LOOP, children=[traceability_logging, skip])

# Define the exclusive choices
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[trade_negotiation_loop, skip])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[micro_lot_sorting_loop, skip])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[fermentation_control_loop, skip])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[sensory_profiling_loop, skip])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[roast_calibration_loop, skip])
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[blend_creation_loop, skip])
exclusive_choice_7 = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit_loop, skip])
exclusive_choice_8 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design_loop, skip])
exclusive_choice_9 = OperatorPOWL(operator=Operator.XOR, children=[quality_inspection_loop, skip])
exclusive_choice_10 = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync_loop, skip])
exclusive_choice_11 = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning_loop, skip])
exclusive_choice_12 = OperatorPOWL(operator=Operator.XOR, children=[cafe_training_loop, skip])
exclusive_choice_13 = OperatorPOWL(operator=Operator.XOR, children=[dynamic_pricing_loop, skip])
exclusive_choice_14 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback_loop, skip])
exclusive_choice_15 = OperatorPOWL(operator=Operator.XOR, children=[traceability_logging_loop, skip])

# Define the root model
root = StrictPartialOrder(nodes=[
    farm_selection_loop,
    trade_negotiation_loop,
    micro_lot_sorting_loop,
    fermentation_control_loop,
    sensory_profiling_loop,
    roast_calibration_loop,
    blend_creation_loop,
    sustainability_audit_loop,
    packaging_design_loop,
    quality_inspection_loop,
    inventory_sync_loop,
    logistics_planning_loop,
    cafe_training_loop,
    dynamic_pricing_loop,
    customer_feedback_loop,
    traceability_logging_loop
])

# Add the order edges
root.order.add_edge(farm_selection_loop, trade_negotiation_loop)
root.order.add_edge(farm_selection_loop, micro_lot_sorting_loop)
root.order.add_edge(trade_negotiation_loop, exclusive_choice_1)
root.order.add_edge(micro_lot_sorting_loop, exclusive_choice_2)
root.order.add_edge(exclusive_choice_1, fermentation_control_loop)
root.order.add_edge(exclusive_choice_2, sensory_profiling_loop)
root.order.add_edge(fermentation_control_loop, exclusive_choice_3)
root.order.add_edge(sensory_profiling_loop, roast_calibration_loop)
root.order.add_edge(exclusive_choice_3, blend_creation_loop)
root.order.add_edge(roast_calibration_loop, sustainability_audit_loop)
root.order.add_edge(blend_creation_loop, packaging_design_loop)
root.order.add_edge(sustainability_audit_loop, quality_inspection_loop)
root.order.add_edge(packaging_design_loop, inventory_sync_loop)
root.order.add_edge(quality_inspection_loop, logistics_planning_loop)
root.order.add_edge(inventory_sync_loop, cafe_training_loop)
root.order.add_edge(logistics_planning_loop, dynamic_pricing_loop)
root.order.add_edge(cafe_training_loop, customer_feedback_loop)
root.order.add_edge(dynamic_pricing_loop, traceability_logging_loop)
root.order.add_edge(customer_feedback_loop, exclusive_choice_4)
root.order.add_edge(traceability_logging_loop, exclusive_choice_5)
root.order.add_edge(exclusive_choice_4, exclusive_choice_6)
root.order.add_edge(exclusive_choice_5, exclusive_choice_7)
root.order.add_edge(exclusive_choice_6, exclusive_choice_8)
root.order.add_edge(exclusive_choice_7, exclusive_choice_9)
root.order.add_edge(exclusive_choice_8, exclusive_choice_10)
root.order.add_edge(exclusive_choice_9, exclusive_choice_11)
root.order.add_edge(exclusive_choice_10, exclusive_choice_12)
root.order.add_edge(exclusive_choice_11, exclusive_choice_13)
root.order.add_edge(exclusive_choice_12, exclusive_choice_14)
root.order.add_edge(exclusive_choice_13, exclusive_choice_15)

print(root)