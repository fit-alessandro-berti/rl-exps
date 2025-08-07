import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
intake       = Transition(label='Artifact Intake')
prelim       = Transition(label='Preliminary Check')
historical   = Transition(label='Historical Review')
chemical     = Transition(label='Chemical Test')
provenance   = Transition(label='Provenance Audit')
expert       = Transition(label='Expert Panel')
token        = Transition(label='Token Minting')
legal        = Transition(label='Legal Review')
compliance   = Transition(label='Compliance Check')
insurance    = Transition(label='Insurance Valuation')
risk         = Transition(label='Risk Assessment')
packaging    = Transition(label='Packaging Prep')
climate      = Transition(label='Climate Control')
transport    = Transition(label='Transport Setup')
final        = Transition(label='Final Approval')

# Loop for expert validation: do Expert Panel, then either exit or do another Expert Panel and repeat
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert, expert])

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake, prelim, historical, chemical, provenance, expert_loop,
    token, legal, compliance, insurance, risk,
    packaging, climate, transport, final
])

# Add edges
root.order.add_edge(intake, prelim)
root.order.add_edge(prelim, historical)
root.order.add_edge(prelim, chemical)
root.order.add_edge(prelim, provenance)
root.order.add_edge(historical, expert_loop)
root.order.add_edge(chemical, expert_loop)
root.order.add_edge(provenance, expert_loop)
root.order.add_edge(expert_loop, token)
root.order.add_edge(token, legal)
root.order.add_edge(legal, compliance)
root.order.add_edge(compliance, insurance)
root.order.add_edge(insurance, risk)
root.order.add_edge(risk, packaging)
root.order.add_edge(packaging, climate)
root.order.add_edge(climate, transport)
root.order.add_edge(transport, final)