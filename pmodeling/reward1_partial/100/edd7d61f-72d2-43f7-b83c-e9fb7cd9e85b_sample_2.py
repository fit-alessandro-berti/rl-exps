from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities with their labels
activities = {
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

# Create the POWL model
root = StrictPartialOrder(nodes=[
    activities['Initial Review'],
    activities['Provenance Check'],
    activities['Material Scan'],
    activities['Chemical Test'],
    activities['Imaging Capture'],
    activities['Expert Consult'],
    activities['Historical Match'],
    activities['Forgery Detect'],
    activities['Documentation Verify'],
    activities['Cross-Border Check'],
    activities['Condition Assess'],
    activities['Value Estimate'],
    activities['Report Draft'],
    activities['Report Review'],
    activities['Client Approval'],
    activities['Certification Issue'],
    activities['Archive Record']
])

# Define the dependencies between activities
root.order.add_edge(activities['Initial Review'], activities['Provenance Check'])
root.order.add_edge(activities['Provenance Check'], activities['Material Scan'])
root.order.add_edge(activities['Material Scan'], activities['Chemical Test'])
root.order.add_edge(activities['Chemical Test'], activities['Imaging Capture'])
root.order.add_edge(activities['Imaging Capture'], activities['Expert Consult'])
root.order.add_edge(activities['Expert Consult'], activities['Historical Match'])
root.order.add_edge(activities['Historical Match'], activities['Forgery Detect'])
root.order.add_edge(activities['Forgery Detect'], activities['Documentation Verify'])
root.order.add_edge(activities['Documentation Verify'], activities['Cross-Border Check'])
root.order.add_edge(activities['Cross-Border Check'], activities['Condition Assess'])
root.order.add_edge(activities['Condition Assess'], activities['Value Estimate'])
root.order.add_edge(activities['Value Estimate'], activities['Report Draft'])
root.order.add_edge(activities['Report Draft'], activities['Report Review'])
root.order.add_edge(activities['Report Review'], activities['Client Approval'])
root.order.add_edge(activities['Client Approval'], activities['Certification Issue'])
root.order.add_edge(activities['Certification Issue'], activities['Archive Record'])

print(root)