import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the coffee sourcing and distribution process
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

# Define the relationships between activities
xor1 = OperatorPOWL(operator=Operator.XOR, children=[trade_negotiation, sample_testing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[micro_lot_sorting, fermentation_control])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[sensory_profiling, roast_calibration])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[blend_creation, sustainability_audit])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, quality_inspection])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, logistics_planning])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[cafe_training, dynamic_pricing])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, traceability_logging])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[farm_selection, xor1])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor2, xor3])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor4, xor5])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor6, xor7])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[xor8])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)
root.order.add_edge(loop5, xor5)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor1)

# Print the POWL model
print(root)