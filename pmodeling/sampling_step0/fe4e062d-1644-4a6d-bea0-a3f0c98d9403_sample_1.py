import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
client_profiling = Transition(label='Client Profiling')
ingredient_sourcing = Transition(label='Ingredient Sourcing')
quality_check = Transition(label='Quality Check')
blend_experiment = Transition(label='Blend Experiment')
maturation_cycle = Transition(label='Maturation Cycle')
sensory_panel = Transition(label='Sensory Panel')
refinement_loop = Transition(label='Refinement Loop')
stability_test = Transition(label='Stability Test')
packaging_design = Transition(label='Packaging Design')
batch_coordination = Transition(label='Batch Coordination')
compliance_audit = Transition(label='Compliance Audit')
market_survey = Transition(label='Market Survey')
feedback_review = Transition(label='Feedback Review')
order_finalize = Transition(label='Order Finalize')
distribution_plan = Transition(label='Distribution Plan')
inventory_update = Transition(label='Inventory Update')

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[refinement_loop, stability_test])
loop = OperatorPOWL(operator=Operator.LOOP, children=[blend_experiment, maturation_cycle, sensory_panel])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, batch_coordination])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, market_survey])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, order_finalize])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, inventory_update])

# Define the POWL model
root = StrictPartialOrder(nodes=[client_profiling, ingredient_sourcing, quality_check, loop, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(client_profiling, ingredient_sourcing)
root.order.add_edge(ingredient_sourcing, quality_check)
root.order.add_edge(quality_check, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, distribution_plan)
root.order.add_edge(xor5, inventory_update)

# Print the POWL model
print(root)