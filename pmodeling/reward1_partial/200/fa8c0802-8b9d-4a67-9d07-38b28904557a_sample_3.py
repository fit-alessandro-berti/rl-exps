import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (data_aggregation, anomaly_detect),
        (data_aggregation, risk_assess),
        (data_aggregation, demand_model),
        (anomaly_detect, stakeholder_sync),
        (anomaly_detect, auto_negotiate),
        (anomaly_detect, inventory_optimize),
        (risk_assess, contingency_plan),
        (risk_assess, resource_allocate),
        (risk_assess, sustainability_check),
        (risk_assess, compliance_verify),
        (demand_model, impact_score),
        (demand_model, distribution_plan),
        (stakeholder_sync, feedback_loop),
        (stakeholder_sync, performance_audit),
        (auto_negotiate, inventory_optimize),
        (auto_negotiate, contingency_plan),
        (auto_negotiate, resource_allocate),
        (auto_negotiate, sustainability_check),
        (auto_negotiate, compliance_verify),
        (inventory_optimize, impact_score),
        (inventory_optimize, distribution_plan),
        (contingency_plan, resource_allocate),
        (contingency_plan, sustainability_check),
        (contingency_plan, compliance_verify),
        (resource_allocate, sustainability_check),
        (resource_allocate, compliance_verify),
        (sustainability_check, impact_score),
        (sustainability_check, distribution_plan),
        (compliance_verify, impact_score),
        (compliance_verify, distribution_plan),
        (impact_score, distribution_plan),
        (distribution_plan, feedback_loop),
        (distribution_plan, performance_audit),
        (feedback_loop, performance_audit),
        (performance_audit, schedule_execute)
    ]
)

# Print the root
print(root)