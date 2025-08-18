from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Initiate Audit': Transition(label='Initiate Audit'),
    'Gather Documents': Transition(label='Gather Documents'),
    'Verify Suppliers': Transition(label='Verify Suppliers'),
    'Screen Transactions': Transition(label='Screen Transactions'),
    'Classify Products': Transition(label='Classify Products'),
    'Assess Risks': Transition(label='Assess Risks'),
    'Check Sanctions': Transition(label='Check Sanctions'),
    'Review Tariffs': Transition(label='Review Tariffs'),
    'Cross-Verify Data': Transition(label='Cross-Verify Data'),
    'Conduct Interviews': Transition(label='Conduct Interviews'),
    'Analyze Reports': Transition(label='Analyze Reports'),
    'Identify Gaps': Transition(label='Identify Gaps'),
    'Recommend Actions': Transition(label='Recommend Actions'),
    'Implement Changes': Transition(label='Implement Changes'),
    'Monitor Compliance': Transition(label='Monitor Compliance'),
    'Finalize Report': Transition(label='Finalize Report')
}

# Define the process structure
audit_process = StrictPartialOrder(
    nodes=[
        activities['Initiate Audit'],
        activities['Gather Documents'],
        activities['Verify Suppliers'],
        activities['Screen Transactions'],
        activities['Classify Products'],
        activities['Assess Risks'],
        activities['Check Sanctions'],
        activities['Review Tariffs'],
        activities['Cross-Verify Data'],
        activities['Conduct Interviews'],
        activities['Analyze Reports'],
        activities['Identify Gaps'],
        activities['Recommend Actions'],
        activities['Implement Changes'],
        activities['Monitor Compliance'],
        activities['Finalize Report']
    ]
)

# Define the dependencies
audit_process.order.add_edge(activities['Initiate Audit'], activities['Gather Documents'])
audit_process.order.add_edge(activities['Gather Documents'], activities['Verify Suppliers'])
audit_process.order.add_edge(activities['Verify Suppliers'], activities['Screen Transactions'])
audit_process.order.add_edge(activities['Screen Transactions'], activities['Classify Products'])
audit_process.order.add_edge(activities['Classify Products'], activities['Assess Risks'])
audit_process.order.add_edge(activities['Assess Risks'], activities['Check Sanctions'])
audit_process.order.add_edge(activities['Check Sanctions'], activities['Review Tariffs'])
audit_process.order.add_edge(activities['Review Tariffs'], activities['Cross-Verify Data'])
audit_process.order.add_edge(activities['Cross-Verify Data'], activities['Conduct Interviews'])
audit_process.order.add_edge(activities['Conduct Interviews'], activities['Analyze Reports'])
audit_process.order.add_edge(activities['Analyze Reports'], activities['Identify Gaps'])
audit_process.order.add_edge(activities['Identify Gaps'], activities['Recommend Actions'])
audit_process.order.add_edge(activities['Recommend Actions'], activities['Implement Changes'])
audit_process.order.add_edge(activities['Implement Changes'], activities['Monitor Compliance'])
audit_process.order.add_edge(activities['Monitor Compliance'], activities['Finalize Report'])

root = audit_process
print(root)