from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define exclusive choices and loops
exclusive_choice_milk = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, starter_culture])
exclusive_choice_curd = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, pressing_cheese])
exclusive_choice_microbial = OperatorPOWL(operator=Operator.XOR, children=[microbial_profiling, aging_control])
exclusive_choice_hand_wrapping = OperatorPOWL(operator=Operator.XOR, children=[hand_wrapping, quality_audit])
exclusive_choice_packaging = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, climate_shipping])
exclusive_choice_retail = OperatorPOWL(operator=Operator.XOR, children=[retail_coordination, seasonal_review])
exclusive_choice_survey = OperatorPOWL(operator=Operator.XOR, children=[consumer_survey, feedback_analysis])
exclusive_choice_market = OperatorPOWL(operator=Operator.XOR, children=[market_adjustment, None])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    farm_selection, exclusive_choice_milk, exclusive_choice_curd, exclusive_choice_microbial, exclusive_choice_hand_wrapping,
    exclusive_choice_packaging, exclusive_choice_retail, exclusive_choice_survey, exclusive_choice_market
])

# Define dependencies between nodes
root.order.add_edge(farm_selection, exclusive_choice_milk)
root.order.add_edge(farm_selection, exclusive_choice_curd)
root.order.add_edge(farm_selection, exclusive_choice_microbial)
root.order.add_edge(farm_selection, exclusive_choice_hand_wrapping)
root.order.add_edge(farm_selection, exclusive_choice_packaging)
root.order.add_edge(farm_selection, exclusive_choice_retail)
root.order.add_edge(farm_selection, exclusive_choice_survey)
root.order.add_edge(farm_selection, exclusive_choice_market)

# Additional dependencies can be added here based on the specific process flow