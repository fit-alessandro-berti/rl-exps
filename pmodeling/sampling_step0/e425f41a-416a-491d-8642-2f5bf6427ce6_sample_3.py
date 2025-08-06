from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
ingredient_sourcing = Transition(label='Ingredient Sourcing')
botanical_extraction = Transition(label='Botanical Extraction')
initial_blending = Transition(label='Initial Blending')
sensory_testing = Transition(label='Sensory Testing')
chemical_analysis = Transition(label='Chemical Analysis')
recipe_refinement = Transition(label='Recipe Refinement')
stability_check = Transition(label='Stability Check')
client_sampling = Transition(label='Client Sampling')
feedback_review = Transition(label='Feedback Review')
final_adjustment = Transition(label='Final Adjustment')
custom_packaging = Transition(label='Custom Packaging')
label_design = Transition(label='Label Design')
hand_labeling = Transition(label='Hand Labeling')
regulatory_audit = Transition(label='Regulatory Audit')
batch_documentation = Transition(label='Batch Documentation')
limited_release = Transition(label='Limited Release')
market_launch = Transition(label='Market Launch')

# Define the control flow
ingredient_sourcing_node = OperatorPOWL(operator=Operator.ANY, children=[ingredient_sourcing])
botanical_extraction_node = OperatorPOWL(operator=Operator.ANY, children=[botanical_extraction])
initial_blending_node = OperatorPOWL(operator=Operator.ANY, children=[initial_blending])
sensory_testing_node = OperatorPOWL(operator=Operator.ANY, children=[sensory_testing])
chemical_analysis_node = OperatorPOWL(operator=Operator.ANY, children=[chemical_analysis])
recipe_refinement_node = OperatorPOWL(operator=Operator.ANY, children=[recipe_refinement])
stability_check_node = OperatorPOWL(operator=Operator.ANY, children=[stability_check])
client_sampling_node = OperatorPOWL(operator=Operator.ANY, children=[client_sampling])
feedback_review_node = OperatorPOWL(operator=Operator.ANY, children=[feedback_review])
final_adjustment_node = OperatorPOWL(operator=Operator.ANY, children=[final_adjustment])
custom_packaging_node = OperatorPOWL(operator=Operator.ANY, children=[custom_packaging])
label_design_node = OperatorPOWL(operator=Operator.ANY, children=[label_design])
hand_labeling_node = OperatorPOWL(operator=Operator.ANY, children=[hand_labeling])
regulatory_audit_node = OperatorPOWL(operator=Operator.ANY, children=[regulatory_audit])
batch_documentation_node = OperatorPOWL(operator=Operator.ANY, children=[batch_documentation])
limited_release_node = OperatorPOWL(operator=Operator.ANY, children=[limited_release])
market_launch_node = OperatorPOWL(operator=Operator.ANY, children=[market_launch])

# Define the loops
sensory_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensory_testing_node, feedback_review_node, final_adjustment_node])
chemical_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[chemical_analysis_node, stability_check_node])

# Define the partial order
root = StrictPartialOrder(nodes=[
    ingredient_sourcing_node,
    botanical_extraction_node,
    initial_blending_node,
    sensory_testing_loop,
    chemical_analysis_loop,
    custom_packaging_node,
    label_design_node,
    hand_labeling_node,
    regulatory_audit_node,
    batch_documentation_node,
    limited_release_node,
    market_launch_node
])

# Add dependencies
root.order.add_edge(ingredient_sourcing_node, botanical_extraction_node)
root.order.add_edge(botanical_extraction_node, initial_blending_node)
root.order.add_edge(initial_blending_node, sensory_testing_loop)
root.order.add_edge(sensory_testing_loop, chemical_analysis_loop)
root.order.add_edge(chemical_analysis_loop, custom_packaging_node)
root.order.add_edge(custom_packaging_node, label_design_node)
root.order.add_edge(label_design_node, hand_labeling_node)
root.order.add_edge(hand_labeling_node, regulatory_audit_node)
root.order.add_edge(regulatory_audit_node, batch_documentation_node)
root.order.add_edge(batch_documentation_node, limited_release_node)
root.order.add_edge(limited_release_node, market_launch_node)

print(root)