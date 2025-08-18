from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
ingredient_sourcing_next_sample_testing = OperatorPOWL(operator=Operator.XOR, children=[ingredient_sourcing, sample_testing])
sample_testing_next_oil_extraction = OperatorPOWL(operator=Operator.XOR, children=[ingredient_sourcing, sample_testing])
oil_extraction_next_blend_formulation = OperatorPOWL(operator=Operator.XOR, children=[oil_extraction, blend_formulation])
blend_formulation_next_quality_control = OperatorPOWL(operator=Operator.XOR, children=[oil_extraction, blend_formulation])
quality_control_next_aging_process = OperatorPOWL(operator=Operator.XOR, children=[quality_control, aging_process])
aging_process_next_allergen_check = OperatorPOWL(operator=Operator.XOR, children=[aging_process, allergen_check])
allergen_check_next_market_research = OperatorPOWL(operator=Operator.XOR, children=[allergen_check, market_research])
market_research_next_bottle_design = OperatorPOWL(operator=Operator.XOR, children=[market_research, bottle_design])
bottle_design_next_label_approval = OperatorPOWL(operator=Operator.XOR, children=[bottle_design, label_approval])
label_approval_next_packaging_setup = OperatorPOWL(operator=Operator.XOR, children=[label_approval, packaging_setup])
packaging_setup_next_batch_mixing = OperatorPOWL(operator=Operator.XOR, children=[packaging_setup, batch_mixing])
batch_mixing_next_scent_profiling = OperatorPOWL(operator=Operator.XOR, children=[batch_mixing, scent_profiling])
scent_profiling_next_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[scent_profiling, client_feedback])
client_feedback_next_release_scheduling = OperatorPOWL(operator=Operator.XOR, children=[client_feedback, release_scheduling])
release_scheduling_next_regulatory_review = OperatorPOWL(operator=Operator.XOR, children=[release_scheduling, regulatory_review])
regulatory_review_next_sales_training = OperatorPOWL(operator=Operator.XOR, children=[regulatory_review, sales_training])

root = StrictPartialOrder(nodes=[
    ingredient_sourcing_next_sample_testing,
    sample_testing_next_oil_extraction,
    oil_extraction_next_blend_formulation,
    blend_formulation_next_quality_control,
    quality_control_next_aging_process,
    aging_process_next_allergen_check,
    allergen_check_next_market_research,
    market_research_next_bottle_design,
    bottle_design_next_label_approval,
    label_approval_next_packaging_setup,
    packaging_setup_next_batch_mixing,
    batch_mixing_next_scent_profiling,
    scent_profiling_next_client_feedback,
    client_feedback_next_release_scheduling,
    release_scheduling_next_regulatory_review,
    regulatory_review_next_sales_training
])

# Add dependencies
root.order.add_edge(ingredient_sourcing_next_sample_testing, sample_testing_next_oil_extraction)
root.order.add_edge(sample_testing_next_oil_extraction, oil_extraction_next_blend_formulation)
root.order.add_edge(oil_extraction_next_blend_formulation, blend_formulation_next_quality_control)
root.order.add_edge(blend_formulation_next_quality_control, quality_control_next_aging_process)
root.order.add_edge(quality_control_next_aging_process, aging_process_next_allergen_check)
root.order.add_edge(aging_process_next_allergen_check, allergen_check_next_market_research)
root.order.add_edge(allergen_check_next_market_research, market_research_next_bottle_design)
root.order.add_edge(market_research_next_bottle_design, bottle_design_next_label_approval)
root.order.add_edge(bottle_design_next_label_approval, label_approval_next_packaging_setup)
root.order.add_edge(label_approval_next_packaging_setup, packaging_setup_next_batch_mixing)
root.order.add_edge(packaging_setup_next_batch_mixing, batch_mixing_next_scent_profiling)
root.order.add_edge(batch_mixing_next_scent_profiling, scent_profiling_next_client_feedback)
root.order.add_edge(scent_profiling_next_client_feedback, client_feedback_next_release_scheduling)
root.order.add_edge(client_feedback_next_release_scheduling, release_scheduling_next_regulatory_review)
root.order.add_edge(release_scheduling_next_regulatory_review, regulatory_review_next_sales_training)

print(root)