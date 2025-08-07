import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the partial order
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

# Add dependencies if necessary
# For example, if ingredient sourcing must occur before quality testing:
root.order.add_edge(ingredient_sourcing, quality_testing)

# Add more dependencies as needed based on the actual process flow
# Example:
# root.order.add_edge(scent_blending, formula_adjust)

# Print or return the root model
print(root)