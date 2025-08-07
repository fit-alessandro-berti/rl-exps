import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
ingredient_sourcing = Transition(label='Ingredient Sourcing')
quality_testing = Transition(label='Quality Testing')
micro_batch = Transition(label='Micro Batch')
scent_blending = Transition(label='Scent Blending')
sensory_panel = Transition(label='Sensory Panel')
formula_adjust = Transition(label='Formula Adjust')
safety_review = Transition(label='Safety Review')
sustainability_check = Transition(label='Sustainability Check')
prototype_creation = Transition(label='Prototype Creation')
label_approval = Transition(label='Label Approval')
marketing_plan = Transition(label='Marketing Plan')
distribution_prep = Transition(label='Distribution Prep')
sales_launch = Transition(label='Sales Launch')

# Loop for sensory evaluation and formula adjustments
# A = Sensory Panel -> Formula Adjust
sensory_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensory_panel, formula_adjust])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ingredient_sourcing,
    quality_testing,
    micro_batch,
    scent_blending,
    sensory_loop,
    safety_review,
    sustainability_check,
    prototype_creation,
    label_approval,
    marketing_plan,
    distribution_prep,
    sales_launch
])

# Define the control-flow dependencies
root.order.add_edge(ingredient_sourcing, quality_testing)
root.order.add_edge(quality_testing, micro_batch)
root.order.add_edge(micro_batch, scent_blending)
root.order.add_edge(scent_blending, sensory_loop)
root.order.add_edge(sensory_loop, safety_review)
root.order.add_edge(safety_review, sustainability_check)
root.order.add_edge(sustainability_check, prototype_creation)
root.order.add_edge(prototype_creation, label_approval)
root.order.add_edge(label_approval, marketing_plan)
root.order.add_edge(marketing_plan, distribution_prep)
root.order.add_edge(distribution_prep, sales_launch)