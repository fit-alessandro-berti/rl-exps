import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
farm_selection      = Transition(label='Farm Selection')
milk_testing        = Transition(label='Milk Testing')
starter_culture     = Transition(label='Starter Culture')
curd_formation      = Transition(label='Curd Formation')
pressing_cheese     = Transition(label='Pressing Cheese')
microbial_profiling = Transition(label='Microbial Profiling')
aging_control       = Transition(label='Aging Control')
hand_wrapping       = Transition(label='Hand Wrapping')
quality_audit       = Transition(label='Quality Audit')
packaging_prep      = Transition(label='Packaging Prep')
climate_shipping    = Transition(label='Climate Shipping')
retail_coordination = Transition(label='Retail Coordination')
seasonal_review     = Transition(label='Seasonal Review')
consumer_survey     = Transition(label='Consumer Survey')
feedback_analysis   = Transition(label='Feedback Analysis')
market_adjustment   = Transition(label='Market Adjustment')

# Loop for seasonal aging & climate shipping
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[aging_control, climate_shipping]
)

# Choice for either retail or market adjustment
retail_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[retail_coordination, market_adjustment]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    farm_selection,
    milk_testing,
    starter_culture,
    curd_formation,
    pressing_cheese,
    microbial_profiling,
    aging_loop,
    hand_wrapping,
    quality_audit,
    packaging_prep,
    seasonal_review,
    consumer_survey,
    feedback_analysis,
    retail_choice
])

# Sequential dependencies
root.order.add_edge(farm_selection, milk_testing)
root.order.add_edge(milk_testing, starter_culture)
root.order.add_edge(starter_culture, curd_formation)
root.order.add_edge(curd_formation, pressing_cheese)
root.order.add_edge(pressing_cheese, microbial_profiling)
root.order.add_edge(microbial_profiling, aging_loop)
root.order.add_edge(aging_loop, hand_wrapping)
root.order.add_edge(hand_wrapping, quality_audit)
root.order.add_edge(quality_audit, packaging_prep)

# Concurrency after packaging
root.order.add_edge(packaging_prep, seasonal_review)
root.order.add_edge(packaging_prep, consumer_survey)

# After seasonal review, either retail or market adjustment
root.order.add_edge(seasonal_review, retail_choice)
root.order.add_edge(consumer_survey, retail_choice)

# Final choice either retail or market adjustment
root.order.add_edge(retail_choice, feedback_analysis)
root.order.add_edge(retail_choice, market_adjustment)