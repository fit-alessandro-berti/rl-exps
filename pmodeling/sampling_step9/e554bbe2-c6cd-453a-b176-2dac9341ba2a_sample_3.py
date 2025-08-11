import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define exclusive choice for microbial profiling and hand wrapping
xor = OperatorPOWL(operator=Operator.XOR, children=[microbial_profiling, hand_wrapping])

# Define loop for quality audit and packaging prep
loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_audit, packaging_prep])

# Define loop for climate shipping and retail coordination
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_shipping, retail_coordination])

# Define loop for seasonal review and consumer survey
seasonal_loop = OperatorPOWL(operator=Operator.LOOP, children=[seasonal_review, consumer_survey])

# Define loop for feedback analysis and market adjustment
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_analysis, market_adjustment])

# Define the root POWL model
root = StrictPartialOrder(nodes=[farm_selection, milk_testing, starter_culture, curd_formation, pressing_cheese, xor, loop, climate_loop, seasonal_loop, feedback_loop])
root.order.add_edge(farm_selection, milk_testing)
root.order.add_edge(milk_testing, starter_culture)
root.order.add_edge(starter_culture, curd_formation)
root.order.add_edge(curd_formation, pressing_cheese)
root.order.add_edge(pressing_cheese, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, climate_loop)
root.order.add_edge(climate_loop, seasonal_loop)
root.order.add_edge(seasonal_loop, feedback_loop)
root.order.add_edge(feedback_loop, loop)