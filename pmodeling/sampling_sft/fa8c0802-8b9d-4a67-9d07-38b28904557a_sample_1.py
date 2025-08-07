import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
data_agg       = Transition(label='Data Aggregation')
anomaly_detect = Transition(label='Anomaly Detect')
risk_assess    = Transition(label='Risk Assess')
demand_model   = Transition(label='Demand Model')
stakeholder    = Transition(label='Stakeholder Sync')
auto_negotiate = Transition(label='Auto Negotiate')
inventory_opt  = Transition(label='Inventory Optimize')
contingency    = Transition(label='Contingency Plan')
resource_alloc = Transition(label='Resource Allocate')
sustainability = Transition(label='Sustainability Check')
compliance     = Transition(label='Compliance Verify')
impact_score   = Transition(label='Impact Score')
distribution   = Transition(label='Distribution Plan')
feedback_loop  = Transition(label='Feedback Loop')
performance    = Transition(label='Performance Audit')
schedule_exec  = Transition(label='Schedule Execute')

# Build the loop body: performance audit -> schedule execution
loop_body = StrictPartialOrder(nodes=[performance, schedule_exec])
loop_body.order.add_edge(performance, schedule_exec)

# LOOP: after each feedback loop, perform the audit & schedule execution, then loop again
loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, loop_body])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    data_agg, anomaly_detect, risk_assess, demand_model,
    stakeholder, auto_negotiate, inventory_opt,
    contingency, resource_alloc, sustainability, compliance,
    impact_score, distribution, loop
])

# Define the control-flow dependencies
root.order.add_edge(data_agg, anomaly_detect)
root.order.add_edge(data_agg, risk_assess)
root.order.add_edge(data_agg, demand_model)
root.order.add_edge(anomaly_detect, stakeholder)
root.order.add_edge(risk_assess, stakeholder)
root.order.add_edge(demand_model, stakeholder)
root.order.add_edge(stakeholder, auto_negotiate)
root.order.add_edge(stakeholder, contingency)
root.order.add_edge(stakeholder, resource_alloc)
root.order.add_edge(stakeholder, sustainability)
root.order.add_edge(stakeholder, compliance)
root.order.add_edge(auto_negotiate, inventory_opt)
root.order.add_edge(contingency, inventory_opt)
root.order.add_edge(resource_alloc, inventory_opt)
root.order.add_edge(sustainability, impact_score)
root.order.add_edge(compliance, impact_score)
root.order.add_edge(inventory_opt, distribution)
root.order.add_edge(distribution, loop)
root.order.add_edge(loop, performance)