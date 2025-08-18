from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Define the activities
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

# Define the control flow
# Client Profiling -> Ingredient Sourcing -> Quality Check
root.nodes.add(client_profiling)
root.nodes.add(ingredient_sourcing)
root.nodes.add(quality_check)
root.order.add_edge(client_profiling, ingredient_sourcing)
root.order.add_edge(ingredient_sourcing, quality_check)

# Quality Check -> Blend Experiment
root.order.add_edge(quality_check, blend_experiment)

# Blend Experiment -> Maturation Cycle
root.order.add_edge(blend_experiment, maturation_cycle)

# Maturation Cycle -> Sensory Panel
root.order.add_edge(maturation_cycle, sensory_panel)

# Sensory Panel -> Refinement Loop
root.order.add_edge(sensory_panel, refinement_loop)

# Refinement Loop -> Stability Test
root.order.add_edge(refinement_loop, stability_test)

# Stability Test -> Packaging Design
root.order.add_edge(stability_test, packaging_design)

# Packaging Design -> Batch Coordination
root.order.add_edge(packaging_design, batch_coordination)

# Batch Coordination -> Compliance Audit
root.order.add_edge(batch_coordination, compliance_audit)

# Compliance Audit -> Market Survey
root.order.add_edge(compliance_audit, market_survey)

# Market Survey -> Feedback Review
root.order.add_edge(market_survey, feedback_review)

# Feedback Review -> Order Finalize
root.order.add_edge(feedback_review, order_finalize)

# Order Finalize -> Distribution Plan
root.order.add_edge(order_finalize, distribution_plan)

# Distribution Plan -> Inventory Update
root.order.add_edge(distribution_plan, inventory_update)

# Save the final result in the variable 'root'