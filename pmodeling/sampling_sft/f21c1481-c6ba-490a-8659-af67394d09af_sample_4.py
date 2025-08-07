import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
coll_survey   = Transition(label='Collection Survey')
prov_check    = Transition(label='Provenance Check')
leg_review    = Transition(label='Legal Review')
sci_test      = Transition(label='Scientific Test')
mat_analysis  = Transition(label='Material Analysis')
own_audit     = Transition(label='Ownership Audit')
eth_screening = Transition(label='Ethical Screening')
cond_report   = Transition(label='Condition Report')
exp_consult   = Transition(label='Expert Consultation')
trans_plan    = Transition(label='Transport Planning')
secure_pack   = Transition(label='Secure Packing')
custom_clear  = Transition(label='Customs Clearance')
insu_setup    = Transition(label='Insurance Setup')
exhibit_prep  = Transition(label='Exhibit Preparation')
final_approve = Transition(label='Final Approval')

# Loop for iterative scientific testing and analysis
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sci_test, mat_analysis]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    coll_survey,
    prov_check,
    leg_review,
    loop,
    cond_report,
    exp_consult,
    trans_plan,
    secure_pack,
    custom_clear,
    insu_setup,
    exhibit_prep,
    final_approve
])

# Define the control-flow dependencies
root.order.add_edge(coll_survey, prov_check)
root.order.add_edge(coll_survey, leg_review)

root.order.add_edge(prov_check, loop)
root.order.add_edge(leg_review, loop)

root.order.add_edge(loop, cond_report)
root.order.add_edge(cond_report, exp_consult)

root.order.add_edge(exp_consult, trans_plan)
root.order.add_edge(trans_plan, secure_pack)
root.order.add_edge(secure_pack, custom_clear)
root.order.add_edge(custom_clear, insu_setup)

root.order.add_edge(insu_setup, exhibit_prep)
root.order.add_edge(exhibit_prep, final_approve)