import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
intake = Transition(label='Intake Review')
pre_inspect = Transition(label='Preliminary Inspect')
prov_check = Transition(label='Provenance Check')
arch_research = Transition(label='Archival Research')
material_test = Transition(label='Material Testing')
radiocarbon = Transition(label='Radiocarbon Date')
stylistic_assess = Transition(label='Stylistic Assess')
expert_consult = Transition(label='Expert Consult')
findings_compile = Transition(label='Findings Compile')
internal_review = Transition(label='Internal Review')
client_present = Transition(label='Client Present')
approval_confirm = Transition(label='Approval Confirm')
secure_package = Transition(label='Secure Package')
transport_arrange = Transition(label='Transport Arrange')
chain_custody = Transition(label='Chain Custody')

# Loop for expert consultations (repeat until client approval)
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, client_present])

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake,
    pre_inspect,
    prov_check,
    arch_research,
    material_test,
    radiocarbon,
    stylistic_assess,
    expert_loop,
    findings_compile,
    internal_review,
    approval_confirm,
    secure_package,
    transport_arrange,
    chain_custody
])

# Define the control-flow dependencies
root.order.add_edge(intake, pre_inspect)
root.order.add_edge(pre_inspect, prov_check)
root.order.add_edge(prov_check, arch_research)
root.order.add_edge(prov_check, material_test)
root.order.add_edge(material_test, radiocarbon)
root.order.add_edge(radiocarbon, stylistic_assess)
root.order.add_edge(stylistic_assess, expert_loop)
root.order.add_edge(expert_loop, findings_compile)
root.order.add_edge(findings_compile, internal_review)
root.order.add_edge(internal_review, approval_confirm)
root.order.add_edge(approval_confirm, secure_package)
root.order.add_edge(secure_package, transport_arrange)
root.order.add_edge(transport_arrange, chain_custody)