import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the loops and exclusive choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[farm_selection, sample_testing, trade_negotiation])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[micro_lot_sorting, fermentation_control, sensory_profiling, roast_calibration])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[blend_creation, sustainability_audit])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, quality_inspection])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[inventory_sync, logistics_planning])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[cafe_training, dynamic_pricing])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, traceability_logging])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop1)

# Print the root
print(root)