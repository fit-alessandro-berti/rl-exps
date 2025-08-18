import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[botanical_extraction, initial_blending, sensory_testing, chemical_analysis, recipe_refinement, stability_check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[client_sampling, feedback_review, final_adjustment])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[custom_packaging, label_design, hand_labeling, regulatory_audit, batch_documentation])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[limited_release, market_launch])

root = StrictPartialOrder(nodes=[ingredient_sourcing, loop1, loop2, loop3, loop4])
root.order.add_edge(ingredient_sourcing, loop1)
root.order.add_edge(ingredient_sourcing, loop2)
root.order.add_edge(ingredient_sourcing, loop3)
root.order.add_edge(ingredient_sourcing, loop4)

print(root)