import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    intake_review, preliminary_inspect, provenance_check, archival_research,
    material_testing, radiocarbon_date, stylistic_assess, expert_consult,
    findings_compile, internal_review, client_present, approval_confirm,
    secure_package, transport_arrange, chain_custody
])

# Define dependencies between transitions
root.order.add_edge(intake_review, preliminary_inspect)
root.order.add_edge(preliminary_inspect, provenance_check)
root.order.add_edge(provenance_check, archival_research)
root.order.add_edge(archival_research, material_testing)
root.order.add_edge(material_testing, radiocarbon_date)
root.order.add_edge(radiocarbon_date, stylistic_assess)
root.order.add_edge(stylistic_assess, expert_consult)
root.order.add_edge(expert_consult, findings_compile)
root.order.add_edge(findings_compile, internal_review)
root.order.add_edge(internal_review, client_present)
root.order.add_edge(client_present, approval_confirm)
root.order.add_edge(approval_confirm, secure_package)
root.order.add_edge(secure_package, transport_arrange)
root.order.add_edge(transport_arrange, chain_custody)

# Print the final POWL model
print(root)