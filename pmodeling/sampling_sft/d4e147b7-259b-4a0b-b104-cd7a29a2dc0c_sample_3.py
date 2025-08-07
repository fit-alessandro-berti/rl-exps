import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
t_intake    = Transition(label='Artifact Intake')
t_visual    = Transition(label='Visual Scan')
t_material  = Transition(label='Material Test')
t_radioc    = Transition(label='Radiocarbon Check')
t_archive   = Transition(label='Archive Review')
t_prov      = Transition(label='Provenance Search')
t_expert    = Transition(label='Expert Consult')
t_micro     = Transition(label='Microscope Exam')
t_infrared  = Transition(label='Infrared Scan')
t_legal     = Transition(label='Legal Verify')
t_condition = Transition(label='Condition Report')
t_catalog   = Transition(label='Digital Catalog')
t_audit     = Transition(label='Ownership Audit')
t_restore   = Transition(label='Restoration Plan')
t_final     = Transition(label='Final Approval')
t_cert      = Transition(label='Authentication Cert')

# Build the loop for expert consultation
# Loop: do Expert Consult, then either exit or do Material Test & Microscope Exam & Infrared Scan again
expert_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[t_expert, StrictPartialOrder(nodes=[t_material, t_micro, t_infrared])]
)

# Build the partial order for the initial physical inspection phase
po_inspection = StrictPartialOrder(nodes=[
    t_visual,
    t_material,
    t_radioc,
    t_archive,
    t_prov,
    expert_loop,
    t_legal,
    t_condition,
    t_catalog,
    t_audit
])
po_inspection.order.add_edge(t_visual, t_material)
po_inspection.order.add_edge(t_visual, t_radioc)
po_inspection.order.add_edge(t_archive, t_prov)
po_inspection.order.add_edge(t_prov, expert_loop)
po_inspection.order.add_edge(expert_loop, t_legal)
po_inspection.order.add_edge(t_legal, t_condition)
po_inspection.order.add_edge(t_condition, t_catalog)
po_inspection.order.add_edge(t_catalog, t_audit)

# Build the partial order for the final restoration & approval phase
po_approval = StrictPartialOrder(nodes=[
    t_restore,
    t_final,
    t_cert
])
po_approval.order.add_edge(t_restore, t_final)
po_approval.order.add_edge(t_final, t_cert)

# Final partial order: perform initial inspection, then either exit or do restoration & approval
root = StrictPartialOrder(nodes=[po_inspection, po_approval])
root.order.add_edge(po_inspection, po_approval)