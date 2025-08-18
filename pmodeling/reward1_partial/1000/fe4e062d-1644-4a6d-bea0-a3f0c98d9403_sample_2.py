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

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, ingredient_sourcing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[blend_experiment, sensory_panel])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[maturation_cycle, stability_test])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, batch_coordination])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, market_survey])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, order_finalize])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, inventory_update])

# Define the partial order
root = StrictPartialOrder(nodes=[client_profiling, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(client_profiling, xor1)
root.order.add_edge(client_profiling, xor2)
root.order.add_edge(client_profiling, xor3)
root.order.add_edge(client_profiling, xor4)
root.order.add_edge(client_profiling, xor5)
root.order.add_edge(client_profiling, xor6)
root.order.add_edge(client_profiling, xor7)

# Print the POWL model
print(root)