from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
ingredient_sourcing = Transition(label='Ingredient Sourcing')
sample_testing = Transition(label='Sample Testing')
oil_extraction = Transition(label='Oil Extraction')
blend_formulation = Transition(label='Blend Formulation')
quality_control = Transition(label='Quality Control')
aging_process = Transition(label='Aging Process')
allergen_check = Transition(label='Allergen Check')
market_research = Transition(label='Market Research')
bottle_design = Transition(label='Bottle Design')
label_approval = Transition(label='Label Approval')
packaging_setup = Transition(label='Packaging Setup')
batch_mixing = Transition(label='Batch Mixing')
scent_profiling = Transition(label='Scent Profiling')
client_feedback = Transition(label='Client Feedback')
release_scheduling = Transition(label='Release Scheduling')
regulatory_review = Transition(label='Regulatory Review')
sales_training = Transition(label='Sales Training')

# Define the partial order
root = StrictPartialOrder(nodes=[
    ingredient_sourcing,
    sample_testing,
    oil_extraction,
    blend_formulation,
    quality_control,
    aging_process,
    allergen_check,
    market_research,
    bottle_design,
    label_approval,
    packaging_setup,
    batch_mixing,
    scent_profiling,
    client_feedback,
    release_scheduling,
    regulatory_review,
    sales_training
])

# Add dependencies between activities if any (not specified in the problem statement)
# For example, if 'ingredient_sourcing' is a prerequisite for 'sample_testing':
# root.order.add_edge(ingredient_sourcing, sample_testing)

print(root)