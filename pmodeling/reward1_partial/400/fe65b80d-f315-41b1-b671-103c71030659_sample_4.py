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

# Define the partial order model
root = StrictPartialOrder()

# Add transitions to the root
root.nodes.add(ingredient_sourcing)
root.nodes.add(quality_testing)
root.nodes.add(scent_blending)
root.nodes.add(micro_batch)
root.nodes.add(sensory_panel)
root.nodes.add(formula_adjust)
root.nodes.add(safety_review)
root.nodes.add(sustainability_check)
root.nodes.add(packaging_design)
root.nodes.add(prototype_creation)
root.nodes.add(client_feedback)
root.nodes.add(label_approval)
root.nodes.add(final_production)
root.nodes.add(marketing_plan)
root.nodes.add(distribution_prep)
root.nodes.add(sales_launch)

# Define dependencies
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

# Print the root model
print(root)