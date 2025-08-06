import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Provenance Check', 'Material Testing', 'Stylistic Review', 'Expert Panel',
              'Legal Clearance', 'Ethics Audit', 'Insurance Quote', 'Risk Assess',
              'Digital Archive', 'Replica Build', 'Transport Prep', 'Final Review',
              'Catalog Entry', 'Public Notice', 'Condition Report']

# Create the transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Create the nodes for the POWL model
provenance_check = transitions[0]
material_testing = transitions[1]
stylistic_review = transitions[2]
expert_panel = transitions[3]
legal_clearance = transitions[4]
ethics_audit = transitions[5]
insurance_quote = transitions[6]
risk_assess = transitions[7]
digital_archive = transitions[8]
replica_build = transitions[9]
transport_prep = transitions[10]
final_review = transitions[11]
catalog_entry = transitions[12]
public_notice = transitions[13]
condition_report = transitions[14]

# Create the operators for the POWL model
xor = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, ethics_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[insurance_quote, risk_assess])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[digital_archive, replica_build])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[transport_prep, final_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, public_notice])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, xor5])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[xor6, xor4])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[xor7, xor3])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[xor8, xor2])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[xor9, xor])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[xor10])
root.order.add_edge(xor10, xor9)
root.order.add_edge(xor9, xor8)
root.order.add_edge(xor8, xor7)
root.order.add_edge(xor7, xor6)
root.order.add_edge(xor6, xor5)
root.order.add_edge(xor5, xor4)
root.order.add_edge(xor4, xor3)
root.order.add_edge(xor3, xor2)
root.order.add_edge(xor2, xor)
root.order.add_edge(xor, xor10)