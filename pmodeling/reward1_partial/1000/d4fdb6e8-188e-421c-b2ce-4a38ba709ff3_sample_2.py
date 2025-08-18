import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for the end of each activity
skip = SilentTransition()

# Define the partial order model
root = StrictPartialOrder()

# Add activities to the partial order
root.add_transition(artifact_receipt)
root.add_transition(initial_inspection)
root.add_transition(material_testing)
root.add_transition(provenance_check)
root.add_transition(digital_imaging)
root.add_transition(database_search)
root.add_transition(expert_consult)
root.add_transition(legal_review)
root.add_transition(cultural_audit)
root.add_transition(condition_report)
root.add_transition(risk_assessment)
root.add_transition(insurance_setup)
root.add_transition(transport_plan)
root.add_transition(final_certification)
root.add_transition(archive_entry)
root.add_transition(publication_prep)

# Define the partial order relationships
root.add_edge(artifact_receipt, initial_inspection)
root.add_edge(initial_inspection, material_testing)
root.add_edge(material_testing, provenance_check)
root.add_edge(provenance_check, digital_imaging)
root.add_edge(digital_imaging, database_search)
root.add_edge(database_search, expert_consult)
root.add_edge(expert_consult, legal_review)
root.add_edge(legal_review, cultural_audit)
root.add_edge(cultural_audit, condition_report)
root.add_edge(condition_report, risk_assessment)
root.add_edge(risk_assessment, insurance_setup)
root.add_edge(insurance_setup, transport_plan)
root.add_edge(transport_plan, final_certification)
root.add_edge(final_certification, archive_entry)
root.add_edge(archive_entry, publication_prep)

# Define the order of activities
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

# Print the final model
print(root)