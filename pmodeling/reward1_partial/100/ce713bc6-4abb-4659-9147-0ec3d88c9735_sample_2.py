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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        initial_inquiry,
        document_review,
        historical_research,
        material_sampling,
        forensic_testing,
        ownership_audit,
        legal_verification,
        ethical_screening,
        expert_consultation,
        cultural_assessment,
        condition_survey,
        provenance_mapping,
        risk_analysis,
        report_compilation,
        acquisition_approval,
        repatriation_review,
        archival_storage
    ],
    order=[
        (initial_inquiry, document_review),
        (document_review, historical_research),
        (historical_research, material_sampling),
        (material_sampling, forensic_testing),
        (forensic_testing, ownership_audit),
        (ownership_audit, legal_verification),
        (legal_verification, ethical_screening),
        (ethical_screening, expert_consultation),
        (expert_consultation, cultural_assessment),
        (cultural_assessment, condition_survey),
        (condition_survey, provenance_mapping),
        (provenance_mapping, risk_analysis),
        (risk_analysis, report_compilation),
        (report_compilation, acquisition_approval),
        (acquisition_approval, repatriation_review),
        (repatriation_review, archival_storage)
    ]
)