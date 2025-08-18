import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions (activities)
intake_review = Transition(label='Intake Review')
preliminary_inspect = Transition(label='Preliminary Inspect')
provenance_check = Transition(label='Provenance Check')
archival_research = Transition(label='Archival Research')
material_testing = Transition(label='Material Testing')
radiocarbon_date = Transition(label='Radiocarbon Date')
stylistic_assess = Transition(label='Stylistic Assess')
expert_consult = Transition(label='Expert Consult')
findings_compile = Transition(label='Findings Compile')
internal_review = Transition(label='Internal Review')
client_present = Transition(label='Client Present')
approval_confirm = Transition(label='Approval Confirm')
secure_package = Transition(label='Secure Package')
transport_arrange = Transition(label='Transport Arrange')
chain_custody = Transition(label='Chain Custody')

# Define silent transitions
skip = SilentTransition()

# Define partial order components
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, archival_research, material_testing, radiocarbon_date, stylistic_assess, expert_consult])
xor_findings = OperatorPOWL(operator=Operator.XOR, children=[internal_review, client_present, approval_confirm])
xor_transport = OperatorPOWL(operator=Operator.XOR, children=[secure_package, transport_arrange])
partial_order = StrictPartialOrder(nodes=[intake_review, preliminary_inspect, loop_provenance, xor_findings, xor_transport, chain_custody])
partial_order.order.add_edge(intake_review, preliminary_inspect)
partial_order.order.add_edge(preliminary_inspect, loop_provenance)
partial_order.order.add_edge(loop_provenance, xor_findings)
partial_order.order.add_edge(xor_findings, xor_transport)
partial_order.order.add_edge(xor_transport, chain_custody)

root = partial_order