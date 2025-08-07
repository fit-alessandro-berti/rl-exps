import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
intake       = Transition(label='Artifact Intake')
visual       = Transition(label='Visual Scan')
material     = Transition(label='Material Test')
radiocarbon  = Transition(label='Radiocarbon Check')
archive      = Transition(label='Archive Review')
prov_search  = Transition(label='Provenance Search')
expert       = Transition(label='Expert Consult')
microscope   = Transition(label='Microscope Exam')
infrared     = Transition(label='Infrared Scan')
legal        = Transition(label='Legal Verify')
condition    = Transition(label='Condition Report')
digital      = Transition(label='Digital Catalog')
ownership    = Transition(label='Ownership Audit')
restoration  = Transition(label='Restoration Plan')
final        = Transition(label='Final Approval')
cert         = Transition(label='Authentication Cert')

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake, visual, material, radiocarbon,
    archive, prov_search, expert,
    microscope, infrared,
    legal, condition,
    digital, ownership, restoration, final, cert
])

# Initial dependencies
root.order.add_edge(intake, visual)
root.order.add_edge(intake, material)
root.order.add_edge(intake, radiocarbon)

# Material test then provenance search
root.order.add_edge(material, prov_search)
root.order.add_edge(radiocarbon, prov_search)

# Parallel research and expert consultation
root.order.add_edge(prov_search, expert)
root.order.add_edge(prov_search, archive)

# After research, parallel micro/infrared exams
root.order.add_edge(expert, microscope)
root.order.add_edge(expert, infrared)
root.order.add_edge(archive, microscope)
root.order.add_edge(archive, infrared)

# After both micro/infrared, legal and condition reports
root.order.add_edge(microscope, legal)
root.order.add_edge(infrared, legal)
root.order.add_edge(microscope, condition)
root.order.add_edge(infrared, condition)

# After legal and condition, digital catalog and ownership audit
root.order.add_edge(legal, digital)
root.order.add_edge(condition, digital)
root.order.add_edge(legal, ownership)
root.order.add_edge(condition, ownership)

# Parallel restoration plan and final approval
root.order.add_edge(digital, restoration)
root.order.add_edge(ownership, restoration)
root.order.add_edge(digital, final)
root.order.add_edge(ownership, final)

# Final approval leads to authentication certificate
root.order.add_edge(final, cert)