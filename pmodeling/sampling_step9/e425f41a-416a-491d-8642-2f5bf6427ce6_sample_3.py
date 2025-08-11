import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
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

# Define silent transitions (if any)
skip = SilentTransition()

# Define the loop node (Stability Check)
loop_stability = OperatorPOWL(operator=Operator.LOOP, children=[stability_check])

# Define the choice node (Client Sampling)
choice_sampling = OperatorPOWL(operator=Operator.XOR, children=[client_sampling, skip])

# Define the choice node (Feedback Review)
choice_review = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, skip])

# Define the choice node (Final Adjustment)
choice_adjustment = OperatorPOWL(operator=Operator.XOR, children=[final_adjustment, skip])

# Define the choice node (Custom Packaging)
choice_packaging = OperatorPOWL(operator=Operator.XOR, children=[custom_packaging, skip])

# Define the choice node (Label Design)
choice_label = OperatorPOWL(operator=Operator.XOR, children=[label_design, skip])

# Define the choice node (Hand Labeling)
choice_hand_labeling = OperatorPOWL(operator=Operator.XOR, children=[hand_labeling, skip])

# Define the choice node (Regulatory Audit)
choice_audit = OperatorPOWL(operator=Operator.XOR, children=[regulatory_audit, skip])

# Define the choice node (Batch Documentation)
choice_documentation = OperatorPOWL(operator=Operator.XOR, children=[batch_documentation, skip])

# Define the choice node (Market Launch)
choice_launch = OperatorPOWL(operator=Operator.XOR, children=[market_launch, skip])

# Define the root node (Initial Blending)
root = StrictPartialOrder(nodes=[loop_stability, choice_sampling, choice_review, choice_adjustment, choice_packaging, choice_label, choice_hand_labeling, choice_audit, choice_documentation, choice_launch])

# Add edges between nodes
root.order.add_edge(loop_stability, choice_sampling)
root.order.add_edge(choice_sampling, choice_review)
root.order.add_edge(choice_review, choice_adjustment)
root.order.add_edge(choice_adjustment, choice_packaging)
root.order.add_edge(choice_packaging, choice_label)
root.order.add_edge(choice_label, choice_hand_labeling)
root.order.add_edge(choice_hand_labeling, choice_audit)
root.order.add_edge(choice_audit, choice_documentation)
root.order.add_edge(choice_documentation, choice_launch)

# Print the root POWL model
print(root)