import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
farm_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[farm_selection, sample_testing])
trade_negotiation_loop = OperatorPOWL(operator=Operator.LOOP, children=[trade_negotiation, skip])
sensory_profiling_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensory_profiling, skip])
fermentation_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_control, skip])
roast_calibration_loop = OperatorPOWL(operator=Operator.LOOP, children=[roast_calibration, skip])
blend_creation_loop = OperatorPOWL(operator=Operator.LOOP, children=[blend_creation, skip])
inventory_sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_sync, skip])
logistics_planning_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_planning, skip])
cafe_training_loop = OperatorPOWL(operator=Operator.LOOP, children=[cafe_training, skip])
dynamic_pricing_loop = OperatorPOWL(operator=Operator.LOOP, children=[dynamic_pricing, skip])
customer_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, skip])
traceability_logging_loop = OperatorPOWL(operator=Operator.LOOP, children=[traceability_logging, skip])

# Define exclusive choice nodes
exclusive_choice1 = OperatorPOWL(operator=Operator.XOR, children=[farm_selection_loop, trade_negotiation_loop])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[sensory_profiling_loop, fermentation_control_loop])
exclusive_choice3 = OperatorPOWL(operator=Operator.XOR, children=[roast_calibration_loop, blend_creation_loop])
exclusive_choice4 = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync_loop, logistics_planning_loop])
exclusive_choice5 = OperatorPOWL(operator=Operator.XOR, children=[cafe_training_loop, dynamic_pricing_loop])
exclusive_choice6 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback_loop, traceability_logging_loop])

# Define the root node
root = StrictPartialOrder(nodes=[exclusive_choice1, exclusive_choice2, exclusive_choice3, exclusive_choice4, exclusive_choice5, exclusive_choice6])

# Define the order dependencies
root.order.add_edge(exclusive_choice1, exclusive_choice2)
root.order.add_edge(exclusive_choice2, exclusive_choice3)
root.order.add_edge(exclusive_choice3, exclusive_choice4)
root.order.add_edge(exclusive_choice4, exclusive_choice5)
root.order.add_edge(exclusive_choice5, exclusive_choice6)