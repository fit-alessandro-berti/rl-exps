import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
ingredient_sourcing = Transition(label='Ingredient Sourcing')
quality_testing = Transition(label='Quality Testing')
scent_blending = Transition(label='Scent Blending')
micro_batch = Transition(label='Micro Batch')
sensory_panel = Transition(label='Sensory Panel')
formula_adjust = Transition(label='Formula Adjust')
safety_review = Transition(label='Safety Review')
sustainability_check = Transition(label='Sustainability Check')
packaging_design = Transition(label='Packaging Design')
prototype_creation = Transition(label='Prototype Creation')
client_feedback = Transition(label='Client Feedback')
label_approval = Transition(label='Label Approval')
final_production = Transition(label='Final Production')
marketing_plan = Transition(label='Marketing Plan')
distribution_prep = Transition(label='Distribution Prep')
sales_launch = Transition(label='Sales Launch')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    ingredient_sourcing,
    quality_testing,
    scent_blending,
    micro_batch,
    sensory_panel,
    formula_adjust,
    safety_review,
    sustainability_check,
    packaging_design,
    prototype_creation,
    client_feedback,
    label_approval,
    final_production,
    marketing_plan,
    distribution_prep,
    sales_launch
])

# Define the order of activities
root.order.add_edge(ingredient_sourcing, quality_testing)
root.order.add_edge(quality_testing, scent_blending)
root.order.add_edge(scent_blending, micro_batch)
root.order.add_edge(micro_batch, sensory_panel)
root.order.add_edge(sensory_panel, formula_adjust)
root.order.add_edge(formula_adjust, safety_review)
root.order.add_edge(safety_review, sustainability_check)
root.order.add_edge(sustainability_check, packaging_design)
root.order.add_edge(packaging_design, prototype_creation)
root.order.add_edge(prototype_creation, client_feedback)
root.order.add_edge(client_feedback, label_approval)
root.order.add_edge(label_approval, final_production)
root.order.add_edge(final_production, marketing_plan)
root.order.add_edge(marketing_plan, distribution_prep)
root.order.add_edge(distribution_prep, sales_launch)

print(root)