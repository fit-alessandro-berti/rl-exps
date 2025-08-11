import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Flow 1: Sourcing, Testing, Extraction
sourcing_test_extraction = OperatorPOWL(operator=Operator.XOR, children=[ingredient_sourcing, sample_testing, oil_extraction])

# Flow 2: Blending, Quality Control, Aging
blending_quality_aging = OperatorPOWL(operator=Operator.XOR, children=[blend_formulation, quality_control, aging_process])

# Flow 3: Allergen Check, Market Research, Design
allergen_market_design = OperatorPOWL(operator=Operator.XOR, children=[allergen_check, market_research, bottle_design])

# Flow 4: Label Approval, Packaging Setup, Mixing
label_packaging_mixing = OperatorPOWL(operator=Operator.XOR, children=[label_approval, packaging_setup, batch_mixing])

# Flow 5: Scent Profiling, Client Feedback
scents_feedback = OperatorPOWL(operator=Operator.XOR, children=[scent_profiling, client_feedback])

# Flow 6: Release Scheduling, Regulatory Review
release_regulatory = OperatorPOWL(operator=Operator.XOR, children=[release_scheduling, regulatory_review])

# Flow 7: Sales Training
sales_training_node = OperatorPOWL(operator=Operator.XOR, children=[sales_training])

# Loop through the main processes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[sourcing_test_extraction])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[blending_quality_aging])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[allergen_market_design])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[label_packaging_mixing])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[scents_feedback])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[release_regulatory])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[sales_training_node])

# Connect the loops
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7])

# Define the order of execution
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop1)

print(root)