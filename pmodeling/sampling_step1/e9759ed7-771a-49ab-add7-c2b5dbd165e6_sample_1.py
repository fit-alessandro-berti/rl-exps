import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the process
sourcing = Transition(label='Ingredient Sourcing')
testing = Transition(label='Sample Testing')
extraction = Transition(label='Oil Extraction')
formulation = Transition(label='Blend Formulation')
quality_control = Transition(label='Quality Control')
aging = Transition(label='Aging Process')
allergen_check = Transition(label='Allergen Check')
market_research = Transition(label='Market Research')
bottle_design = Transition(label='Bottle Design')
label_approval = Transition(label='Label Approval')
packaging_setup = Transition(label='Packaging Setup')
batch_mixing = Transition(label='Batch Mixing')
scent_profiling = Transition(label='Scent Profiling')
feedback = Transition(label='Client Feedback')
release_scheduling = Transition(label='Release Scheduling')
regulatory_review = Transition(label='Regulatory Review')
sales_training = Transition(label='Sales Training')

# Define the partial order
root = StrictPartialOrder(nodes=[
    sourcing,
    testing,
    extraction,
    formulation,
    quality_control,
    aging,
    allergen_check,
    market_research,
    bottle_design,
    label_approval,
    packaging_setup,
    batch_mixing,
    scent_profiling,
    feedback,
    release_scheduling,
    regulatory_review,
    sales_training
])

# Add the dependencies between the nodes
root.order.add_edge(sourcing, testing)
root.order.add_edge(testing, extraction)
root.order.add_edge(extraction, formulation)
root.order.add_edge(formulation, quality_control)
root.order.add_edge(quality_control, aging)
root.order.add_edge(aging, allergen_check)
root.order.add_edge(allergen_check, market_research)
root.order.add_edge(market_research, bottle_design)
root.order.add_edge(bottle_design, label_approval)
root.order.add_edge(label_approval, packaging_setup)
root.order.add_edge(packaging_setup, batch_mixing)
root.order.add_edge(batch_mixing, scent_profiling)
root.order.add_edge(scent_profiling, feedback)
root.order.add_edge(feedback, release_scheduling)
root.order.add_edge(release_scheduling, regulatory_review)
root.order.add_edge(regulatory_review, sales_training)

# Print the root
print(root)