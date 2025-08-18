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

# Define the process using the defined activities
farm_selection_to_milk_testing = OperatorPOWL(operator=Operator.XOR, children=[farm_selection, skip])
milk_testing_to_starter_culture = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, skip])
starter_culture_to_curd_formation = OperatorPOWL(operator=Operator.XOR, children=[starter_culture, skip])
curd_formation_to_pressing_cheese = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, skip])
pressing_cheese_to_microbial_profiling = OperatorPOWL(operator=Operator.XOR, children=[pressing_cheese, skip])
microbial_profiling_to_aging_control = OperatorPOWL(operator=Operator.XOR, children=[microbial_profiling, skip])
aging_control_to_hand_wrapping = OperatorPOWL(operator=Operator.XOR, children=[aging_control, skip])
hand_wrapping_to_quality_audit = OperatorPOWL(operator=Operator.XOR, children=[hand_wrapping, skip])
quality_audit_to_packaging_prep = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, skip])
packaging_prep_to_climate_shipping = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])
climate_shipping_to_retail_coordination = OperatorPOWL(operator=Operator.XOR, children=[climate_shipping, skip])
retail_coordination_to_seasonal_review = OperatorPOWL(operator=Operator.XOR, children=[retail_coordination, skip])
seasonal_review_to_consumer_survey = OperatorPOWL(operator=Operator.XOR, children=[seasonal_review, skip])
consumer_survey_to_feedback_analysis = OperatorPOWL(operator=Operator.XOR, children=[consumer_survey, skip])
feedback_analysis_to_market_adjustment = OperatorPOWL(operator=Operator.XOR, children=[feedback_analysis, skip])

root = StrictPartialOrder(nodes=[
    farm_selection_to_milk_testing,
    milk_testing_to_starter_culture,
    starter_culture_to_curd_formation,
    curd_formation_to_pressing_cheese,
    pressing_cheese_to_microbial_profiling,
    microbial_profiling_to_aging_control,
    aging_control_to_hand_wrapping,
    hand_wrapping_to_quality_audit,
    quality_audit_to_packaging_prep,
    packaging_prep_to_climate_shipping,
    climate_shipping_to_retail_coordination,
    retail_coordination_to_seasonal_review,
    seasonal_review_to_consumer_survey,
    consumer_survey_to_feedback_analysis,
    feedback_analysis_to_market_adjustment
])