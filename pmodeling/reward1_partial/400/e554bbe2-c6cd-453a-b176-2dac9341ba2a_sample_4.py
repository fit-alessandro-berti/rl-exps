import pm4py
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

aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, quality_audit, packaging_prep])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_shipping, retail_coordination])
seasonal_xor = OperatorPOWL(operator=Operator.XOR, children=[seasonal_review, skip])
consumer_xor = OperatorPOWL(operator=Operator.XOR, children=[consumer_survey, feedback_analysis])
market_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_adjustment])

root = StrictPartialOrder(nodes=[farm_selection, milk_testing, starter_culture, curd_formation, pressing_cheese, microbial_profiling, aging_loop, packaging_loop, seasonal_xor, consumer_xor, market_loop])
root.order.add_edge(farm_selection, milk_testing)
root.order.add_edge(milk_testing, starter_culture)
root.order.add_edge(starter_culture, curd_formation)
root.order.add_edge(curd_formation, pressing_cheese)
root.order.add_edge(pressing_cheese, microbial_profiling)
root.order.add_edge(microbial_profiling, aging_loop)
root.order.add_edge(aging_loop, packaging_loop)
root.order.add_edge(packaging_loop, seasonal_xor)
root.order.add_edge(seasonal_xor, consumer_xor)
root.order.add_edge(consumer_xor, market_loop)

print(root)