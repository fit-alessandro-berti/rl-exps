import pm4py

# Define the transitions for each activity
sourcing = pm4py.objects.powl.obj.Transition(label='Ingredient Sourcing')
testing = pm4py.objects.powl.obj.Transition(label='Sample Testing')
extraction = pm4py.objects.powl.obj.Transition(label='Oil Extraction')
blending = pm4py.objects.powl.obj.Transition(label='Blend Formulation')
quality_control = pm4py.objects.powl.obj.Transition(label='Quality Control')
aging = pm4py.objects.powl.obj.Transition(label='Aging Process')
allergen_check = pm4py.objects.powl.obj.Transition(label='Allergen Check')
market_research = pm4py.objects.powl.obj.Transition(label='Market Research')
bottle_design = pm4py.objects.powl.obj.Transition(label='Bottle Design')
label_approval = pm4py.objects.powl.obj.Transition(label='Label Approval')
packaging_setup = pm4py.objects.powl.obj.Transition(label='Packaging Setup')
batch_mixing = pm4py.objects.powl.obj.Transition(label='Batch Mixing')
scent_profiling = pm4py.objects.powl.obj.Transition(label='Scent Profiling')
client_feedback = pm4py.objects.powl.obj.Transition(label='Client Feedback')
release_scheduling = pm4py.objects.powl.obj.Transition(label='Release Scheduling')
regulatory_review = pm4py.objects.powl.obj.Transition(label='Regulatory Review')
sales_training = pm4py.objects.powl.obj.Transition(label='Sales Training')

# Define the partial order structure
root = pm4py.objects.powl.obj.StrictPartialOrder(nodes=[
    sourcing,
    testing,
    extraction,
    blending,
    quality_control,
    aging,
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
root.order.add_edge(sourcing, testing)
root.order.add_edge(testing, extraction)
root.order.add_edge(extraction, blending)
root.order.add_edge(blending, quality_control)
root.order.add_edge(quality_control, aging)
root.order.add_edge(aging, allergen_check)
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

print(root)