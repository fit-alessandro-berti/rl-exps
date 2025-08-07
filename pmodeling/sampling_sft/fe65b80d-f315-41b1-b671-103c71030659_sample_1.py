import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
t_source = Transition(label='Ingredient Sourcing')
t_quality = Transition(label='Quality Testing')
t_blend = Transition(label='Scent Blending')
t_micro = Transition(label='Micro Batch')
t_panel = Transition(label='Sensory Panel')
t_adjust = Transition(label='Formula Adjust')
t_safety = Transition(label='Safety Review')
t_sustain = Transition(label='Sustainability Check')
t_design = Transition(label='Packaging Design')
t_prototype = Transition(label='Prototype Creation')
t_feedback = Transition(label='Client Feedback')
t_label = Transition(label='Label Approval')
t_production = Transition(label='Final Production')
t_marketing = Transition(label='Marketing Plan')
t_prep = Transition(label='Distribution Prep')
t_launch = Transition(label='Sales Launch')

# Loop for sensory panel + formula adjustment
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[t_panel, t_adjust]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    t_source, t_quality, t_blend,
    t_micro, loop,
    t_safety, t_sustain,
    t_design, t_prototype,
    t_feedback, t_label,
    t_production, t_marketing,
    t_prep, t_launch
])

# Define the control-flow dependencies
root.order.add_edge(t_source, t_quality)
root.order.add_edge(t_source, t_blend)
root.order.add_edge(t_quality, t_micro)
root.order.add_edge(t_blend, t_micro)
root.order.add_edge(t_micro, loop)
root.order.add_edge(loop, t_safety)
root.order.add_edge(loop, t_sustain)
root.order.add_edge(t_safety, t_design)
root.order.add_edge(t_sustain, t_design)
root.order.add_edge(t_design, t_prototype)
root.order.add_edge(t_prototype, t_feedback)
root.order.add_edge(t_feedback, t_label)
root.order.add_edge(t_label, t_production)
root.order.add_edge(t_production, t_marketing)
root.order.add_edge(t_marketing, t_prep)
root.order.add_edge(t_prep, t_launch)