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

# Define partial order
root = StrictPartialOrder(nodes=[
    farm_selection, 
    milk_testing, 
    starter_culture, 
    curd_formation, 
    pressing_cheese, 
    microbial_profiling, 
    aging_control, 
    hand_wrapping, 
    quality_audit, 
    packaging_prep, 
    climate_shipping, 
    retail_coordination, 
    seasonal_review, 
    consumer_survey, 
    feedback_analysis, 
    market_adjustment
])

# Define dependencies
root.order.add_edge(farm_selection, milk_testing)
root.order.add_edge(milk_testing, starter_culture)
root.order.add_edge(starter_culture, curd_formation)
root.order.add_edge(curd_formation, pressing_cheese)
root.order.add_edge(pressing_cheese, microbial_profiling)
root.order.add_edge(microbial_profiling, aging_control)
root.order.add_edge(aging_control, hand_wrapping)
root.order.add_edge(hand_wrapping, quality_audit)
root.order.add_edge(quality_audit, packaging_prep)
root.order.add_edge(packaging_prep, climate_shipping)
root.order.add_edge(climate_shipping, retail_coordination)
root.order.add_edge(retail_coordination, seasonal_review)
root.order.add_edge(seasonal_review, consumer_survey)
root.order.add_edge(consumer_survey, feedback_analysis)
root.order.add_edge(feedback_analysis, market_adjustment)

print(root)