import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
data_agg      = Transition(label='Data Aggregation')
anomaly_detect= Transition(label='Anomaly Detect')
risk_assess   = Transition(label='Risk Assess')
demand_model  = Transition(label='Demand Model')
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

# Build the loop body (Anomaly Detect -> Risk Assess -> Demand Model -> Stakeholder Sync -> Auto Negotiate -> Inventory Optimize)
body = StrictPartialOrder(nodes=[
    anomaly_detect,
    risk_assess,
    demand_model,
    stakeholder_sync,
    auto_negotiate,
    inventory_optimize
])
body.order.add_edge(anomaly_detect, risk_assess)
body.order.add_edge(risk_assess, demand_model)
body.order.add_edge(demand_model, stakeholder_sync)
body.order.add_edge(stakeholder_sync, auto_negotiate)
body.order.add_edge(auto_negotiate, inventory_optimize)

# Build the full adaptive cycle: body -> Contingency Plan -> Resource Allocate -> Sustainability Check -> Compliance Verify -> Impact Score -> Distribution Plan
cycle = StrictPartialOrder(nodes=[
    contingency_plan,
    resource_allocate,
    sustainability_check,
    compliance_verify,
    impact_score,
    distribution_plan
])
cycle.order.add_edge(body, contingency_plan)
cycle.order.add_edge(contingency_plan, resource_allocate)
cycle.order.add_edge(resource_allocate, sustainability_check)
cycle.order.add_edge(sustainability_check, compliance_verify)
cycle.order.add_edge(compliance_verify, impact_score)
cycle.order.add_edge(impact_score, distribution_plan)

# Build the full process: initial aggregation followed by a loop of adaptive cycles and final execution
root = StrictPartialOrder(nodes=[
    data_agg,
    cycle,
    feedback_loop,
    performance_audit,
    schedule_execute
])
root.order.add_edge(data_agg, cycle)
root.order.add_edge(cycle, feedback_loop)
root.order.add_edge(feedback_loop, cycle)
root.order.add_edge(cycle, performance_audit)
root.order.add_edge(performance_audit, schedule_execute)