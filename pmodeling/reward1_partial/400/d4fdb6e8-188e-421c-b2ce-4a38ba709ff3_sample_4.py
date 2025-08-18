import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
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

# Define silent transitions for the loop
skip = SilentTransition()

# Define the loop node for risk assessment and insurance setup
loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assessment, insurance_setup])

# Define the exclusive choice node for cultural audit and condition report
xor = OperatorPOWL(operator=Operator.XOR, children=[cultural_audit, condition_report])

# Define the exclusive choice node for expert consultation and legal review
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, legal_review])

# Define the exclusive choice node for material testing and database search
xor3 = OperatorPOWL(operator=Operator.XOR, children=[material_testing, database_search])

# Define the exclusive choice node for initial inspection and digital imaging
xor4 = OperatorPOWL(operator=Operator.XOR, children=[initial_inspection, digital_imaging])

# Define the strict partial order for the entire process
root = StrictPartialOrder(nodes=[artifact_receipt, xor4, xor3, xor2, xor, loop, final_certification, archive_entry, publication_prep])

# Define the order dependencies
root.order.add_edge(artifact_receipt, xor4)
root.order.add_edge(xor4, xor3)
root.order.add_edge(xor3, xor2)
root.order.add_edge(xor2, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, final_certification)
root.order.add_edge(final_certification, archive_entry)
root.order.add_edge(archive_entry, publication_prep)

print(root)