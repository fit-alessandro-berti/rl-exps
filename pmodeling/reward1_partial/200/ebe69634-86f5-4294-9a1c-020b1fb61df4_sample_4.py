from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
activities = {
    'Client Intake': Transition(label='Client Intake'),
    'Needs Analysis': Transition(label='Needs Analysis'),
    'Developer Match': Transition(label='Developer Match'),
    'Expert Vetting': Transition(label='Expert Vetting'),
    'Prototype Build': Transition(label='Prototype Build'),
    'Feedback Loop': Transition(label='Feedback Loop'),
    'Model Refinement': Transition(label='Model Refinement'),
    'License Draft': Transition(label='License Draft'),
    'IP Negotiation': Transition(label='IP Negotiation'),
    'Contract Sign': Transition(label='Contract Sign'),
    'Deployment Prep': Transition(label='Deployment Prep'),
    'Go Live': Transition(label='Go Live'),
    'Monitor Model': Transition(label='Monitor Model'),
    'Optimize AI': Transition(label='Optimize AI'),
    'Support Handoff': Transition(label='Support Handoff'),
    'Compliance Check': Transition(label='Compliance Check'),
    'Final Review': Transition(label='Final Review')
}

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        activities['Client Intake'],
        activities['Needs Analysis'],
        activities['Developer Match'],
        activities['Expert Vetting'],
        activities['Prototype Build'],
        activities['Feedback Loop'],
        activities['Model Refinement'],
        activities['License Draft'],
        activities['IP Negotiation'],
        activities['Contract Sign'],
        activities['Deployment Prep'],
        activities['Go Live'],
        activities['Monitor Model'],
        activities['Optimize AI'],
        activities['Support Handoff'],
        activities['Compliance Check'],
        activities['Final Review']
    ]
)

# Define the dependencies
root.order.add_edge(activities['Client Intake'], activities['Needs Analysis'])
root.order.add_edge(activities['Needs Analysis'], activities['Developer Match'])
root.order.add_edge(activities['Developer Match'], activities['Expert Vetting'])
root.order.add_edge(activities['Expert Vetting'], activities['Prototype Build'])
root.order.add_edge(activities['Prototype Build'], activities['Feedback Loop'])
root.order.add_edge(activities['Feedback Loop'], activities['Model Refinement'])
root.order.add_edge(activities['Model Refinement'], activities['License Draft'])
root.order.add_edge(activities['License Draft'], activities['IP Negotiation'])
root.order.add_edge(activities['IP Negotiation'], activities['Contract Sign'])
root.order.add_edge(activities['Contract Sign'], activities['Deployment Prep'])
root.order.add_edge(activities['Deployment Prep'], activities['Go Live'])
root.order.add_edge(activities['Go Live'], activities['Monitor Model'])
root.order.add_edge(activities['Monitor Model'], activities['Optimize AI'])
root.order.add_edge(activities['Optimize AI'], activities['Support Handoff'])
root.order.add_edge(activities['Support Handoff'], activities['Compliance Check'])
root.order.add_edge(activities['Compliance Check'], activities['Final Review'])