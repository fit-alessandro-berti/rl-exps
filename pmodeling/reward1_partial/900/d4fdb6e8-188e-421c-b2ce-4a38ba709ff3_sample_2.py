import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

initial_inspection_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, provenance_check, digital_imaging, database_search])
expert_panel_review = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, legal_review])
cultural_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[cultural_audit, condition_report, risk_assessment])
insurance_validation = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, transport_plan])
final_certification_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_certification, archive_entry, publication_prep])

root = StrictPartialOrder(nodes=[artifact_receipt, initial_inspection_loop, expert_panel_review, cultural_audit_loop, insurance_validation, final_certification_loop])
root.order.add_edge(artifact_receipt, initial_inspection_loop)
root.order.add_edge(initial_inspection_loop, expert_panel_review)
root.order.add_edge(expert_panel_review, cultural_audit_loop)
root.order.add_edge(cultural_audit_loop, insurance_validation)
root.order.add_edge(insurance_validation, final_certification_loop)

print(root)