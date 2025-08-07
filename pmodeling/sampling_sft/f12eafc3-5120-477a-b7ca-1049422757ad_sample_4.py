import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk_selection    = Transition(label='Milk Selection')
quality_testing   = Transition(label='Quality Testing')
milk_pasteurize   = Transition(label='Milk Pasteurize')
cheese_crafting   = Transition(label='Cheese Crafting')
controlled_aging  = Transition(label='Controlled Aging')
sensory_review    = Transition(label='Sensory Review')
custom_packaging  = Transition(label='Custom Packaging')
label_printing    = Transition(label='Label Printing')
export_licensing  = Transition(label='Export Licensing')
documentation_prep= Transition(label='Documentation Prep')
customs_clearance = Transition(label='Customs Clearance')
cold_shipping     = Transition(label='Cold Shipping')
delivery_tracking = Transition(label='Delivery Tracking')
feedback_review   = Transition(label='Feedback Review')
market_analysis   = Transition(label='Market Analysis')

# Loop for the controlled aging and sensory review steps
# Concurrency: both can happen in parallel within the aging period
# Loop: do sensory review after aging, then optionally repeat
loop_aging_sensory = OperatorPOWL(
    operator=Operator.LOOP,
    children=[controlled_aging, sensory_review]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk_selection,
    quality_testing,
    milk_pasteurize,
    cheese_crafting,
    loop_aging_sensory,
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

# Sequence: milk -> testing -> pasteurize -> crafting
root.order.add_edge(milk_selection,    quality_testing)
root.order.add_edge(quality_testing,   milk_pasteurize)
root.order.add_edge(milk_pasteurize,   cheese_crafting)

# Loop for aging and sensory review
root.order.add_edge(cheese_crafting,   loop_aging_sensory)

# Packaging and labeling after the loop
root.order.add_edge(loop_aging_sensory, custom_packaging)
root.order.add_edge(custom_packaging,   label_printing)

# Licensing and documentation after packaging
root.order.add_edge(label_printing,     export_licensing)
root.order.add_edge(export_licensing,   documentation_prep)

# Clearance and shipping after documentation
root.order.add_edge(documentation_prep, customs_clearance)
root.order.add_edge(customs_clearance,  cold_shipping)

# Tracking and feedback after shipping
root.order.add_edge(cold_shipping,      delivery_tracking)
root.order.add_edge(delivery_tracking,  feedback_review)

# Analysis after feedback
root.order.add_edge(feedback_review,   market_analysis)