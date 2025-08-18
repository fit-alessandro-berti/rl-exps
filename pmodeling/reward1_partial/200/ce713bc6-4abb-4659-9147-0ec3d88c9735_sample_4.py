import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
activities = [Transition(label=activity) for activity in ['Initial Inquiry', 'Document Review', 'Historical Research', 'Material Sampling', 'Forensic Testing', 'Ownership Audit', 'Legal Verification', 'Ethical Screening', 'Expert Consultation', 'Cultural Assessment', 'Condition Survey', 'Provenance Mapping', 'Risk Analysis', 'Report Compilation', 'Acquisition Approval', 'Repatriation Review', 'Archival Storage']]

# Define the process as a StrictPartialOrder
root = StrictPartialOrder(nodes=activities)

# Define the order of activities (dependencies)
root.order.add_edge(activities[0], activities[1])
root.order.add_edge(activities[1], activities[2])
root.order.add_edge(activities[2], activities[3])
root.order.add_edge(activities[3], activities[4])
root.order.add_edge(activities[4], activities[5])
root.order.add_edge(activities[5], activities[6])
root.order.add_edge(activities[6], activities[7])
root.order.add_edge(activities[7], activities[8])
root.order.add_edge(activities[8], activities[9])
root.order.add_edge(activities[9], activities[10])
root.order.add_edge(activities[10], activities[11])
root.order.add_edge(activities[11], activities[12])
root.order.add_edge(activities[12], activities[13])
root.order.add_edge(activities[13], activities[14])
root.order.add_edge(activities[14], activities[15])
root.order.add_edge(activities[15], activities[16])
root.order.add_edge(activities[16], activities[17])

print(root)