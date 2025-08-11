import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the loop and choice nodes
ingredient_sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[ingredient_sourcing, botanical_extraction])
initial_blending_loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_blending, sensory_testing, chemical_analysis, recipe_refinement, stability_check])
client_sampling_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_sampling, feedback_review, final_adjustment, custom_packaging])
label_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[label_design, hand_labeling, regulatory_audit, batch_documentation])
limited_release_loop = OperatorPOWL(operator=Operator.LOOP, children=[limited_release, market_launch])

# Define the exclusive choice nodes
ingredient_sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[ingredient_sourcing_loop, client_sampling_loop])
label_design_choice = OperatorPOWL(operator=Operator.XOR, children=[label_design_loop, limited_release_loop])

# Define the root node
root = StrictPartialOrder(nodes=[ingredient_sourcing_choice, label_design_choice])

# Define the order of the nodes
root.order.add_edge(ingredient_sourcing_choice, label_design_choice)

# Print the root node
print(root)