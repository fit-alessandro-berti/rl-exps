from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for empty labels
empty_transition = SilentTransition()

# Define the process structure
ingredient_sourcing_to_botanical_extraction = OperatorPOWL(operator=Operator.XOR, children=[ingredient_sourcing, empty_transition])
botanical_extraction_to_initial_blending = OperatorPOWL(operator=Operator.XOR, children=[botanical_extraction, empty_transition])
initial_blending_to_sensory_testing = OperatorPOWL(operator=Operator.XOR, children=[initial_blending, empty_transition])
sensory_testing_to_chemical_analysis = OperatorPOWL(operator=Operator.XOR, children=[sensory_testing, empty_transition])
chemical_analysis_to_recipe_refinement = OperatorPOWL(operator=Operator.XOR, children=[chemical_analysis, empty_transition])
recipe_refinement_to_stability_check = OperatorPOWL(operator=Operator.XOR, children=[recipe_refinement, empty_transition])
stability_check_to_client_sampling = OperatorPOWL(operator=Operator.XOR, children=[stability_check, empty_transition])
client_sampling_to_feedback_review = OperatorPOWL(operator=Operator.XOR, children=[client_sampling, empty_transition])
feedback_review_to_final_adjustment = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, empty_transition])
final_adjustment_to_custom_packaging = OperatorPOWL(operator=Operator.XOR, children=[final_adjustment, empty_transition])
custom_packaging_to_label_design = OperatorPOWL(operator=Operator.XOR, children=[custom_packaging, empty_transition])
label_design_to_hand_labeling = OperatorPOWL(operator=Operator.XOR, children=[label_design, empty_transition])
hand_labeling_to_regulatory_audit = OperatorPOWL(operator=Operator.XOR, children=[hand_labeling, empty_transition])
regulatory_audit_to_batch_documentation = OperatorPOWL(operator=Operator.XOR, children=[regulatory_audit, empty_transition])
batch_documentation_to_limited_release = OperatorPOWL(operator=Operator.XOR, children=[batch_documentation, empty_transition])
limited_release_to_market_launch = OperatorPOWL(operator=Operator.XOR, children=[limited_release, empty_transition])

# Define the partial order
root = StrictPartialOrder(nodes=[
    ingredient_sourcing_to_botanical_extraction,
    botanical_extraction_to_initial_blending,
    initial_blending_to_sensory_testing,
    sensory_testing_to_chemical_analysis,
    chemical_analysis_to_recipe_refinement,
    recipe_refinement_to_stability_check,
    stability_check_to_client_sampling,
    client_sampling_to_feedback_review,
    feedback_review_to_final_adjustment,
    final_adjustment_to_custom_packaging,
    custom_packaging_to_label_design,
    label_design_to_hand_labeling,
    hand_labeling_to_regulatory_audit,
    regulatory_audit_to_batch_documentation,
    batch_documentation_to_limited_release,
    limited_release_to_market_launch
])

# Add edges to the partial order
root.order.add_edge(ingredient_sourcing_to_botanical_extraction, botanical_extraction_to_initial_blending)
root.order.add_edge(botanical_extraction_to_initial_blending, initial_blending_to_sensory_testing)
root.order.add_edge(initial_blending_to_sensory_testing, sensory_testing_to_chemical_analysis)
root.order.add_edge(sensory_testing_to_chemical_analysis, chemical_analysis_to_recipe_refinement)
root.order.add_edge(chemical_analysis_to_recipe_refinement, recipe_refinement_to_stability_check)
root.order.add_edge(recipe_refinement_to_stability_check, stability_check_to_client_sampling)
root.order.add_edge(stability_check_to_client_sampling, client_sampling_to_feedback_review)
root.order.add_edge(client_sampling_to_feedback_review, feedback_review_to_final_adjustment)
root.order.add_edge(feedback_review_to_final_adjustment, final_adjustment_to_custom_packaging)
root.order.add_edge(final_adjustment_to_custom_packaging, custom_packaging_to_label_design)
root.order.add_edge(custom_packaging_to_label_design, label_design_to_hand_labeling)
root.order.add_edge(label_design_to_hand_labeling, hand_labeling_to_regulatory_audit)
root.order.add_edge(hand_labeling_to_regulatory_audit, regulatory_audit_to_batch_documentation)
root.order.add_edge(regulatory_audit_to_batch_documentation, batch_documentation_to_limited_release)
root.order.add_edge(batch_documentation_to_limited_release, limited_release_to_market_launch)

# Print the root of the POWL model
print(root)