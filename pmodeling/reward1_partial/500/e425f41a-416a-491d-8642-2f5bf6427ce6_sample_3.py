import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
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
    ],
    order={
        ingredient_sourcing: [botanical_extraction],
        botanical_extraction: [initial_blending],
        initial_blending: [sensory_testing],
        sensory_testing: [chemical_analysis],
        chemical_analysis: [recipe_refinement],
        recipe_refinement: [stability_check],
        stability_check: [client_sampling],
        client_sampling: [feedback_review],
        feedback_review: [final_adjustment],
        final_adjustment: [custom_packaging],
        custom_packaging: [label_design],
        label_design: [hand_labeling],
        hand_labeling: [regulatory_audit],
        regulatory_audit: [batch_documentation],
        batch_documentation: [limited_release],
        limited_release: [market_launch]
    }
)

print(root)