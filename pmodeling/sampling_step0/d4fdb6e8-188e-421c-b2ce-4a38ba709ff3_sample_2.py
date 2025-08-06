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
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()

# Define the partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, provenance_check, digital_imaging, database_search, expert_consult, legal_review, cultural_audit, condition_report, risk_assessment, insurance_setup, transport_plan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[artifact_receipt, initial_inspection, loop1])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[final_certification, skip1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[archive_entry, skip2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[publication_prep, skip3])
root = StrictPartialOrder(nodes=[loop2, xor1, xor2, xor3])
root.order.add_edge(loop2, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop2, xor3)