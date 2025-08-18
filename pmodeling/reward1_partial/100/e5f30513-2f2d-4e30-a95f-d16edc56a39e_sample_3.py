from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process
intake_review_to_preliminary_inspect = OperatorPOWL(operator=Operator.XOR, children=[intake_review, preliminary_inspect])
provenance_check_to_archival_research = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archival_research])
material_testing_to_radiocarbon_date = OperatorPOWL(operator=Operator.XOR, children=[material_testing, radiocarbon_date])
stylistic_assess_to_expert_consult = OperatorPOWL(operator=Operator.XOR, children=[stylistic_assess, expert_consult])

# Define the parallel path for testing and consulting
parallel_path = StrictPartialOrder(nodes=[material_testing_to_radiocarbon_date, stylistic_assess_to_expert_consult], order={material_testing_to_radiocarbon_date: stylistic_assess_to_expert_consult, stylistic_assess_to_expert_consult: material_testing_to_radiocarbon_date})

# Define the loop for the parallel path
loop = OperatorPOWL(operator=Operator.LOOP, children=[parallel_path])

# Define the main process flow
main_flow = StrictPartialOrder(nodes=[intake_review_to_preliminary_inspect, provenance_check_to_archival_research, loop, findings_compile, internal_review, client_present, approval_confirm, secure_package, transport_arrange, chain_custody])

# Connect the nodes
main_flow.order.add_edge(intake_review_to_preliminary_inspect, provenance_check_to_archival_research)
main_flow.order.add_edge(provenance_check_to_archival_research, loop)
main_flow.order.add_edge(loop, findings_compile)
main_flow.order.add_edge(findings_compile, internal_review)
main_flow.order.add_edge(internal_review, client_present)
main_flow.order.add_edge(client_present, approval_confirm)
main_flow.order.add_edge(approval_confirm, secure_package)
main_flow.order.add_edge(secure_package, transport_arrange)
main_flow.order.add_edge(transport_arrange, chain_custody)

# Define the root
root = main_flow