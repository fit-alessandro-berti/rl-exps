import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        ingredient_sourcing,
        quality_testing,
        scent_blending,
        micro_batch,
        sensory_panel,
        formula_adjust,
        safety_review,
        sustainability_check,
        packaging_design,
        prototype_creation,
        client_feedback,
        label_approval,
        final_production,
        marketing_plan,
        distribution_prep,
        sales_launch
    ],
    order=[
        (ingredient_sourcing, quality_testing),
        (ingredient_sourcing, scent_blending),
        (quality_testing, micro_batch),
        (micro_batch, sensory_panel),
        (sensory_panel, formula_adjust),
        (formula_adjust, safety_review),
        (safety_review, sustainability_check),
        (sustainability_check, packaging_design),
        (packaging_design, prototype_creation),
        (prototype_creation, client_feedback),
        (client_feedback, label_approval),
        (label_approval, final_production),
        (final_production, marketing_plan),
        (marketing_plan, distribution_prep),
        (distribution_prep, sales_launch)
    ]
)