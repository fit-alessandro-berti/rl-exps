import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
initial_inquiry = Transition(label='Initial Inquiry')
document_review = Transition(label='Document Review')
historical_research = Transition(label='Historical Research')
material_sampling = Transition(label='Material Sampling')
forensic_testing = Transition(label='Forensic Testing')
ownership_audit = Transition(label='Ownership Audit')
legal_verification = Transition(label='Legal Verification')
ethical_screening = Transition(label='Ethical Screening')
expert_consultation = Transition(label='Expert Consultation')
cultural_assessment = Transition(label='Cultural Assessment')
condition_survey = Transition(label='Condition Survey')
provenance_mapping = Transition(label='Provenance Mapping')
risk_analysis = Transition(label='Risk Analysis')
report_compilation = Transition(label='Report Compilation')
acquisition_approval = Transition(label='Acquisition Approval')
repatriation_review = Transition(label='Repatriation Review')
archival_storage = Transition(label='Archival Storage')

# Define the loop and choice nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[historical_research, material_sampling, forensic_testing, ownership_audit, legal_verification, ethical_screening, expert_consultation, cultural_assessment, condition_survey, provenance_mapping, risk_analysis])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[report_compilation, acquisition_approval, repatriation_review, archival_storage])
xor = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])

# Define the root node with the defined transitions
root = StrictPartialOrder(nodes=[initial_inquiry, document_review, xor])
root.order.add_edge(initial_inquiry, document_review)
root.order.add_edge(document_review, xor)

# Print the root node for verification
print(root)