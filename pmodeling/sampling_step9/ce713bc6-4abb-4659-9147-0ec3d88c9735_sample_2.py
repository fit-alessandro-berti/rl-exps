import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
Initial_Inquiry = Transition(label='Initial Inquiry')
Document_Review = Transition(label='Document Review')
Historical_Research = Transition(label='Historical Research')
Material_Sampling = Transition(label='Material Sampling')
Forensic_Testing = Transition(label='Forensic Testing')
Ownership_Audit = Transition(label='Ownership Audit')
Legal_Verification = Transition(label='Legal Verification')
Ethical_Screening = Transition(label='Ethical Screening')
Expert_Consultation = Transition(label='Expert Consultation')
Cultural_Assessment = Transition(label='Cultural Assessment')
Condition_Survey = Transition(label='Condition Survey')
Provenance_Mapping = Transition(label='Provenance Mapping')
Risk_Analysis = Transition(label='Risk Analysis')
Report_Compilation = Transition(label='Report Compilation')
Acquisition_Approval = Transition(label='Acquisition Approval')
Repatriation_Review = Transition(label='Repatriation Review')
Archival_Storage = Transition(label='Archival Storage')

skip = SilentTransition()

historical_research = OperatorPOWL(operator=Operator.XOR, children=[Historical_Research, skip])
material_sampling = OperatorPOWL(operator=Operator.XOR, children=[Material_Sampling, skip])
forensic_testing = OperatorPOWL(operator=Operator.XOR, children=[Forensic_Testing, skip])
ownership_audit = OperatorPOWL(operator=Operator.XOR, children=[Ownership_Audit, skip])
legal_verification = OperatorPOWL(operator=Operator.XOR, children=[Legal_Verification, skip])
ethical_screening = OperatorPOWL(operator=Operator.XOR, children=[Ethical_Screening, skip])
expert_consultation = OperatorPOWL(operator=Operator.XOR, children=[Expert_Consultation, skip])
cultural_assessment = OperatorPOWL(operator=Operator.XOR, children=[Cultural_Assessment, skip])
condition_survey = OperatorPOWL(operator=Operator.XOR, children=[Condition_Survey, skip])
provenance_mapping = OperatorPOWL(operator=Operator.XOR, children=[Provenance_Mapping, skip])
risk_analysis = OperatorPOWL(operator=Operator.XOR, children=[Risk_Analysis, skip])
report_compilation = OperatorPOWL(operator=Operator.XOR, children=[Report_Compilation, skip])
acquisition_approval = OperatorPOWL(operator=Operator.XOR, children=[Acquisition_Approval, skip])
repatriation_review = OperatorPOWL(operator=Operator.XOR, children=[Repatriation_Review, skip])
archival_storage = OperatorPOWL(operator=Operator.XOR, children=[Archival_Storage, skip])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[historical_research, material_sampling, forensic_testing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ownership_audit, legal_verification, ethical_screening])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[expert_consultation, cultural_assessment, condition_survey])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_mapping, risk_analysis, report_compilation])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[acquisition_approval, repatriation_review, archival_storage])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)

print(root)