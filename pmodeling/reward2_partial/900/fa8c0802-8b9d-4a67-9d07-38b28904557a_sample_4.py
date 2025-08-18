import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define the POWL model
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

# Define the dependencies (partial order)
root.order.add_edge(data_aggregation, anomaly_detect)
root.order.add_edge(anomaly_detect, risk_assess)
root.order.add_edge(risk_assess, demand_model)
root.order.add_edge(demand_model, stakeholder_sync)
root.order.add_edge(stakeholder_sync, auto_negotiate)
root.order.add_edge(auto_negotiate, inventory_optimize)
root.order.add_edge(inventory_optimize, contingency_plan)
root.order.add_edge(contingency_plan, resource_allocate)
root.order.add_edge(resource_allocate, sustainability_check)
root.order.add_edge(sustainability_check, compliance_verify)
root.order.add_edge(compliance_verify, impact_score)
root.order.add_edge(impact_score, distribution_plan)
root.order.add_edge(distribution_plan, feedback_loop)
root.order.add_edge(feedback_loop, performance_audit)
root.order.add_edge(performance_audit, schedule_execute)

# Print the POWL model
print(root)