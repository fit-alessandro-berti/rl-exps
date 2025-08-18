from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Define the POWL model
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, quality_audit])
xor_handwrapping = OperatorPOWL(operator=Operator.XOR, children=[hand_wrapping, skip])
xor_review = OperatorPOWL(operator=Operator.XOR, children=[seasonal_review, skip])
xor_survey = OperatorPOWL(operator=Operator.XOR, children=[consumer_survey, skip])
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[feedback_analysis, skip])
xor_market = OperatorPOWL(operator=Operator.XOR, children=[market_adjustment, skip])

root = StrictPartialOrder(nodes=[farm_selection, milk_testing, starter_culture, curd_formation, pressing_cheese,
                                  microbial_profiling, loop_aging, xor_handwrapping, xor_review, xor_survey,
                                  xor_feedback, xor_market])
root.order.add_edge(farm_selection, milk_testing)
root.order.add_edge(milk_testing, starter_culture)
root.order.add_edge(starter_culture, curd_formation)
root.order.add_edge(curd_formation, pressing_cheese)
root.order.add_edge(pressing_cheese, microbial_profiling)
root.order.add_edge(microbial_profiling, loop_aging)
root.order.add_edge(loop_aging, xor_handwrapping)
root.order.add_edge(xor_handwrapping, xor_review)
root.order.add_edge(xor_review, xor_survey)
root.order.add_edge(xor_survey, xor_feedback)
root.order.add_edge(xor_feedback, xor_market)

print(root)