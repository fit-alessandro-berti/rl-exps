from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ingredient_sourcing = Transition(label='Ingredient Sourcing')
botanical_extraction = Transition(label='Botanical Extraction')
initial_blending = Transition(label='Initial Blending')
sensory_testing = Transition(label='Sensory Testing')
chemical_analysis = Transition(label='Chemical Analysis')
recipe_refinement = Transition(label='Recipe Refinement')
stability_check = Transition(label='Stability Check')
client_sampling = Transition(label='Client Sampling')
feedback_review = Transition(label='Feedback Review')
final_adjustment = Transition(label='Final Adjustment')
custom_packaging = Transition(label='Custom Packaging')
label_design = Transition(label='Label Design')
hand_labeling = Transition(label='Hand Labeling')
regulatory_audit = Transition(label='Regulatory Audit')
batch_documentation = Transition(label='Batch Documentation')
limited_release = Transition(label='Limited Release')
market_launch = Transition(label='Market Launch')

# Define loops and choices
ingredient_loop = OperatorPOWL(operator=Operator.LOOP, children=[ingredient_sourcing, botanical_extraction])
initial_blend_loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_blending, sensory_testing, chemical_analysis])
recipe_refinement_loop = OperatorPOWL(operator=Operator.LOOP, children=[recipe_refinement, stability_check])
client_sampling_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_sampling, feedback_review, final_adjustment])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[custom_packaging, label_design, hand_labeling, regulatory_audit, batch_documentation])

# Define partial order
root = StrictPartialOrder(nodes=[ingredient_loop, initial_blend_loop, recipe_refinement_loop, client_sampling_loop, packaging_loop, limited_release, market_launch])
root.order.add_edge(ingredient_loop, initial_blend_loop)
root.order.add_edge(initial_blend_loop, recipe_refinement_loop)
root.order.add_edge(recipe_refinement_loop, client_sampling_loop)
root.order.add_edge(client_sampling_loop, packaging_loop)
root.order.add_edge(packaging_loop, limited_release)
root.order.add_edge(limited_release, market_launch)