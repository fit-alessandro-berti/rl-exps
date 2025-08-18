import pm4py
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

# Define partial order
root = StrictPartialOrder(nodes=[
    milk_selection,
    quality_testing,
    milk_pasteurize,
    cheese_crafting,
    controlled_aging,
    sensory_review,
    custom_packaging,
    label_printing,
    export_licensing,
    documentation_prep,
    customs_clearance,
    cold_shipping,
    delivery_tracking,
    feedback_review,
    market_analysis
])

# Define dependencies
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

# Save the final result in the variable 'root'
print(root)