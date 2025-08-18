import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
loop_artifact_inspection = OperatorPOWL(operator=Operator.LOOP, children=[preliminary_inspect, provenance_check])
loop_scientific_analysis = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, radiocarbon_date])
loop_stylistic_consultation = OperatorPOWL(operator=Operator.LOOP, children=[stylistic_assess, expert_consult])

xor_report_processing = OperatorPOWL(operator=Operator.XOR, children=[internal_review, client_present])

root = StrictPartialOrder(nodes=[loop_artifact_inspection, loop_scientific_analysis, loop_stylistic_consultation, xor_report_processing, secure_package, transport_arrange, chain_custody])
root.order.add_edge(loop_artifact_inspection, loop_scientific_analysis)
root.order.add_edge(loop_scientific_analysis, loop_stylistic_consultation)
root.order.add_edge(loop_stylistic_consultation, xor_report_processing)
root.order.add_edge(xor_report_processing, secure_package)
root.order.add_edge(secure_package, transport_arrange)
root.order.add_edge(transport_arrange, chain_custody)