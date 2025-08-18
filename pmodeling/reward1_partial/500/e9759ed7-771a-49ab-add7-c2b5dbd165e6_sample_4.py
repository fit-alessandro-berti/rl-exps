from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[allergen_check, market_research])
loop = OperatorPOWL(operator=Operator.LOOP, children=[bottle_design, label_approval])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[packaging_setup, batch_mixing])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[scent_profiling, client_feedback])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[release_scheduling, regulatory_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[sales_training, None])

# Define the root POWL model
root = StrictPartialOrder(nodes=[ingredient_sourcing, sample_testing, oil_extraction, blend_formulation, quality_control, aging_process, xor, loop, xor2, xor3, xor4, xor5])
root.order.add_edge(ingredient_sourcing, sample_testing)
root.order.add_edge(sample_testing, oil_extraction)
root.order.add_edge(oil_extraction, blend_formulation)
root.order.add_edge(blend_formulation, quality_control)
root.order.add_edge(quality_control, aging_process)
root.order.add_edge(aging_process, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)