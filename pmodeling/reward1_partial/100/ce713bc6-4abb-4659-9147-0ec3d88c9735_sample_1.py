from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define sub-processes
historical_subprocess = StrictPartialOrder(nodes=[historical_research, material_sampling, forensic_testing, ownership_audit, legal_verification, expert_consultation, cultural_assessment, condition_survey, provenance_mapping, risk_analysis, report_compilation])
ethical_subprocess = StrictPartialOrder(nodes=[ethical_screening, archival_storage])

# Define loop node for the main process
loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_subprocess, ethical_subprocess])

# Define exclusive choice for the main process
xor = OperatorPOWL(operator=Operator.XOR, children=[acquisition_approval, repatriation_review])

# Define root process
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)