from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[ingredient_sourcing, sample_testing, oil_extraction, blend_formulation,
           quality_control, aging_process, allergen_check, market_research,
           bottle_design, label_approval, packaging_setup, batch_mixing,
           scent_profiling, client_feedback, release_scheduling, regulatory_review,
           sales_training],
    order={ingredient_sourcing: sample_testing,
           sample_testing: oil_extraction,
           oil_extraction: blend_formulation,
           blend_formulation: quality_control,
           quality_control: aging_process,
           aging_process: allergen_check,
           allergen_check: market_research,
           market_research: bottle_design,
           bottle_design: label_approval,
           label_approval: packaging_setup,
           packaging_setup: batch_mixing,
           batch_mixing: scent_profiling,
           scent_profiling: client_feedback,
           client_feedback: release_scheduling,
           release_scheduling: regulatory_review,
           regulatory_review: sales_training}
)

print(root)