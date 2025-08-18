import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the exclusive choices and loops
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[trade_negotiation, sample_testing])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[sensory_profiling, fermentation_control])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[roast_calibration, blend_creation])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit, packaging_design])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[quality_inspection, inventory_sync])
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning, cafe_training])
exclusive_choice_7 = OperatorPOWL(operator=Operator.XOR, children=[dynamic_pricing, customer_feedback])
exclusive_choice_8 = OperatorPOWL(operator=Operator.XOR, children=[traceability_logging])

# Construct the process using the exclusive choices and loops
root = StrictPartialOrder(nodes=[
    farm_selection,
    exclusive_choice_1,
    exclusive_choice_2,
    exclusive_choice_3,
    exclusive_choice_4,
    exclusive_choice_5,
    exclusive_choice_6,
    exclusive_choice_7,
    exclusive_choice_8
])

# Define the dependencies between the nodes
root.order.add_edge(farm_selection, exclusive_choice_1)
root.order.add_edge(exclusive_choice_1, exclusive_choice_2)
root.order.add_edge(exclusive_choice_2, exclusive_choice_3)
root.order.add_edge(exclusive_choice_3, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, exclusive_choice_7)
root.order.add_edge(exclusive_choice_7, exclusive_choice_8)
root.order.add_edge(exclusive_choice_8, traceability_logging)