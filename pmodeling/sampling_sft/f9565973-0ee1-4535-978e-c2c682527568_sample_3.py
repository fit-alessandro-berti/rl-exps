import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake       = Transition(label='Artifact Intake')
survey       = Transition(label='Initial Survey')
material     = Transition(label='Material Test')
historical   = Transition(label='Historical Check')
registry     = Transition(label='Registry Search')
owner        = Transition(label='Owner Interview')
condition    = Transition(label='Condition Report')
forgery      = Transition(label='Forgery Scan')
digital      = Transition(label='Digital Tagging')
ledger       = Transition(label='Ledger Entry')
expert       = Transition(label='Expert Review')
legal        = Transition(label='Legal Verify')
provenance   = Transition(label='Provenance Draft')
approval     = Transition(label='Client Approval')
certificate  = Transition(label='Final Certificate')
archive      = Transition(label='Archive Storage')

# Silent transition for optional steps
skip = SilentTransition()

# Loop for optional forgery scan
loop_forgery = OperatorPOWL(operator=Operator.LOOP, children=[forgery, skip])

# Exclusive choice for optional material test vs. condition report
material_xor = OperatorPOWL(operator=Operator.XOR, children=[material, condition])

# Exclusive choice for optional registry search vs. owner interview
registry_xor = OperatorPOWL(operator=operator.XOR, children=[registry, owner])

# Exclusive choice for optional digital tagging vs. ledger entry
digital_xor = OperatorPOWL(operator=operator.XOR, children=[digital, ledger])

# Exclusive choice for optional expert review vs. legal verify
expert_xor = OperatorPOWL(operator=operator.XOR, children=[expert, legal])

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake, survey,
    material_xor,
    registry_xor,
    loop_forgery,
    condition,
    historical,
    provenance,
    approval,
    certificate,
    archive
])

# Define the control-flow dependencies
root.order.add_edge(intake, survey)
root.order.add_edge(survey, material_xor)
root.order.add_edge(material_xor, historical)
root.order.add_edge(historical, registry_xor)
root.order.add_edge(registry_xor, provenance)
root.order.add_edge(provenance, approval)
root.order.add_edge(provenance, certificate)
root.order.add_edge(provenance, archive)
root.order.add_edge(loop_forgery, provenance)
root.order.add_edge(condition, provenance)