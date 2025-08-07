import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
initial = Transition(label='Initial Inquiry')
doc_rev = Transition(label='Document Review')
hist_res = Transition(label='Historical Research')
mat_samp = Transition(label='Material Sampling')
fore_test = Transition(label='Forensic Testing')
own_audit = Transition(label='Ownership Audit')
legal_ver = Transition(label='Legal Verification')
ethical_sc = Transition(label='Ethical Screening')
expert_con = Transition(label='Expert Consultation')
cultural_ass = Transition(label='Cultural Assessment')
cond_survey = Transition(label='Condition Survey')
prov_map = Transition(label='Provenance Mapping')
risk_anal = Transition(label='Risk Analysis')
report_comp = Transition(label='Report Compilation')
acq_approve = Transition(label='Acquisition Approval')
rep_review = Transition(label='Repatriation Review')
arch_storage = Transition(label='Archival Storage')

# Build the loop body: Risk Analysis -> Report Compilation -> Acquisition Approval
loop_body = StrictPartialOrder(nodes=[risk_anal, report_comp, acq_approve])
loop_body.order.add_edge(risk_anal, report_comp)
loop_body.order.add_edge(report_comp, acq_approve)

# LOOP: do Initial Inquiry -> Document Review -> Historical Research -> Material Sampling -> Forensic Testing
# then either exit or do Ownership Audit -> Legal Verification -> Ethical Screening -> Expert Consultation
# then do Cultural Assessment -> Condition Survey -> Provenance Mapping
# then either do Risk Analysis -> Report Compilation -> Acquisition Approval
# or do Repatriation Review -> Archival Storage, then repeat
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        StrictPartialOrder(nodes=[
            initial,
            doc_rev,
            hist_res,
            mat_samp,
            fore_test
        ]),
        StrictPartialOrder(nodes=[
            own_audit,
            legal_ver,
            ethical_sc,
            expert_con
        ]),
        StrictPartialOrder(nodes=[
            cultural_ass,
            cond_survey,
            prov_map
        ]),
        loop_body
    ]
)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    initial,
    doc_rev,
    hist_res,
    mat_samp,
    fore_test,
    own_audit,
    legal_ver,
    ethical_sc,
    expert_con,
    cultural_ass,
    cond_survey,
    prov_map,
    loop,
    rep_review,
    arch_storage
])

# Define the control‐flow dependencies
root.order.add_edge(initial, doc_rev)
root.order.add_edge(doc_rev, hist_res)
root.order.add_edge(hist_res, mat_samp)
root.order.add_edge(mat_samp, fore_test)
root.order.add_edge(fore_test, own_audit)
root.order.add_edge(own_audit, legal_ver)
root.order.add_edge(legal_ver, ethical_sc)
root.order.add_edge(ethical_sc, expert_con)
root.order.add_edge(expert_con, cultural_ass)
root.order.add_edge(cultural_ass, cond_survey)
root.order.add_edge(cond_survey, prov_map)
root.order.add_edge(prov_map, loop)
root.order.add_edge(loop, rep_review)
root.order.add_edge(loop, arch_storage)