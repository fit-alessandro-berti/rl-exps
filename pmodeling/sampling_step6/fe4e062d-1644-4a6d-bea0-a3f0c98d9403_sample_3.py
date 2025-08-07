import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the root process as a strict partial order
root = StrictPartialOrder(nodes=[
    client_profiling,
    ingredient_sourcing,
    quality_check,
    blend_experiment,
    maturation_cycle,
    sensory_panel,
    refinement_loop,
    stability_test,
    packaging_design,
    batch_coordination,
    compliance_audit,
    market_survey,
    feedback_review,
    order_finalize,
    distribution_plan,
    inventory_update
])

# The order of the nodes is not specified, so we assume they are in the order they appear in the description
# If there are dependencies between nodes, they would be added here as edges in the root object

# The root object now contains the POWL model for the process