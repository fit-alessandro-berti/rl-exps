import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define individual transitions (activities)
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

# Define silent transitions
skip = SilentTransition()

# Define the workflow
# Step 1: Ingredient Sourcing
# Step 2: Quality Testing
# Step 3: Scent Blending
# Step 4: Micro Batch
# Step 5: Sensory Panel
# Step 6: Formula Adjust
# Step 7: Safety Review
# Step 8: Sustainability Check
# Step 9: Packaging Design
# Step 10: Prototype Creation
# Step 11: Client Feedback
# Step 12: Label Approval
# Step 13: Final Production
# Step 14: Marketing Plan
# Step 15: Distribution Prep
# Step 16: Sales Launch

# Define the loop for the main workflow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[
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
    final_production
])

# Define the exclusive choice for the workflow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[
    marketing_plan,
    distribution_prep,
    sales_launch
])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop1, xor1])
root.order.add_edge(loop1, xor1)

# Print the root POWL model
print(root)