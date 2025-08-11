import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
provenance_check = Transition(label='Provenance Check')
material_testing = Transition(label='Material Testing')
stylistic_review = Transition(label='Stylistic Review')
expert_panel = Transition(label='Expert Panel')
legal_clearance = Transition(label='Legal Clearance')
ethics_audit = Transition(label='Ethics Audit')
insurance_quote = Transition(label='Insurance Quote')
risk_assess = Transition(label='Risk Assess')
digital_archive = Transition(label='Digital Archive')
replica_build = Transition(label='Replica Build')
transport_prep = Transition(label='Transport Prep')
final_review = Transition(label='Final Review')
catalog_entry = Transition(label='Catalog Entry')
public_notice = Transition(label='Public Notice')
condition_report = Transition(label='Condition Report')

# Define the transitions for silent activities
skip = SilentTransition()

# Define the loops and XORs
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_testing])
stylistic_loop = OperatorPOWL(operator=Operator.LOOP, children=[stylistic_review, expert_panel])
legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_clearance, ethics_audit])
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, insurance_quote])
digital_archive_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_archive, replica_build])
transport_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[transport_prep, final_review])

# Define the XORs
legal_ethics_xor = OperatorPOWL(operator=Operator.XOR, children=[legal_loop, ethics_audit])
risk_insurance_xor = OperatorPOWL(operator=Operator.XOR, children=[risk_loop, insurance_quote])
transport_final_xor = OperatorPOWL(operator=Operator.XOR, children=[transport_prep_loop, final_review])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    provenance_loop,
    stylistic_loop,
    legal_ethics_xor,
    risk_insurance_xor,
    transport_final_xor,
    digital_archive_loop,
    catalog_entry,
    public_notice,
    condition_report
])

# Define the dependencies
root.order.add_edge(provenance_loop, stylistic_loop)
root.order.add_edge(provenance_loop, legal_ethics_xor)
root.order.add_edge(provenance_loop, risk_insurance_xor)
root.order.add_edge(stylistic_loop, legal_ethics_xor)
root.order.add_edge(stylistic_loop, risk_insurance_xor)
root.order.add_edge(legal_ethics_xor, transport_final_xor)
root.order.add_edge(risk_insurance_xor, transport_final_xor)
root.order.add_edge(transport_final_xor, digital_archive_loop)
root.order.add_edge(digital_archive_loop, catalog_entry)
root.order.add_edge(catalog_entry, public_notice)
root.order.add_edge(public_notice, condition_report)

# Print the root POWL model
print(root)