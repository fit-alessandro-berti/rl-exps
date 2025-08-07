import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake     = Transition(label='Artifact Intake')
cond       = Transition(label='Condition Check')
material   = Transition(label='Material Test')
style      = Transition(label='Style Compare')
carbon     = Transition(label='Carbon Dating')
document   = Transition(label='Document Review')
provenance = Transition(label='Provenance Check')
imaging    = Transition(label='Digital Imaging')
forgery    = Transition(label='Forgery Scan')
expert     = Transition(label='Expert Consult')
research   = Transition(label='Historical Research')
panel      = Transition(label='Panel Review')
report     = Transition(label='Report Draft')
approval   = Transition(label='Final Approval')
catalog    = Transition(label='Catalog Entry')

# Silent transition for loop exit
skip = SilentTransition()

# Build the verification and analysis phase as a partial order
verification = StrictPartialOrder(nodes=[
    intake,
    cond,
    material,
    style,
    carbon,
    document,
    provenance,
    imaging,
    forgery,
    expert,
    research
])
verification.order.add_edge(intake, cond)
verification.order.add_edge(cond, material)
verification.order.add_edge(cond, style)
verification.order.add_edge(material, carbon)
verification.order.add_edge(style, carbon)
verification.order.add_edge(carbon, document)
verification.order.add_edge(document, provenance)
verification.order.add_edge(document, imaging)
verification.order.add_edge(imaging, forgery)
verification.order.add_edge(provenance, forgery)
verification.order.add_edge(forgery, expert)
verification.order.add_edge(research, expert)

# Build the authentication phase as a partial order
authentication = StrictPartialOrder(nodes=[
    research,
    expert,
    panel,
    report,
    approval,
    catalog
])
authentication.order.add_edge(research, expert)
authentication.order.add_edge(expert, panel)
authentication.order.add_edge(panel, report)
authentication.order.add_edge(report, approval)
authentication.order.add_edge(approval, catalog)

# Loop: repeat historical research and expert consultation until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[research, expert])

# Final POWL model: start with verification, then the loop, and finally authentication
root = StrictPartialOrder(nodes=[
    verification,
    loop,
    authentication
])
root.order.add_edge(verification, loop)
root.order.add_edge(loop, authentication)