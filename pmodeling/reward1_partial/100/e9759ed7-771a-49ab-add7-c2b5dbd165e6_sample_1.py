from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the perfume creation process
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
ingredient_sourcing_node = IngredientSourcing()
sample_testing_node = SampleTesting()
oil_extraction_node = OilExtraction()
blend_formulation_node = BlendFormulation()
quality_control_node = QualityControl()
aging_process_node = AgingProcess()
allergen_check_node = AllergenCheck()
market_research_node = MarketResearch()
bottle_design_node = BottleDesign()
label_approval_node = LabelApproval()
packaging_setup_node = PackagingSetup()
batch_mixing_node = BatchMixing()
scent_profiling_node = ScentProfiling()
client_feedback_node = ClientFeedback()
release_scheduling_node = ReleaseScheduling()
regulatory_review_node = RegulatoryReview()
sales_training_node = SalesTraining()

# Define the partial order graph
root = StrictPartialOrder(
    nodes=[
        ingredient_sourcing_node,
        sample_testing_node,
        oil_extraction_node,
        blend_formulation_node,
        quality_control_node,
        aging_process_node,
        allergen_check_node,
        market_research_node,
        bottle_design_node,
        label_approval_node,
        packaging_setup_node,
        batch_mixing_node,
        scent_profiling_node,
        client_feedback_node,
        release_scheduling_node,
        regulatory_review_node,
        sales_training_node
    ]
)

# Define the dependencies
root.order.add_edge(ingredient_sourcing_node, sample_testing_node)
root.order.add_edge(sample_testing_node, oil_extraction_node)
root.order.add_edge(oil_extraction_node, blend_formulation_node)
root.order.add_edge(blend_formulation_node, quality_control_node)
root.order.add_edge(quality_control_node, aging_process_node)
root.order.add_edge(aging_process_node, allergen_check_node)
root.order.add_edge(allergen_check_node, market_research_node)
root.order.add_edge(market_research_node, bottle_design_node)
root.order.add_edge(bottle_design_node, label_approval_node)
root.order.add_edge(label_approval_node, packaging_setup_node)
root.order.add_edge(packaging_setup_node, batch_mixing_node)
root.order.add_edge(batch_mixing_node, scent_profiling_node)
root.order.add_edge(scent_profiling_node, client_feedback_node)
root.order.add_edge(client_feedback_node, release_scheduling_node)
root.order.add_edge(release_scheduling_node, regulatory_review_node)
root.order.add_edge(regulatory_review_node, sales_training_node)