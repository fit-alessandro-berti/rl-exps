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

# Define silent transitions
skip = SilentTransition()

# Define loop and exclusive choice operators
ingredient_loop = OperatorPOWL(operator=Operator.LOOP, children=[ingredient_sourcing, quality_testing])
scent_loop = OperatorPOWL(operator=Operator.LOOP, children=[scent_blending, micro_batch, sensory_panel])
formula_loop = OperatorPOWL(operator=Operator.LOOP, children=[formula_adjust, safety_review, sustainability_check])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, prototype_creation])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_feedback, label_approval, final_production])
marketing_loop = OperatorPOWL(operator=Operator.LOOP, children=[marketing_plan, distribution_prep, sales_launch])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    ingredient_loop,
    scent_loop,
    formula_loop,
    packaging_loop,
    feedback_loop,
    marketing_loop
])

# Define dependencies
root.order.add_edge(ingredient_loop, scent_loop)
root.order.add_edge(scent_loop, formula_loop)
root.order.add_edge(formula_loop, packaging_loop)
root.order.add_edge(packaging_loop, feedback_loop)
root.order.add_edge(feedback_loop, marketing_loop)

print(root)