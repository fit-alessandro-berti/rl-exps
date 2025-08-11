import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice for the market research and bottle design
market_research_bottle_design = OperatorPOWL(operator=Operator.XOR, children=[market_research, bottle_design])

# Define the loop for the quality control and allergen check
quality_control_allergen_check = OperatorPOWL(operator=Operator.LOOP, children=[quality_control, allergen_check])

# Define the exclusive choice for the sales training and regulatory review
sales_training_regulatory_review = OperatorPOWL(operator=Operator.XOR, children=[sales_training, regulatory_review])

# Define the loop for the scent profiling and client feedback
scent_profiling_client_feedback = OperatorPOWL(operator=Operator.LOOP, children=[scent_profiling, client_feedback])

# Define the exclusive choice for the batch mixing and release scheduling
batch_mixing_release_scheduling = OperatorPOWL(operator=Operator.XOR, children=[batch_mixing, release_scheduling])

# Define the root POWL model
root = StrictPartialOrder(nodes=[ingredient_sourcing, sample_testing, oil_extraction, blend_formulation, quality_control_allergen_check, market_research_bottle_design, sales_training_regulatory_review, scent_profiling_client_feedback, batch_mixing_release_scheduling])
root.order.add_edge(ingredient_sourcing, sample_testing)
root.order.add_edge(sample_testing, oil_extraction)
root.order.add_edge(oil_extraction, blend_formulation)
root.order.add_edge(blend_formulation, quality_control_allergen_check)
root.order.add_edge(quality_control_allergen_check, market_research_bottle_design)
root.order.add_edge(market_research_bottle_design, sales_training_regulatory_review)
root.order.add_edge(sales_training_regulatory_review, scent_profiling_client_feedback)
root.order.add_edge(scent_profiling_client_feedback, batch_mixing_release_scheduling)