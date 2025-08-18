from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions representing the activities
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

# Define silent transitions for no-op steps
skip = SilentTransition()

# Define the partial order nodes and their dependencies
loop_farm_selection = OperatorPOWL(operator=Operator.LOOP, children=[farm_selection, sample_testing])
xor_trade_negotiation = OperatorPOWL(operator=Operator.XOR, children=[trade_negotiation, skip])
xor_micro_lot_sorting = OperatorPOWL(operator=Operator.XOR, children=[micro_lot_sorting, skip])
xor_fermentation_control = OperatorPOWL(operator=Operator.XOR, children=[fermentation_control, skip])
xor_sensory_profiling = OperatorPOWL(operator=Operator.XOR, children=[sensory_profiling, skip])
xor_roast_calibration = OperatorPOWL(operator=Operator.XOR, children=[roast_calibration, skip])
xor_blend_creation = OperatorPOWL(operator=Operator.XOR, children=[blend_creation, skip])
xor_sustainability_audit = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit, skip])
xor_packaging_design = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, skip])
xor_quality_inspection = OperatorPOWL(operator=Operator.XOR, children=[quality_inspection, skip])
xor_inventory_sync = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, skip])
xor_logistics_planning = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning, skip])
xor_cafe_training = OperatorPOWL(operator=Operator.XOR, children=[cafe_training, skip])
xor_dynamic_pricing = OperatorPOWL(operator=Operator.XOR, children=[dynamic_pricing, skip])
xor_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip])
xor_traceability_logging = OperatorPOWL(operator=Operator.XOR, children=[traceability_logging, skip])

# Create the root partial order with the defined nodes and their dependencies
root = StrictPartialOrder(nodes=[
    loop_farm_selection,
    xor_trade_negotiation,
    xor_micro_lot_sorting,
    xor_fermentation_control,
    xor_sensory_profiling,
    xor_roast_calibration,
    xor_blend_creation,
    xor_sustainability_audit,
    xor_packaging_design,
    xor_quality_inspection,
    xor_inventory_sync,
    xor_logistics_planning,
    xor_cafe_training,
    xor_dynamic_pricing,
    xor_customer_feedback,
    xor_traceability_logging
])

# Add dependencies between nodes if necessary (e.g., loop dependencies)
root.order.add_edge(loop_farm_selection, xor_trade_negotiation)
root.order.add_edge(loop_farm_selection, xor_micro_lot_sorting)
root.order.add_edge(loop_farm_selection, xor_fermentation_control)
root.order.add_edge(loop_farm_selection, xor_sensory_profiling)
root.order.add_edge(loop_farm_selection, xor_roast_calibration)
root.order.add_edge(loop_farm_selection, xor_blend_creation)
root.order.add_edge(loop_farm_selection, xor_sustainability_audit)
root.order.add_edge(loop_farm_selection, xor_packaging_design)
root.order.add_edge(loop_farm_selection, xor_quality_inspection)
root.order.add_edge(loop_farm_selection, xor_inventory_sync)
root.order.add_edge(loop_farm_selection, xor_logistics_planning)
root.order.add_edge(loop_farm_selection, xor_cafe_training)
root.order.add_edge(loop_farm_selection, xor_dynamic_pricing)
root.order.add_edge(loop_farm_selection, xor_customer_feedback)
root.order.add_edge(loop_farm_selection, xor_traceability_logging)

print(root)