import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

milk_selection = Transition(label='Milk Selection')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
cheese_crafting = Transition(label='Cheese Crafting')
controlled_aging = Transition(label='Controlled Aging')
sensory_review = Transition(label='Sensory Review')
custom_packaging = Transition(label='Custom Packaging')
label_printing = Transition(label='Label Printing')
export_licensing = Transition(label='Export Licensing')
documentation_prep = Transition(label='Documentation Prep')
customs_clearance = Transition(label='Customs Clearance')
cold_shipping = Transition(label='Cold Shipping')
delivery_tracking = Transition(label='Delivery Tracking')
feedback_review = Transition(label='Feedback Review')
market_analysis = Transition(label='Market Analysis')

# Define the control flow
# Milk selection and quality testing are concurrent
milk_selection_and_quality_testing = OperatorPOWL(operator=Operator.XOR, children=[milk_selection, quality_testing])

# Milk pasteurization is a prerequisite for cheese crafting
milk_pasteurize_then_cheese_crafting = OperatorPOWL(operator=Operator.LOOP, children=[milk_pasteurize, cheese_crafting])

# Controlled aging is a prerequisite for sensory review
controlled_aging_then_sensory_review = OperatorPOWL(operator=Operator.LOOP, children=[controlled_aging, sensory_review])

# Custom packaging is a prerequisite for label printing
custom_packaging_then_label_printing = OperatorPOWL(operator=Operator.LOOP, children=[custom_packaging, label_printing])

# Export licensing is a prerequisite for documentation preparation
export_licensing_then_documentation_prep = OperatorPOWL(operator=Operator.LOOP, children=[export_licensing, documentation_prep])

# Customs clearance is a prerequisite for cold shipping
customs_clearance_then_cold_shipping = OperatorPOWL(operator=Operator.LOOP, children=[customs_clearance, cold_shipping])

# Delivery tracking is a prerequisite for feedback review
delivery_tracking_then_feedback_review = OperatorPOWL(operator=Operator.LOOP, children=[delivery_tracking, feedback_review])

# Market analysis is a prerequisite for the end of the process
market_analysis_then_end = OperatorPOWL(operator=Operator.LOOP, children=[market_analysis])

# Define the strict partial order
root = StrictPartialOrder(nodes=[
    milk_selection_and_quality_testing,
    milk_pasteurize_then_cheese_crafting,
    controlled_aging_then_sensory_review,
    custom_packaging_then_label_printing,
    export_licensing_then_documentation_prep,
    customs_clearance_then_cold_shipping,
    delivery_tracking_then_feedback_review,
    market_analysis_then_end
])

# Define the dependencies
root.order.add_edge(milk_selection_and_quality_testing, milk_pasteurize_then_cheese_crafting)
root.order.add_edge(milk_pasteurize_then_cheese_crafting, controlled_aging_then_sensory_review)
root.order.add_edge(controlled_aging_then_sensory_review, custom_packaging_then_label_printing)
root.order.add_edge(custom_packaging_then_label_printing, export_licensing_then_documentation_prep)
root.order.add_edge(export_licensing_then_documentation_prep, customs_clearance_then_cold_shipping)
root.order.add_edge(customs_clearance_then_cold_shipping, delivery_tracking_then_feedback_review)
root.order.add_edge(delivery_tracking_then_feedback_review, market_analysis_then_end)