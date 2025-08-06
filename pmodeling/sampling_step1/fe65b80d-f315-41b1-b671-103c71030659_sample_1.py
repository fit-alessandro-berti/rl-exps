import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the loop nodes
ingredient_loop = OperatorPOWL(operator=Operator.LOOP, children=[ingredient_sourcing, quality_testing, scent_blending])
sensory_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensory_panel, formula_adjust])
safety_loop = OperatorPOWL(operator=Operator.LOOP, children=[safety_review, sustainability_check])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, prototype_creation, client_feedback, label_approval])
production_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_production, marketing_plan, distribution_prep, sales_launch])

# Define the partial order
root = StrictPartialOrder(nodes=[ingredient_loop, sensory_loop, safety_loop, packaging_loop, production_loop])
root.order.add_edge(ingredient_loop, sensory_loop)
root.order.add_edge(sensory_loop, safety_loop)
root.order.add_edge(safety_loop, packaging_loop)
root.order.add_edge(packaging_loop, production_loop)

# Return the root of the POWL model
print(root)