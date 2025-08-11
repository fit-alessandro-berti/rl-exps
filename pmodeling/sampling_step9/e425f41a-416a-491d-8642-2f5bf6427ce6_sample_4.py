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

skip = SilentTransition()

# Define the POWL model structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[botanical_extraction, initial_blending, sensory_testing, chemical_analysis, recipe_refinement, stability_check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[client_sampling, feedback_review, final_adjustment])
xor = OperatorPOWL(operator=Operator.XOR, children=[custom_packaging, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[label_design, hand_labeling])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[regulatory_audit, batch_documentation])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[limited_release, market_launch])

root = StrictPartialOrder(nodes=[loop1, loop2, xor, xor2, xor3, xor4])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)

# Save the final result in the variable 'root'