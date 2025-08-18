from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the POWL model
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

# Define the partial order nodes
sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[ingredient_sourcing, quality_testing, scent_blending, micro_batch, sensory_panel, formula_adjust, safety_review, sustainability_check])
prototype_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, prototype_creation, client_feedback, label_approval, final_production])
marketing_loop = OperatorPOWL(operator=Operator.LOOP, children=[marketing_plan, distribution_prep, sales_launch])

# Define the partial order
root = StrictPartialOrder(nodes=[sourcing_loop, prototype_loop, marketing_loop])
root.order.add_edge(sourcing_loop, prototype_loop)
root.order.add_edge(prototype_loop, marketing_loop)

print(root)