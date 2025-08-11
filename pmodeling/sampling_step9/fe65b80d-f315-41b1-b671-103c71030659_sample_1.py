import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop nodes
sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[ingredient_sourcing, quality_testing])
scent_loop = OperatorPOWL(operator=Operator.LOOP, children=[scent_blending, micro_batch, sensory_panel])
adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[formula_adjust, safety_review, sustainability_check])
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, prototype_creation])

# Define the exclusive choice nodes
sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[sourcing_loop, skip])
scent_choice = OperatorPOWL(operator=Operator.XOR, children=[scent_loop, skip])
adjust_choice = OperatorPOWL(operator=Operator.XOR, children=[adjust_loop, skip])
design_choice = OperatorPOWL(operator=Operator.XOR, children=[design_loop, skip])

# Define the root node
root = StrictPartialOrder(nodes=[sourcing_choice, scent_choice, adjust_choice, design_choice, client_feedback, label_approval, final_production, marketing_plan, distribution_prep, sales_launch])
root.order.add_edge(sourcing_choice, scent_choice)
root.order.add_edge(scent_choice, adjust_choice)
root.order.add_edge(adjust_choice, design_choice)
root.order.add_edge(design_choice, client_feedback)
root.order.add_edge(client_feedback, label_approval)
root.order.add_edge(label_approval, final_production)
root.order.add_edge(final_production, marketing_plan)
root.order.add_edge(marketing_plan, distribution_prep)
root.order.add_edge(distribution_prep, sales_launch)