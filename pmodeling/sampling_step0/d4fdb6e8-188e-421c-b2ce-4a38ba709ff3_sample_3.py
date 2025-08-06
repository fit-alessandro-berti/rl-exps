import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip_inspection = SilentTransition()
skip_test = SilentTransition()
skip_search = SilentTransition()
skip_expert = SilentTransition()
skip_legal = SilentTransition()
skip_cultural = SilentTransition()
skip_condition = SilentTransition()
skip_risk = SilentTransition()
skip_insurance = SilentTransition()
skip_transport = SilentTransition()
skip_final = SilentTransition()

# Define the exclusive choices
initial_inspection_choice = OperatorPOWL(operator=Operator.XOR, children=[initial_inspection, skip_inspection])
material_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[material_testing, skip_test])
provenance_check_choice = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip_search])
expert_consult_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip_expert])
legal_review_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip_legal])
cultural_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[cultural_audit, skip_cultural])
condition_report_choice = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip_condition])
risk_assessment_choice = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, skip_risk])
insurance_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, skip_insurance])
transport_plan_choice = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, skip_transport])
final_certification_choice = OperatorPOWL(operator=Operator.XOR, children=[final_certification, skip_final])

# Define the loop nodes
loop_inspection = OperatorPOWL(operator=Operator.LOOP, children=[initial_inspection, material_testing, provenance_check, expert_consult, legal_review, cultural_audit, condition_report, risk_assessment, insurance_setup, transport_plan, final_certification])
loop_transport = OperatorPOWL(operator=Operator.LOOP, children=[final_certification, archive_entry, publication_prep])

# Define the partial order
root = StrictPartialOrder(nodes=[artifact_receipt, loop_inspection, loop_transport])
root.order.add_edge(artifact_receipt, initial_inspection_choice)
root.order.add_edge(initial_inspection_choice, loop_inspection)
root.order.add_edge(loop_inspection, final_certification_choice)
root.order.add_edge(final_certification_choice, loop_transport)
root.order.add_edge(loop_transport, archive_entry)
root.order.add_edge(loop_transport, publication_prep)