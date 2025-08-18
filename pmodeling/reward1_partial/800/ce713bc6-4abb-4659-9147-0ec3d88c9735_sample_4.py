import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
activities = ['Initial Inquiry', 'Document Review', 'Historical Research', 'Material Sampling', 'Forensic Testing', 'Ownership Audit', 'Legal Verification', 'Ethical Screening', 'Expert Consultation', 'Cultural Assessment', 'Condition Survey', 'Provenance Mapping', 'Risk Analysis', 'Report Compilation', 'Acquisition Approval', 'Repatriation Review', 'Archival Storage']
transitions = [Transition(label=activity) for activity in activities]

# Define the POWL model
root = StrictPartialOrder(nodes=transitions)

# Add edges to represent the process flow
root.order.add_edge(transitions[0], transitions[1])
root.order.add_edge(transitions[1], transitions[2])
root.order.add_edge(transitions[2], transitions[3])
root.order.add_edge(transitions[3], transitions[4])
root.order.add_edge(transitions[4], transitions[5])
root.order.add_edge(transitions[5], transitions[6])
root.order.add_edge(transitions[6], transitions[7])
root.order.add_edge(transitions[7], transitions[8])
root.order.add_edge(transitions[8], transitions[9])
root.order.add_edge(transitions[9], transitions[10])
root.order.add_edge(transitions[10], transitions[11])
root.order.add_edge(transitions[11], transitions[12])
root.order.add_edge(transitions[12], transitions[13])
root.order.add_edge(transitions[13], transitions[14])
root.order.add_edge(transitions[14], transitions[15])
root.order.add_edge(transitions[15], transitions[16])

print(root)