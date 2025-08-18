import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define sub-processes
expert_panel = OperatorPOWL(operator=Operator.XOR, children=[sensory_panel, skip])
refinement_process = OperatorPOWL(operator=Operator.LOOP, children=[refinement_loop, stability_test])
compliance_process = OperatorPOWL(operator=Operator.LOOP, children=[compliance_audit, market_survey])

# Define root process
root = StrictPartialOrder(nodes=[client_profiling, ingredient_sourcing, quality_check, blend_experiment, maturation_cycle, expert_panel, refinement_process, compliance_process, packaging_design, batch_coordination, order_finalize, distribution_plan, inventory_update])
root.order.add_edge(client_profiling, ingredient_sourcing)
root.order.add_edge(ingredient_sourcing, quality_check)
root.order.add_edge(quality_check, blend_experiment)
root.order.add_edge(blend_experiment, maturation_cycle)
root.order.add_edge(maturation_cycle, expert_panel)
root.order.add_edge(expert_panel, refinement_loop)
root.order.add_edge(refinement_loop, stability_test)
root.order.add_edge(stability_test, refinement_process)
root.order.add_edge(refinement_process, packaging_design)
root.order.add_edge(packaging_design, batch_coordination)
root.order.add_edge(batch_coordination, order_finalize)
root.order.add_edge(order_finalize, distribution_plan)
root.order.add_edge(distribution_plan, inventory_update)