import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
farm_selection = Transition(label='Farm Selection')
milk_testing = Transition(label='Milk Testing')
starter_culture = Transition(label='Starter Culture')
curd_formation = Transition(label='Curd Formation')
pressing_cheese = Transition(label='Pressing Cheese')
microbial_profiling = Transition(label='Microbial Profiling')
aging_control = Transition(label='Aging Control')
hand_wrapping = Transition(label='Hand Wrapping')
quality_audit = Transition(label='Quality Audit')
packaging_prep = Transition(label='Packaging Prep')
climate_shipping = Transition(label='Climate Shipping')
retail_coordination = Transition(label='Retail Coordination')
seasonal_review = Transition(label='Seasonal Review')
consumer_survey = Transition(label='Consumer Survey')
feedback_analysis = Transition(label='Feedback Analysis')
market_adjustment = Transition(label='Market Adjustment')

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice transitions
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[starter_culture, milk_testing])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[aging_control, microbial_profiling])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[hand_wrapping, quality_audit])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, climate_shipping])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[retail_coordination, seasonal_review])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[consumer_survey, feedback_analysis])
xor_7 = OperatorPOWL(operator=Operator.XOR, children=[market_adjustment, skip])

# Define the loop transitions
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[farm_selection, xor_1])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[curd_formation, xor_2])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[pressing_cheese, xor_3])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[xor_4, xor_5])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[xor_6, xor_7])

# Define the partial order
root = StrictPartialOrder(nodes=[loop_1, loop_2, loop_3, loop_4, loop_5, xor_1, xor_2, xor_3, xor_4, xor_5, xor_6, xor_7])
root.order.add_edge(loop_1, xor_1)
root.order.add_edge(loop_2, xor_2)
root.order.add_edge(loop_3, xor_3)
root.order.add_edge(loop_4, xor_4)
root.order.add_edge(loop_5, xor_5)
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, loop_3)
root.order.add_edge(loop_3, loop_4)
root.order.add_edge(loop_4, loop_5)
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, xor_4)
root.order.add_edge(xor_4, xor_5)
root.order.add_edge(xor_5, xor_6)
root.order.add_edge(xor_6, xor_7)