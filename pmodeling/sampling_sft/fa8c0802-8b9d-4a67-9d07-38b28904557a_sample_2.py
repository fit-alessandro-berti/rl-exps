import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
data_agg        = Transition(label='Data Aggregation')
anomaly_detect  = Transition(label='Anomaly Detect')
risk_assess     = Transition(label='Risk Assess')
demand_model    = Transition(label='Demand Model')
stakeholder_sync= Transition(label='Stakeholder Sync')
auto_negotiate  = Transition(label='Auto Negotiate')
inventory_opt   = Transition(label='Inventory Optimize')
contingency_plan= Transition(label='Contingency Plan')
resource_alloc  = Transition(label='Resource Allocate')
sustainability_chk= Transition(label='Sustainability Check')
compliance_ver  = Transition(label='Compliance Verify')
impact_score    = Transition(label='Impact Score')
distribution_plan= Transition(label='Distribution Plan')
feedback_loop   = Transition(label='Feedback Loop')
performance_audit= Transition(label='Performance Audit')
schedule_execute= Transition(label='Schedule Execute')

# Loop body for the adaptive loop: perform all activities except Schedule Execute
body = StrictPartialOrder(nodes=[
    data_agg,
    anomaly_detect,
    risk_assess,
    demand_model,
    stakeholder_sync,
    auto_negotiate,
    inventory_opt,
    contingency_plan,
    resource_alloc,
    sustainability_chk,
    compliance_ver,
    impact_score,
    distribution_plan,
    feedback_loop,
    performance_audit
])
body.order.add_edge(data_agg, anomaly_detect)
body.order.add_edge(anomaly_detect, risk_assess)
body.order.add_edge(risk_assess, demand_model)
body.order.add_edge(demand_model, stakeholder_sync)
body.order.add_edge(stakeholder_sync, auto_negotiate)
body.order.add_edge(auto_negotiate, inventory_opt)
body.order.add_edge(inventory_opt, contingency_plan)
body.order.add_edge(contingency_plan, resource_alloc)
body.order.add_edge(resource_alloc, sustainability_chk)
body.order.add_edge(sustainability_chk, compliance_ver)
body.order.add_edge(compliance_ver, impact_score)
body.order.add_edge(impact_score, distribution_plan)
body.order.add_edge(distribution_plan, feedback_loop)
body.order.add_edge(feedback_loop, performance_audit)

# The adaptive loop: do one round of the body, then optionally repeat
adaptive_loop = OperatorPOWL(operator=Operator.LOOP, children=[body, schedule_execute])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    adaptive_loop,
    data_agg,
    anomaly_detect,
    risk_assess,
    demand_model,
    stakeholder_sync,
    auto_negotiate,
    inventory_opt,
    contingency_plan,
    resource_alloc,
    sustainability_chk,
    compliance_ver,
    impact_score,
    distribution_plan,
    feedback_loop,
    performance_audit
])
root.order.add_edge(adaptive_loop, data_agg)
root.order.add_edge(adaptive_loop, anomaly_detect)
root.order.add_edge(adaptive_loop, risk_assess)
root.order.add_edge(adaptive_loop, demand_model)
root.order.add_edge(adaptive_loop, stakeholder_sync)
root.order.add_edge(adaptive_loop, auto_negotiate)
root.order.add_edge(adaptive_loop, inventory_opt)
root.order.add_edge(adaptive_loop, contingency_plan)
root.order.add_edge(adaptive_loop, resource_alloc)
root.order.add_edge(adaptive_loop, sustainability_chk)
root.order.add_edge(adaptive_loop, compliance_ver)
root.order.add_edge(adaptive_loop, impact_score)
root.order.add_edge(adaptive_loop, distribution_plan)
root.order.add_edge(adaptive_loop, feedback_loop)
root.order.add_edge(adaptive_loop, performance_audit)