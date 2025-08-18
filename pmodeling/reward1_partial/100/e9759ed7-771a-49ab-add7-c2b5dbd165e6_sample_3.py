import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[ingredient_sourcing, sample_testing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[oil_extraction, blend_formulation])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[quality_control, allergen_check])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[market_research, bottle_design])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[label_approval, packaging_setup])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[batch_mixing, scent_profiling])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[client_feedback, release_scheduling])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[regulatory_review, sales_training])

# Define the root node
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor2, xor5)
root.order.add_edge(xor3, xor6)
root.order.add_edge(xor3, xor7)
root.order.add_edge(xor4, xor8)
root.order.add_edge(xor5, xor8)
root.order.add_edge(xor6, xor8)
root.order.add_edge(xor7, xor8)