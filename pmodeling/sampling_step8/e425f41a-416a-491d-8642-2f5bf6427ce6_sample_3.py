import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

ingredient_sourcing_to_botanical_extraction = OperatorPOWL(operator=Operator.XOR, children=[ingredient_sourcing, skip])
botanical_extraction_to_initial_blending = OperatorPOWL(operator=Operator.XOR, children=[botanical_extraction, skip])
initial_blending_to_sensory_testing = OperatorPOWL(operator=Operator.XOR, children=[initial_blending, skip])
sensory_testing_to_chemical_analysis = OperatorPOWL(operator=Operator.XOR, children=[sensory_testing, skip])
chemical_analysis_to_recipe_refinement = OperatorPOWL(operator=Operator.XOR, children=[chemical_analysis, skip])
recipe_refinement_to_stability_check = OperatorPOWL(operator=Operator.XOR, children=[recipe_refinement, skip])
stability_check_to_client_sampling = OperatorPOWL(operator=Operator.XOR, children=[stability_check, skip])
client_sampling_to_feedback_review = OperatorPOWL(operator=Operator.XOR, children=[client_sampling, skip])
feedback_review_to_final_adjustment = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, skip])
final_adjustment_to_custom_packaging = OperatorPOWL(operator=Operator.XOR, children=[final_adjustment, skip])
custom_packaging_to_label_design = OperatorPOWL(operator=Operator.XOR, children=[custom_packaging, skip])
label_design_to_hand_labeling = OperatorPOWL(operator=Operator.XOR, children=[label_design, skip])
hand_labeling_to_regulatory_audit = OperatorPOWL(operator=Operator.XOR, children=[hand_labeling, skip])
regulatory_audit_to_batch_documentation = OperatorPOWL(operator=Operator.XOR, children=[regulatory_audit, skip])
batch_documentation_to_limited_release = OperatorPOWL(operator=Operator.XOR, children=[batch_documentation, skip])
limited_release_to_market_launch = OperatorPOWL(operator=Operator.XOR, children=[limited_release, skip])

root = StrictPartialOrder(nodes=[
    ingredient_sourcing,
    botanical_extraction,
    initial_blending,
    sensory_testing,
    chemical_analysis,
    recipe_refinement,
    stability_check,
    client_sampling,
    feedback_review,
    final_adjustment,
    custom_packaging,
    label_design,
    hand_labeling,
    regulatory_audit,
    batch_documentation,
    limited_release,
    market_launch
])

root.order.add_edge(ingredient_sourcing, botanical_extraction)
root.order.add_edge(botanical_extraction, initial_blending)
root.order.add_edge(initial_blending, sensory_testing)
root.order.add_edge(sensory_testing, chemical_analysis)
root.order.add_edge(chemical_analysis, recipe_refinement)
root.order.add_edge(recipe_refinement, stability_check)
root.order.add_edge(stability_check, client_sampling)
root.order.add_edge(client_sampling, feedback_review)
root.order.add_edge(feedback_review, final_adjustment)
root.order.add_edge(final_adjustment, custom_packaging)
root.order.add_edge(custom_packaging, label_design)
root.order.add_edge(label_design, hand_labeling)
root.order.add_edge(hand_labeling, regulatory_audit)
root.order.add_edge(regulatory_audit, batch_documentation)
root.order.add_edge(batch_documentation, limited_release)
root.order.add_edge(limited_release, market_launch)

print(root)