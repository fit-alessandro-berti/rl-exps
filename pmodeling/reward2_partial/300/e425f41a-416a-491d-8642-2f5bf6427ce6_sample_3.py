import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Create the partial order
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

# Define the dependencies between activities
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

# Print the POWL model
print(root)