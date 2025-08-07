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
legal_comp   = Transition(label='Legal Compliance')
rest_plan    = Transition(label='Restoration Plan')
val_report   = Transition(label='Valuation Report')
market_anal  = Transition(label='Market Analysis')
final_appro  = Transition(label='Final Approval')
sale_prep    = Transition(label='Sale Preparation')
client_not   = Transition(label='Client Notification')

# Loop for expert interviews: do one expert interview, then optionally another
expert_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[expert_int, expert_int]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake,
    prov_check,
    mat_test,
    hist_review,
    expert_loop,
    cond_audit,
    digital_cat,
    forgo_detect,
    legal_comp,
    rest_plan,
    val_report,
    market_anal,
    final_appro,
    sale_prep,
    client_not
])

# Sequential flow
root.order.add_edge(intake, prov_check)
root.order.add_edge(prov_check, mat_test)
root.order.add_edge(mat_test, hist_review)
root.order.add_edge(hist_review, expert_loop)
root.order.add_edge(expert_loop, cond_audit)
root.order.add_edge(cond_audit, digital_cat)
root.order.add_edge(digital_cat, forgo_detect)
root.order.add_edge(forgo_detect, legal_comp)
root.order.add_edge(legal_comp, rest_plan)
root.order.add_edge(rest_plan, val_report)
root.order.add_edge(val_report, market_anal)
root.order.add_edge(market_anal, final_appro)
root.order.add_edge(final_appro, sale_prep)
root.order.add_edge(sale_prep, client_not)

# Final approval can exit early, so we need a silent transition to handle the loop exit
skip = SilentTransition()
root.order.add_edge(final_appro, skip)
root.order.add_edge(skip, client_not)