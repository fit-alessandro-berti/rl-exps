from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define exclusive choice for sensory testing and chemical analysis
sensory_or_chemical = OperatorPOWL(operator=Operator.XOR, children=[sensory_testing, chemical_analysis])

# Define loop for recipe refinement and stability check
loop = OperatorPOWL(operator=Operator.LOOP, children=[recipe_refinement, stability_check])

# Define exclusive choice for final adjustment and limited release
final_or_release = OperatorPOWL(operator=Operator.XOR, children=[final_adjustment, limited_release])

# Define exclusive choice for custom packaging and market launch
packaging_or_launch = OperatorPOWL(operator=Operator.XOR, children=[custom_packaging, market_launch])

# Define root process
root = StrictPartialOrder(nodes=[ingredient_sourcing, botanical_extraction, initial_blending, sensory_or_chemical, loop, final_or_release, packaging_or_launch])
root.order.add_edge(ingredient_sourcing, botanical_extraction)
root.order.add_edge(botanical_extraction, initial_blending)
root.order.add_edge(initial_blending, sensory_or_chemical)
root.order.add_edge(sensory_or_chemical, loop)
root.order.add_edge(loop, final_or_release)
root.order.add_edge(final_or_release, packaging_or_launch)