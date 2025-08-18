import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the relationships between activities using POWL operators
farm_selection_to_milk_testing = OperatorPOWL(operator=Operator.LOOP, children=[milk_testing])
milk_testing_to_starter_culture = OperatorPOWL(operator=Operator.LOOP, children=[starter_culture])
starter_culture_to_curd_formation = OperatorPOWL(operator=Operator.LOOP, children=[curd_formation])
curd_formation_to_pressing_cheese = OperatorPOWL(operator=Operator.LOOP, children=[pressing_cheese])
pressing_cheese_to_microbial_profiling = OperatorPOWL(operator=Operator.LOOP, children=[microbial_profiling])
microbial_profiling_to_aging_control = OperatorPOWL(operator=Operator.LOOP, children=[aging_control])
aging_control_to_hand_wrapping = OperatorPOWL(operator=Operator.LOOP, children=[hand_wrapping])
hand_wrapping_to_quality_audit = OperatorPOWL(operator=Operator.LOOP, children=[quality_audit])
quality_audit_to_packaging_prep = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep])
packaging_prep_to_climate_shipping = OperatorPOWL(operator=Operator.LOOP, children=[climate_shipping])
climate_shipping_to_retail_coordination = OperatorPOWL(operator=Operator.LOOP, children=[retail_coordination])
retail_coordination_to_seasonal_review = OperatorPOWL(operator=Operator.LOOP, children=[seasonal_review])
seasonal_review_to_consumer_survey = OperatorPOWL(operator=Operator.LOOP, children=[consumer_survey])
consumer_survey_to_feedback_analysis = OperatorPOWL(operator=Operator.LOOP, children=[feedback_analysis])
feedback_analysis_to_market_adjustment = OperatorPOWL(operator=Operator.LOOP, children=[market_adjustment])

# Define the final POWL model
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