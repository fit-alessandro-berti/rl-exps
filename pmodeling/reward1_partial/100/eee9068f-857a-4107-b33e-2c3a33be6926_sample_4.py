import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
archive_search = Transition(label='Archive Search')
expert_interview = Transition(label='Expert Interview')
material_scan = Transition(label='Material Scan')
age_analysis = Transition(label='Age Analysis')
stylistic_review = Transition(label='Stylistic Review')
context_mapping = Transition(label='Context Mapping')
legal_clearance = Transition(label='Legal Clearance')
data_compilation = Transition(label='Data Compilation')
report_drafting = Transition(label='Report Drafting')
peer_review = Transition(label='Peer Review')
final_assessment = Transition(label='Final Assessment')
acquisition_plan = Transition(label='Acquisition Plan')
restoration_prep = Transition(label='Restoration Prep')
documentation = Transition(label='Documentation')
data_backup = Transition(label='Data Backup')

# Define silent transitions for parallel processing
skip_archive_search = SilentTransition()
skip_stylistic_review = SilentTransition()
skip_data_backup = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        artifact_intake,
        provenance_check,
        archive_search,
        expert_interview,
        material_scan,
        age_analysis,
        stylistic_review,
        context_mapping,
        legal_clearance,
        data_compilation,
        report_drafting,
        peer_review,
        final_assessment,
        acquisition_plan,
        restoration_prep,
        documentation,
        data_backup
    ],
    order={
        # Artifact Intake -> Provenance Check
        artifact_intake: provenance_check,
        # Provenance Check -> Archive Search
        provenance_check: archive_search,
        # Archive Search -> Expert Interview
        archive_search: expert_interview,
        # Expert Interview -> Material Scan
        expert_interview: material_scan,
        # Material Scan -> Age Analysis
        material_scan: age_analysis,
        # Age Analysis -> Stylistic Review
        age_analysis: stylistic_review,
        # Stylistic Review -> Context Mapping
        stylistic_review: context_mapping,
        # Context Mapping -> Legal Clearance
        context_mapping: legal_clearance,
        # Legal Clearance -> Data Compilation
        legal_clearance: data_compilation,
        # Data Compilation -> Report Drafting
        data_compilation: report_drafting,
        # Report Drafting -> Peer Review
        report_drafting: peer_review,
        # Peer Review -> Final Assessment
        peer_review: final_assessment,
        # Final Assessment -> Acquisition Plan
        final_assessment: acquisition_plan,
        # Acquisition Plan -> Restoration Prep
        acquisition_plan: restoration_prep,
        # Restoration Prep -> Documentation
        restoration_prep: documentation,
        # Documentation -> Data Backup
        documentation: data_backup
    }
)

# Add dependencies between parallel processing steps
root.order.add_edge(archive_search, skip_archive_search)
root.order.add_edge(stylistic_review, skip_stylistic_review)
root.order.add_edge(data_backup, skip_data_backup)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for data backup
root.order.add_edge(data_backup, documentation)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for stylistic review
root.order.add_edge(stylistic_review, context_mapping)

# Add dependencies for legal clearance
root.order.add_edge(legal_clearance, data_compilation)

# Add dependencies for data compilation
root.order.add_edge(data_compilation, report_drafting)

# Add dependencies for report drafting
root.order.add_edge(report_drafting, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup, peer_review)

# Add dependencies for peer review
root.order.add_edge(peer_review, final_assessment)

# Add dependencies for final assessment
root.order.add_edge(final_assessment, acquisition_plan)
root.order.add_edge(final_assessment, restoration_prep)

# Add dependencies for restoration prep
root.order.add_edge(restoration_prep, documentation)

# Add dependencies for documentation
root.order.add_edge(documentation, data_backup)

# Add dependencies for data backup
root.order.add_edge(data_backup