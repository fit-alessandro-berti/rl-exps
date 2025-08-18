import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their names
transitions = {
    'Initial Review': Transition(label='Initial Review'),
    'Provenance Check': Transition(label='Provenance Check'),
    'Material Scan': Transition(label='Material Scan'),
    'Chemical Test': Transition(label='Chemical Test'),
    'Imaging Capture': Transition(label='Imaging Capture'),
    'Expert Consult': Transition(label='Expert Consult'),
    'Historical Match': Transition(label='Historical Match'),
    'Forgery Detect': Transition(label='Forgery Detect'),
    'Documentation Verify': Transition(label='Documentation Verify'),
    'Cross-Border Check': Transition(label='Cross-Border Check'),
    'Condition Assess': Transition(label='Condition Assess'),
    'Value Estimate': Transition(label='Value Estimate'),
    'Report Draft': Transition(label='Report Draft'),
    'Report Review': Transition(label='Report Review'),
    'Client Approval': Transition(label='Client Approval'),
    'Certification Issue': Transition(label='Certification Issue'),
    'Archive Record': Transition(label='Archive Record')
}

# Define the root of the POWL model
root = StrictPartialOrder()

# Add transitions to the root
for transition_name, transition in transitions.items():
    root.add_transition(transition)

# Define the control flow between transitions
# Define the control flow between transitions
root.add_edge(transitions['Initial Review'], transitions['Provenance Check'])
root.add_edge(transitions['Provenance Check'], transitions['Material Scan'])
root.add_edge(transitions['Material Scan'], transitions['Chemical Test'])
root.add_edge(transitions['Chemical Test'], transitions['Imaging Capture'])
root.add_edge(transitions['Imaging Capture'], transitions['Expert Consult'])
root.add_edge(transitions['Expert Consult'], transitions['Historical Match'])
root.add_edge(transitions['Historical Match'], transitions['Forgery Detect'])
root.add_edge(transitions['Forgery Detect'], transitions['Documentation Verify'])
root.add_edge(transitions['Documentation Verify'], transitions['Cross-Border Check'])
root.add_edge(transitions['Cross-Border Check'], transitions['Condition Assess'])
root.add_edge(transitions['Condition Assess'], transitions['Value Estimate'])
root.add_edge(transitions['Value Estimate'], transitions['Report Draft'])
root.add_edge(transitions['Report Draft'], transitions['Report Review'])
root.add_edge(transitions['Report Review'], transitions['Client Approval'])
root.add_edge(transitions['Client Approval'], transitions['Certification Issue'])
root.add_edge(transitions['Certification Issue'], transitions['Archive Record'])

# Print the root POWL model
print(root)