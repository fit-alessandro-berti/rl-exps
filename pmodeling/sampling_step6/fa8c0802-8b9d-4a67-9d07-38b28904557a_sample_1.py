from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their names exactly as given in the description
data_aggregation = Transition(label='Data Aggregation')
anomaly_detect = Transition(label='Anomaly Detect')
risk_assess = Transition(label='Risk Assess')
demand_model = Transition(label='Demand Model')
stakeholder_sync = Transition(label='Stakeholder Sync')
auto_negotiate = Transition(label='Auto Negotiate')
inventory_optimize = Transition(label='Inventory Optimize')
contingency_plan = Transition(label='Contingency Plan')
resource_allocate = Transition(label='Resource Allocate')
sustainability_check = Transition(label='Sustainability Check')
compliance_verify = Transition(label='Compliance Verify')
impact_score = Transition(label='Impact Score')
distribution_plan = Transition(label='Distribution Plan')
feedback_loop = Transition(label='Feedback Loop')
performance_audit = Transition(label='Performance Audit')
schedule_execute = Transition(label='Schedule Execute')

# Create the POWL model
root = StrictPartialOrder(nodes=[
    data_aggregation,
    anomaly_detect,
    risk_assess,
    demand_model,
    stakeholder_sync,
    auto_negotiate,
    inventory_optimize,
    contingency_plan,
    resource_allocate,
    sustainability_check,
    compliance_verify,
    impact_score,
    distribution_plan,
    feedback_loop,
    performance_audit,
    schedule_execute
])

# Since there are no dependencies mentioned in the description, we don't need to add any edges to the root