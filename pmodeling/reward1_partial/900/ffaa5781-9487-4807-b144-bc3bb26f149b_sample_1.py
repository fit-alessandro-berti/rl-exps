import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL transitions
provenance_check = Transition(label='Provenance Check')
radiocarbon_test = Transition(label='Radiocarbon Test')
material_analysis = Transition(label='Material Analysis')
microscopic_scan = Transition(label='Microscopic Scan')
expert_review = Transition(label='Expert Review')
context_validation = Transition(label='Context Validation')
legal_audit = Transition(label='Legal Audit')
export_verify = Transition(label='Export Verify')
digital_imaging = Transition(label='Digital Imaging')
three_d_modeling = Transition(label='3D Modeling')
consensus_meeting = Transition(label='Consensus Meeting')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')
virtual_setup = Transition(label='Virtual Setup')
archival_backup = Transition(label='Archival Backup')

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, export_verify])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[context_validation, expert_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[three_d_modeling, digital_imaging])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[virtual_setup, archival_backup])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, final_approval])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[provenance_check, radiocarbon_test, material_analysis, microscopic_scan, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(provenance_check, radiocarbon_test)
root.order.add_edge(radiocarbon_test, material_analysis)
root.order.add_edge(material_analysis, microscopic_scan)
root.order.add_edge(microscopic_scan, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, final_approval)
root.order.add_edge(final_approval, catalog_entry)
root.order.add_edge(catalog_entry, virtual_setup)
root.order.add_edge(virtual_setup, archival_backup)