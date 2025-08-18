from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (tau labels)
skip = SilentTransition()

# Construct the POWL model
root = StrictPartialOrder()

# Add nodes to the root
root.nodes.add(milk_selection)
root.nodes.add(quality_testing)
root.nodes.add(milk_pasteurize)
root.nodes.add(cheese_crafting)
root.nodes.add(controlled_aging)
root.nodes.add(sensory_review)
root.nodes.add(custom_packaging)
root.nodes.add(label_printing)
root.nodes.add(export_licensing)
root.nodes.add(documentation_prep)
root.nodes.add(customs_clearance)
root.nodes.add(cold_shipping)
root.nodes.add(delivery_tracking)
root.nodes.add(feedback_review)
root.nodes.add(market_analysis)

# Define dependencies between nodes
root.order.add_edge(milk_selection, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, cheese_crafting)
root.order.add_edge(cheese_crafting, controlled_aging)
root.order.add_edge(controlled_aging, sensory_review)
root.order.add_edge(sensory_review, custom_packaging)
root.order.add_edge(custom_packaging, label_printing)
root.order.add_edge(label_printing, export_licensing)
root.order.add_edge(export_licensing, documentation_prep)
root.order.add_edge(documentation_prep, customs_clearance)
root.order.add_edge(customs_clearance, cold_shipping)
root.order.add_edge(cold_shipping, delivery_tracking)
root.order.add_edge(delivery_tracking, feedback_review)
root.order.add_edge(feedback_review, market_analysis)