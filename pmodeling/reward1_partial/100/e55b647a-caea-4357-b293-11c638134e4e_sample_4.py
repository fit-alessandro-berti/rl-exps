from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the process
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
material_sampling = Transition(label='Material Sampling')
scientific_test = Transition(label='Scientific Test')
expert_review = Transition(label='Expert Review')
archive_search = Transition(label='Archive Search')
legal_verify = Transition(label='Legal Verify')
ownership_confirm = Transition(label='Ownership Confirm')
compliance_audit = Transition(label='Compliance Audit')
data_documentation = Transition(label='Data Documentation')
interim_report = Transition(label='Interim Report')
department_review = Transition(label='Department Review')
consensus_meeting = Transition(label='Consensus Meeting')
final_approval = Transition(label='Final Approval')
artifact_release = Transition(label='Artifact Release')

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        artifact_intake,
        provenance_check,
        material_sampling,
        scientific_test,
        expert_review,
        archive_search,
        legal_verify,
        ownership_confirm,
        compliance_audit,
        data_documentation,
        interim_report,
        department_review,
        consensus_meeting,
        final_approval,
        artifact_release
    ],
    order=[
        # Define the dependencies between activities
        # Example: artifact_intake --> provenance_check
        (artifact_intake, provenance_check),
        (artifact_intake, material_sampling),
        (provenance_check, scientific_test),
        (material_sampling, scientific_test),
        (scientific_test, expert_review),
        (scientific_test, archive_search),
        (expert_review, legal_verify),
        (legal_verify, ownership_confirm),
        (ownership_confirm, compliance_audit),
        (compliance_audit, data_documentation),
        (data_documentation, interim_report),
        (interim_report, department_review),
        (department_review, consensus_meeting),
        (consensus_meeting, final_approval),
        (final_approval, artifact_release)
    ]
)