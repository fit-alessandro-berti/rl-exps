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

# Define silent transitions
skip = SilentTransition()

# Define sub-workflows
initial_workflow = OperatorPOWL(operator=Operator.XOR, children=[artifact_receipt, initial_inspection])
material_workflow = OperatorPOWL(operator=Operator.XOR, children=[material_testing, provenance_check])
digital_workflow = OperatorPOWL(operator=Operator.XOR, children=[digital_imaging, database_search])
expert_workflow = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, legal_review])
cultural_workflow = OperatorPOWL(operator=Operator.XOR, children=[cultural_audit, condition_report])
risk_workflow = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, insurance_setup])
transport_workflow = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, final_certification])
archive_workflow = OperatorPOWL(operator=Operator.XOR, children=[archive_entry, publication_prep])

# Define the main workflow
root = StrictPartialOrder(nodes=[initial_workflow, material_workflow, digital_workflow, expert_workflow, cultural_workflow, risk_workflow, transport_workflow, archive_workflow])
root.order.add_edge(initial_workflow, material_workflow)
root.order.add_edge(material_workflow, digital_workflow)
root.order.add_edge(digital_workflow, expert_workflow)
root.order.add_edge(expert_workflow, cultural_workflow)
root.order.add_edge(cultural_workflow, risk_workflow)
root.order.add_edge(risk_workflow, transport_workflow)
root.order.add_edge(transport_workflow, archive_workflow)

print(root)