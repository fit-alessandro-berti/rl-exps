import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
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

# Define the loop for Artifact Receipt, Initial Inspection, Material Testing, and Provenance Check
loop_artifact_receipt_initial_inspection_material_testing_provenance_check = OperatorPOWL(operator=Operator.LOOP, children=[artifact_receipt, initial_inspection, material_testing, provenance_check])

# Define the exclusive choice for Digital Imaging, Database Search, Expert Consult, Legal Review, Cultural Audit, Condition Report, Risk Assessment, Insurance Setup, Transport Plan, Final Certification, Archive Entry, and Publication Prep
xor_digital_imaging_database_search_expert_consult_legal_review_cultural_audit_condition_report_risk_assessment_insurance_setup_transport_plan_final_certification_archive_entry_publication_prep = OperatorPOWL(operator=Operator.XOR, children=[digital_imaging, database_search, expert_consult, legal_review, cultural_audit, condition_report, risk_assessment, insurance_setup, transport_plan, final_certification, archive_entry, publication_prep])

# Create the root Partial Order
root = StrictPartialOrder(nodes=[loop_artifact_receipt_initial_inspection_material_testing_provenance_check, xor_digital_imaging_database_search_expert_consult_legal_review_cultural_audit_condition_report_risk_assessment_insurance_setup_transport_plan_final_certification_archive_entry_publication_prep])
root.order.add_edge(loop_artifact_receipt_initial_inspection_material_testing_provenance_check, xor_digital_imaging_database_search_expert_consult_legal_review_cultural_audit_condition_report_risk_assessment_insurance_setup_transport_plan_final_certification_archive_entry_publication_prep)