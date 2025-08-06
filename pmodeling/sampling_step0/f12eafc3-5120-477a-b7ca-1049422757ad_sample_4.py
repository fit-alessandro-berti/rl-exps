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

skip = SilentTransition()

# Milk Selection -> Quality Testing -> Milk Pasteurize
milk_selection_to_quality_testing = OperatorPOWL(operator=Operator.PO, children=[milk_selection, quality_testing])
quality_testing_to_milk_pasteurize = OperatorPOWL(operator=Operator.PO, children=[quality_testing, milk_pasteurize])

# Milk Pasteurize -> Cheese Crafting
milk_pasteurize_to_cheese_crafting = OperatorPOWL(operator=Operator.PO, children=[milk_pasteurize, cheese_crafting])

# Cheese Crafting -> Controlled Aging
cheese_crafting_to_controlled_aging = OperatorPOWL(operator=Operator.PO, children=[cheese_crafting, controlled_aging])

# Controlled Aging -> Sensory Review
controlled_aging_to_sensory_review = OperatorPOWL(operator=Operator.PO, children=[controlled_aging, sensory_review])

# Sensory Review -> Custom Packaging
sensory_review_to_custom_packaging = OperatorPOWL(operator=Operator.PO, children=[sensory_review, custom_packaging])

# Custom Packaging -> Label Printing
custom_packaging_to_label_printing = OperatorPOWL(operator=Operator.PO, children=[custom_packaging, label_printing])

# Label Printing -> Export Licensing
label_printing_to_export_licensing = OperatorPOWL(operator=Operator.PO, children=[label_printing, export_licensing])

# Export Licensing -> Documentation Prep
export_licensing_to_documentation_prep = OperatorPOWL(operator=Operator.PO, children=[export_licensing, documentation_prep])

# Documentation Prep -> Customs Clearance
documentation_prep_to_customs_clearance = OperatorPOWL(operator=Operator.PO, children=[documentation_prep, customs_clearance])

# Customs Clearance -> Cold Shipping
customs_clearance_to_cold_shipping = OperatorPOWL(operator=Operator.PO, children=[customs_clearance, cold_shipping])

# Cold Shipping -> Delivery Tracking
cold_shipping_to_delivery_tracking = OperatorPOWL(operator=Operator.PO, children=[cold_shipping, delivery_tracking])

# Delivery Tracking -> Feedback Review
delivery_tracking_to_feedback_review = OperatorPOWL(operator=Operator.PO, children=[delivery_tracking, feedback_review])

# Feedback Review -> Market Analysis
feedback_review_to_market_analysis = OperatorPOWL(operator=Operator.PO, children=[feedback_review, market_analysis])

root = StrictPartialOrder(nodes=[milk_selection_to_quality_testing, quality_testing_to_milk_pasteurize, milk_pasteurize_to_cheese_crafting, cheese_crafting_to_controlled_aging, controlled_aging_to_sensory_review, sensory_review_to_custom_packaging, custom_packaging_to_label_printing, label_printing_to_export_licensing, export_licensing_to_documentation_prep, documentation_prep_to_customs_clearance, customs_clearance_to_cold_shipping, cold_shipping_to_delivery_tracking, delivery_tracking_to_feedback_review, feedback_review_to_market_analysis])

root.order.add_edge(milk_selection_to_quality_testing, quality_testing_to_milk_pasteurize)
root.order.add_edge(quality_testing_to_milk_pasteurize, milk_pasteurize_to_cheese_crafting)
root.order.add_edge(milk_pasteurize_to_cheese_crafting, cheese_crafting_to_controlled_aging)
root.order.add_edge(cheese_crafting_to_controlled_aging, controlled_aging_to_sensory_review)
root.order.add_edge(controlled_aging_to_sensory_review, sensory_review_to_custom_packaging)
root.order.add_edge(sensory_review_to_custom_packaging, custom_packaging_to_label_printing)
root.order.add_edge(custom_packaging_to_label_printing, label_printing_to_export_licensing)
root.order.add_edge(label_printing_to_export_licensing, export_licensing_to_documentation_prep)
root.order.add_edge(export_licensing_to_documentation_prep, documentation_prep_to_customs_clearance)
root.order.add_edge(documentation_prep_to_customs_clearance, customs_clearance_to_cold_shipping)
root.order.add_edge(customs_clearance_to_cold_shipping, cold_shipping_to_delivery_tracking)
root.order.add_edge(cold_shipping_to_delivery_tracking, delivery_tracking_to_feedback_review)
root.order.add_edge(delivery_tracking_to_feedback_review, feedback_review_to_market_analysis)