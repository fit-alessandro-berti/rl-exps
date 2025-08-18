import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the workflow
ingredient_sourcing_next = sample_testing
sample_testing_next = oil_extraction
oil_extraction_next = blend_formulation
blend_formulation_next = quality_control
quality_control_next = aging_process
aging_process_next = allergen_check
allergen_check_next = market_research
market_research_next = bottle_design
bottle_design_next = label_approval
label_approval_next = packaging_setup
packaging_setup_next = batch_mixing
batch_mixing_next = scent_profiling
scent_profiling_next = client_feedback
client_feedback_next = release_scheduling
release_scheduling_next = regulatory_review
regulatory_review_next = sales_training

# Define the POWL model
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

# Define the order
root.order.add_edge(ingredient_sourcing, sample_testing)
root.order.add_edge(sample_testing, oil_extraction)
root.order.add_edge(oil_extraction, blend_formulation)
root.order.add_edge(blend_formulation, quality_control)
root.order.add_edge(quality_control, aging_process)
root.order.add_edge(aging_process, allergen_check)
root.order.add_edge(allergen_check, market_research)
root.order.add_edge(market_research, bottle_design)
root.order.add_edge(bottle_design, label_approval)
root.order.add_edge(label_approval, packaging_setup)
root.order.add_edge(packaging_setup, batch_mixing)
root.order.add_edge(batch_mixing, scent_profiling)
root.order.add_edge(scent_profiling, client_feedback)
root.order.add_edge(client_feedback, release_scheduling)
root.order.add_edge(release_scheduling, regulatory_review)
root.order.add_edge(regulatory_review, sales_training)

# Print the POWL model
print(root)