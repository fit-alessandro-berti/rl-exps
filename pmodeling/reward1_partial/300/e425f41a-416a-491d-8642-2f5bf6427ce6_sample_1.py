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
sensory_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensory_testing])
chemical_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[chemical_analysis])
recipe_refinement_loop = OperatorPOWL(operator=Operator.LOOP, children=[recipe_refinement])
stability_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[stability_check])
final_adjustment_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_adjustment])
client_sampling_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_sampling])
feedback_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_review])
custom_packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[custom_packaging])
label_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[label_design])
hand_labeling_loop = OperatorPOWL(operator=Operator.LOOP, children=[hand_labeling])
regulatory_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulatory_audit])
batch_documentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_documentation])
limited_release_loop = OperatorPOWL(operator=Operator.LOOP, children=[limited_release])
market_launch_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_launch])

root = StrictPartialOrder(nodes=[
    ingredient_sourcing,
    botanical_extraction,
    initial_blending,
    sensory_testing_loop,
    chemical_analysis_loop,
    recipe_refinement_loop,
    stability_check_loop,
    client_sampling_loop,
    feedback_review_loop,
    final_adjustment_loop,
    custom_packaging_loop,
    label_design_loop,
    hand_labeling_loop,
    regulatory_audit_loop,
    batch_documentation_loop,
    limited_release_loop,
    market_launch_loop
])

root.order.add_edge(ingredient_sourcing, botanical_extraction)
root.order.add_edge(botanical_extraction, initial_blending)
root.order.add_edge(initial_blending, sensory_testing_loop)
root.order.add_edge(sensory_testing_loop, chemical_analysis_loop)
root.order.add_edge(chemical_analysis_loop, recipe_refinement_loop)
root.order.add_edge(recipe_refinement_loop, stability_check_loop)
root.order.add_edge(stability_check_loop, client_sampling_loop)
root.order.add_edge(client_sampling_loop, feedback_review_loop)
root.order.add_edge(feedback_review_loop, final_adjustment_loop)
root.order.add_edge(final_adjustment_loop, custom_packaging_loop)
root.order.add_edge(custom_packaging_loop, label_design_loop)
root.order.add_edge(label_design_loop, hand_labeling_loop)
root.order.add_edge(hand_labeling_loop, regulatory_audit_loop)
root.order.add_edge(regulatory_audit_loop, batch_documentation_loop)
root.order.add_edge(batch_documentation_loop, limited_release_loop)
root.order.add_edge(limited_release_loop, market_launch_loop)

print(root)