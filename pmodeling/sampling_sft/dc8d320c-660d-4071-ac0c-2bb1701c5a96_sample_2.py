import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake       = Transition(label='Artifact Intake')
prov_check   = Transition(label='Provenance Check')
mat_test     = Transition(label='Material Testing')
hist_review  = Transition(label='Historical Review')
expert_int   = Transition(label='Expert Interview')
cond_audit   = Transition(label='Condition Audit')
digital_cat  = Transition(label='Digital Catalog')
forgo_detect = Transition(label='Forgery Detection')
legal_com    = Transition(label='Legal Compliance')
rest_plan    = Transition(label='Restoration Plan')
val_report   = Transition(label='Valuation Report')
market_an    = Transition(label='Market Analysis')
final_app    = Transition(label='Final Approval')
sale_prep    = Transition(label='Sale Preparation')
client_not   = Transition(label='Client Notification')

# Loop for expert interviews (one or more)
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_int, expert_int])

# Loop for forgery detection (one or more)
forgo_loop = OperatorPOWL(operator=Operator.LOOP, children=[forgo_detect, forgo_detect])

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake, prov_check, mat_test, hist_review,
    expert_loop, digital_cat, legal_com, forgos_loop,
    cond_audit, rest_plan, val_report,
    market_an, final_app, sale_prep, client_not
])

# Define the control-flow dependencies
root.order.add_edge(intake, prov_check)
root.order.add_edge(intake, mat_test)
root.order.add_edge(prov_check, expert_loop)
root.order.add_edge(mat_test, expert_loop)
root.order.add_edge(prov_check, digital_cat)
root.order.add_edge(mat_test, digital_cat)
root.order.add_edge(expert_loop, legal_com)
root.order.add_edge(digital_cat, legal_com)
root.order.add_edge(expert_loop, forgos_loop)
root.order.add_edge(digital_cat, forgos_loop)
root.order.add_edge(legal_com, cond_audit)
root.order.add_edge(forgos_loop, cond_audit)
root.order.add_edge(cond_audit, rest_plan)
root.order.add_edge(cond_audit, val_report)
root.order.add_edge(rest_plan, val_report)
root.order.add_edge(val_report, market_an)
root.order.add_edge(market_an, final_app)
root.order.add_edge(final_app, sale_prep)
root.order.add_edge(sale_prep, client_not)