root = StrictPartialOrder(nodes=[
    Transition(label='Initiate Audit'),
    Transition(label='Gather Documents'),
    Transition(label='Verify Suppliers'),
    Transition(label='Screen Transactions'),
    Transition(label='Classify Products'),
    Transition(label='Assess Risks'),
    Transition(label='Check Sanctions'),
    Transition(label='Review Tariffs'),
    Transition(label='Cross-Verify Data'),
    Transition(label='Conduct Interviews'),
    Transition(label='Analyze Reports'),
    Transition(label='Identify Gaps'),
    Transition(label='Recommend Actions'),
    Transition(label='Implement Changes'),
    Transition(label='Monitor Compliance'),
    Transition(label='Finalize Report')
])

root.order.add_edge(Transition(label='Initiate Audit'), Transition(label='Gather Documents'))
root.order.add_edge(Transition(label='Gather Documents'), Transition(label='Verify Suppliers'))
root.order.add_edge(Transition(label='Verify Suppliers'), Transition(label='Screen Transactions'))
root.order.add_edge(Transition(label='Screen Transactions'), Transition(label='Classify Products'))
root.order.add_edge(Transition(label='Classify Products'), Transition(label='Assess Risks'))
root.order.add_edge(Transition(label='Assess Risks'), Transition(label='Check Sanctions'))
root.order.add_edge(Transition(label='Check Sanctions'), Transition(label='Review Tariffs'))
root.order.add_edge(Transition(label='Review Tariffs'), Transition(label='Cross-Verify Data'))
root.order.add_edge(Transition(label='Cross-Verify Data'), Transition(label='Conduct Interviews'))
root.order.add_edge(Transition(label='Conduct Interviews'), Transition(label='Analyze Reports'))
root.order.add_edge(Transition(label='Analyze Reports'), Transition(label='Identify Gaps'))
root.order.add_edge(Transition(label='Identify Gaps'), Transition(label='Recommend Actions'))
root.order.add_edge(Transition(label='Recommend Actions'), Transition(label='Implement Changes'))
root.order.add_edge(Transition(label='Implement Changes'), Transition(label='Monitor Compliance'))
root.order.add_edge(Transition(label='Monitor Compliance'), Transition(label='Finalize Report'))