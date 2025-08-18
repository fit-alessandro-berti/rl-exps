import pm4py
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

# Define transitions
skip = SilentTransition()

# Define process tree
sensory_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensory_testing, chemical_analysis, stability_check])
refinement_loop = OperatorPOWL(operator=Operator.LOOP, children=[recipe_refinement, feedback_review, final_adjustment])
sampling_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_sampling, regulatory_audit, batch_documentation])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[custom_packaging, label_design, hand_labeling])
release_loop = OperatorPOWL(operator=Operator.LOOP, children=[limited_release, market_launch])

# Define root
root = StrictPartialOrder(nodes=[ingredient_sourcing, botanical_extraction, initial_blending, sensory_testing_loop, refinement_loop, sampling_loop, packaging_loop, release_loop])
root.order.add_edge(ingredient_sourcing, botanical_extraction)
root.order.add_edge(botanical_extraction, initial_blending)
root.order.add_edge(initial_blending, sensory_testing_loop)
root.order.add_edge(sensory_testing_loop, refinement_loop)
root.order.add_edge(refinement_loop, sampling_loop)
root.order.add_edge(sampling_loop, packaging_loop)
root.order.add_edge(packaging_loop, release_loop)