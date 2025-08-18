from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define each activity as a Transition object
artifact_receipt = Transition(label='Artifact Receipt')
initial_inspection = Transition(label='Initial Inspection')
material_testing = Transition(label='Material Testing')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
database_search = Transition(label='Database Search')
expert_consult = Transition(label='Expert Consult')
legal_review = Transition(label='Legal Review')
cultural_audit = Transition(label='Cultural Audit')
condition_report = Transition(label='Condition Report')
risk_assessment = Transition(label='Risk Assessment')
insurance_setup = Transition(label='Insurance Setup')
transport_plan = Transition(label='Transport Plan')
final_certification = Transition(label='Final Certification')
archive_entry = Transition(label='Archive Entry')
publication_prep = Transition(label='Publication Prep')

# Define silent transitions (empty labels)
skip_initial_inspection = SilentTransition()
skip_material_testing = SilentTransition()
skip_provenance_check = SilentTransition()
skip_database_search = SilentTransition()
skip_expert_consult = SilentTransition()
skip_legal_review = SilentTransition()
skip_cultural_audit = SilentTransition()
skip_condition_report = SilentTransition()
skip_risk_assessment = SilentTransition()
skip_insurance_setup = SilentTransition()
skip_transport_plan = SilentTransition()
skip_final_certification = SilentTransition()
skip_archive_entry = SilentTransition()
skip_publication_prep = SilentTransition()

# Define the partial order
root = StrictPartialOrder()

# Define the workflow steps
root.nodes.extend([
    artifact_receipt,
    initial_inspection,
    material_testing,
    provenance_check,
    digital_imaging,
    database_search,
    expert_consult,
    legal_review,
    cultural_audit,
    condition_report,
    risk_assessment,
    insurance_setup,
    transport_plan,
    final_certification,
    archive_entry,
    publication_prep
])

# Define the order of execution
root.order.add_edge(artifact_receipt, initial_inspection)
root.order.add_edge(initial_inspection, material_testing)
root.order.add_edge(material_testing, provenance_check)
root.order.add_edge(provenance_check, digital_imaging)
root.order.add_edge(digital_imaging, database_search)
root.order.add_edge(database_search, expert_consult)
root.order.add_edge(expert_consult, legal_review)
root.order.add_edge(legal_review, cultural_audit)
root.order.add_edge(cultural_audit, condition_report)
root.order.add_edge(condition_report, risk_assessment)
root.order.add_edge(risk_assessment, insurance_setup)
root.order.add_edge(insurance_setup, transport_plan)
root.order.add_edge(transport_plan, final_certification)
root.order.add_edge(final_certification, archive_entry)
root.order.add_edge(archive_entry, publication_prep)

# Add silent transitions where necessary
root.order.add_edge(initial_inspection, skip_initial_inspection)
root.order.add_edge(material_testing, skip_material_testing)
root.order.add_edge(provenance_check, skip_provenance_check)
root.order.add_edge(digital_imaging, skip_database_search)
root.order.add_edge(database_search, skip_expert_consult)
root.order.add_edge(expert_consult, skip_legal_review)
root.order.add_edge(legal_review, skip_cultural_audit)
root.order.add_edge(cultural_audit, skip_condition_report)
root.order.add_edge(condition_report, skip_risk_assessment)
root.order.add_edge(risk_assessment, skip_insurance_setup)
root.order.add_edge(insurance_setup, skip_transport_plan)
root.order.add_edge(transport_plan, skip_final_certification)
root.order.add_edge(final_certification, skip_archive_entry)
root.order.add_edge(archive_entry, skip_publication_prep)

# Ensure all nodes are connected
root.order.add_edge(skip_initial_inspection, initial_inspection)
root.order.add_edge(skip_material_testing, material_testing)
root.order.add_edge(skip_provenance_check, provenance_check)
root.order.add_edge(skip_database_search, digital_imaging)
root.order.add_edge(skip_expert_consult, database_search)
root.order.add_edge(skip_legal_review, expert_consult)
root.order.add_edge(skip_cultural_audit, legal_review)
root.order.add_edge(skip_condition_report, cultural_audit)
root.order.add_edge(skip_risk_assessment, condition_report)
root.order.add_edge(skip_insurance_setup, risk_assessment)
root.order.add_edge(skip_transport_plan, insurance_setup)
root.order.add_edge(skip_final_certification, transport_plan)
root.order.add_edge(skip_archive_entry, final_certification)
root.order.add_edge(skip_publication_prep, archive_entry)

# Ensure the root is defined correctly
root.order.add_edge(skip_publication_prep, publication_prep)