from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define transitions
xor1 = OperatorPOWL(operator=Operator.XOR, children=[material_testing, initial_inspection])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, digital_imaging])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[database_search, expert_consult])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, cultural_audit])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, risk_assessment])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, transport_plan])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[final_certification, archive_entry])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[publication_prep, xor1, xor2, xor3, xor4, xor5, xor6, xor7])

# Create root
root = StrictPartialOrder(nodes=[xor8])
root.order.add_edge(xor8, xor1)
root.order.add_edge(xor8, xor2)
root.order.add_edge(xor8, xor3)
root.order.add_edge(xor8, xor4)
root.order.add_edge(xor8, xor5)
root.order.add_edge(xor8, xor6)
root.order.add_edge(xor8, xor7)