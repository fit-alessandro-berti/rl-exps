import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) as POWL nodes
client_profiling = Transition(label='Client Profiling')
ingredient_sourcing = Transition(label='Ingredient Sourcing')
quality_check = Transition(label='Quality Check')
blend_experiment = Transition(label='Blend Experiment')
maturation_cycle = Transition(label='Maturation Cycle')
sensory_panel = Transition(label='Sensory Panel')
refinement_loop = OperatorPOWL(operator=Operator.LOOP, children=[blend_experiment, sensory_panel])
stability_test = Transition(label='Stability Test')
packaging_design = Transition(label='Packaging Design')
batch_coordination = Transition(label='Batch Coordination')
compliance_audit = Transition(label='Compliance Audit')
market_survey = Transition(label='Market Survey')
feedback_review = Transition(label='Feedback Review')
order_finalize = Transition(label='Order Finalize')
distribution_plan = Transition(label='Distribution Plan')
inventory_update = Transition(label='Inventory Update')

# Define the partial order with dependencies
root = StrictPartialOrder(nodes=[client_profiling, ingredient_sourcing, quality_check, blend_experiment, maturation_cycle, refinement_loop, stability_test, packaging_design, batch_coordination, compliance_audit, market_survey, feedback_review, order_finalize, distribution_plan, inventory_update])
root.order.add_edge(client_profiling, ingredient_sourcing)
root.order.add_edge(ingredient_sourcing, quality_check)
root.order.add_edge(quality_check, blend_experiment)
root.order.add_edge(blend_experiment, maturation_cycle)
root.order.add_edge(maturation_cycle, refinement_loop)
root.order.add_edge(refinement_loop, stability_test)
root.order.add_edge(stability_test, packaging_design)
root.order.add_edge(packaging_design, batch_coordination)
root.order.add_edge(batch_coordination, compliance_audit)
root.order.add_edge(compliance_audit, market_survey)
root.order.add_edge(market_survey, feedback_review)
root.order.add_edge(feedback_review, order_finalize)
root.order.add_edge(order_finalize, distribution_plan)
root.order.add_edge(distribution_plan, inventory_update)

print(root)