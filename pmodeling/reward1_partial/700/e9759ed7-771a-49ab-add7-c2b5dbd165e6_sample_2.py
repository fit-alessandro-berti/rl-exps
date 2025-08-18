import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define control flow operators
ingredient_sourcing_to_sample_testing = OperatorPOWL(operator=Operator.XOR, children=[ingredient_sourcing, sample_testing])
sample_testing_to_oil_extraction = OperatorPOWL(operator=Operator.XOR, children=[sample_testing, oil_extraction])
oil_extraction_to_blend_formulation = OperatorPOWL(operator=Operator.XOR, children=[oil_extraction, blend_formulation])
blend_formulation_to_quality_control = OperatorPOWL(operator=Operator.XOR, children=[blend_formulation, quality_control])
quality_control_to_aging_process = OperatorPOWL(operator=Operator.XOR, children=[quality_control, aging_process])
aging_process_to_allergen_check = OperatorPOWL(operator=Operator.XOR, children=[aging_process, allergen_check])
allergen_check_to_market_research = OperatorPOWL(operator=Operator.XOR, children=[allergen_check, market_research])
market_research_to_bottle_design = OperatorPOWL(operator=Operator.XOR, children=[market_research, bottle_design])
bottle_design_to_label_approval = OperatorPOWL(operator=Operator.XOR, children=[bottle_design, label_approval])
label_approval_to_packaging_setup = OperatorPOWL(operator=Operator.XOR, children=[label_approval, packaging_setup])
packaging_setup_to_batch_mixing = OperatorPOWL(operator=Operator.XOR, children=[packaging_setup, batch_mixing])
batch_mixing_to_scent_profiling = OperatorPOWL(operator=Operator.XOR, children=[batch_mixing, scent_profiling])
scent_profiling_to_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[scent_profiling, client_feedback])
client_feedback_to_release_scheduling = OperatorPOWL(operator=Operator.XOR, children=[client_feedback, release_scheduling])
release_scheduling_to_regulatory_review = OperatorPOWL(operator=Operator.XOR, children=[release_scheduling, regulatory_review])
regulatory_review_to_sales_training = OperatorPOWL(operator=Operator.XOR, children=[regulatory_review, sales_training])

# Define the root POWL model
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

# Define the dependencies between activities
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