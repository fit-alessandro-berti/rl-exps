import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
inq = Transition(label='Inquiry Review')
cbo = Transition(label='Client Onboard')
cd = Transition(label='Concept Draft')
fc = Transition(label='Feedback Cycle')
cs = Transition(label='Contract Setup')
ps = Transition(label='Payment Schedule')
ms = Transition(label='Material Sourcing')
ac = Transition(label='Artwork Create')
qc = Transition(label='Quality Check')
fs = Transition(label='Frame Selection')
pp = Transition(label='Packaging Prep')
sa = Transition(label='Shipment Arrange')
dc = Transition(label='Delivery Confirm')
psf = Transition(label='Post-Sale Support')
rm = Transition(label='Revision Manage')
dm = Transition(label='Delay Mitigate')

# Define the process
inq_cbo = OperatorPOWL(operator=Operator.XOR, children=[inq, cbo])
cbo_cd = OperatorPOWL(operator=Operator.XOR, children=[cbo, cd])
cd_fc = OperatorPOWL(operator=Operator.XOR, children=[cd, fc])
fc_cs = OperatorPOWL(operator=Operator.XOR, children=[fc, cs])
cs_ps = OperatorPOWL(operator=Operator.XOR, children=[cs, ps])
ps_ms = OperatorPOWL(operator=Operator.XOR, children=[ps, ms])
ms_ac = OperatorPOWL(operator=Operator.XOR, children=[ms, ac])
ac_qc = OperatorPOWL(operator=Operator.XOR, children=[ac, qc])
qc_fs = OperatorPOWL(operator=Operator.XOR, children=[qc, fs])
fs_pp = OperatorPOWL(operator=Operator.XOR, children=[fs, pp])
pp_sa = OperatorPOWL(operator=Operator.XOR, children=[pp, sa])
sa_dcf = OperatorPOWL(operator=Operator.XOR, children=[sa, dc])
dc_psf = OperatorPOWL(operator=Operator.XOR, children=[dc, psf])
psf_rm = OperatorPOWL(operator=Operator.XOR, children=[psf, rm])
rm_dm = OperatorPOWL(operator=Operator.XOR, children=[rm, dm])

# Define the partial order
root = StrictPartialOrder(nodes=[inq_cbo, cbo_cd, cd_fc, fc_cs, cs_ps, ps_ms, ms_ac, ac_qc, qc_fs, fs_pp, pp_sa, sa_dcf, dc_psf, psf_rm, rm_dm])
root.order.add_edge(inq_cbo, cbo_cd)
root.order.add_edge(cbo_cd, cd_fc)
root.order.add_edge(cd_fc, fc_cs)
root.order.add_edge(fc_cs, cs_ps)
root.order.add_edge(cs_ps, ps_ms)
root.order.add_edge(ps_ms, ms_ac)
root.order.add_edge(ms_ac, ac_qc)
root.order.add_edge(ac_qc, qc_fs)
root.order.add_edge(qc_fs, fs_pp)
root.order.add_edge(fs_pp, pp_sa)
root.order.add_edge(pp_sa, sa_dcf)
root.order.add_edge(sa_dcf, dc_psf)
root.order.add_edge(dc_psf, psf_rm)
root.order.add_edge(psf_rm, rm_dm)

# Print the root
print(root)