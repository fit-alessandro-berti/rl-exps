import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[starter_culture, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, hand_wrapping, quality_audit, packaging_prep, climate_shipping])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[retail_coordination, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[seasonal_review, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[consumer_survey, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[feedback_analysis, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[market_adjustment, skip])

# Define root
root = StrictPartialOrder(nodes=[farm_selection, milk_testing, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(farm_selection, milk_testing)
root.order.add_edge(milk_testing, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, market_adjustment)