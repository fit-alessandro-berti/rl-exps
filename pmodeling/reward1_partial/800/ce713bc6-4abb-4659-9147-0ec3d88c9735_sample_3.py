import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[ethical_screening, archival_storage])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[repatriation_review, acquisition_approval])
loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_research, material_sampling, forensic_testing, ownership_audit, legal_verification])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[cultural_assessment, condition_survey, provenance_mapping, risk_analysis])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[report_compilation, xor1])
root = StrictPartialOrder(nodes=[initial_inquiry, document_review, loop, xor3, xor4])
root.order.add_edge(loop, xor3)
root.order.add_edge(xor3, xor4)