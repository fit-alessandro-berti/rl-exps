import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
t_sourcing = Transition(label='Ingredient Sourcing')
t_quality = Transition(label='Quality Testing')
t_scent = Transition(label='Scent Blending')
t_micro = Transition(label='Micro Batch')
t_sensory = Transition(label='Sensory Panel')
t_formula = Transition(label='Formula Adjust')
t_safety = Transition(label='Safety Review')
t_sustain = Transition(label='Sustainability Check')
t_package = Transition(label='Packaging Design')
t_prototype = Transition(label='Prototype Creation')
t_feedback = Transition(label='Client Feedback')
t_label = Transition(label='Label Approval')
t_production = Transition(label='Final Production')
t_marketing = Transition(label='Marketing Plan')
t_distribution = Transition(label='Distribution Prep')
t_sales = Transition(label='Sales Launch')

# Loop for sensory evaluation and feedback
loop_sensory = OperatorPOWL(
    operator=Operator.LOOP,
    children=[t_sensory, t_feedback]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    t_sourcing, t_quality, t_scent, t_micro,
    loop_sensory,
    t_formula, t_safety, t_sustain, t_package,
    t_prototype, t_label, t_production,
    t_marketing, t_distribution, t_sales
])

# Sequential edges
root.order.add_edge(t_sourcing, t_quality)
root.order.add_edge(t_quality, t_scent)
root.order.add_edge(t_scent, t_micro)
root.order.add_edge(t_micro, loop_sensory)

# After sensory/feedback loop
root.order.add_edge(loop_sensory, t_formula)
root.order.add_edge(t_formula, t_safety)
root.order.add_edge(t_formula, t_sustain)
root.order.add_edge(t_safety, t_package)

# After packaging, move to prototype and labeling
root.order.add_edge(t_package, t_prototype)
root.order.add_edge(t_prototype, t_label)

# After prototype and labeling, move to production
root.order.add_edge(t_label, t_production)

# After production, move to marketing and distribution
root.order.add_edge(t_production, t_marketing)
root.order.add_edge(t_marketing, t_distribution)

# After distribution, move to sales launch
root.order.add_edge(t_distribution, t_sales)