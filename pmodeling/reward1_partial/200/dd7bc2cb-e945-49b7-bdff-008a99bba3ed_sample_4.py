root = StrictPartialOrder(nodes=[
    Transition(label='Farm Select'),
    Transition(label='Milk Test'),
    Transition(label='Milk Pasteurize'),
    Transition(label='Curd Form'),
    Transition(label='Whey Drain'),
    Transition(label='Cheese Press'),
    Transition(label='Salt Rub'),
    Transition(label='Aging Set'),
    Transition(label='Flavor Check'),
    Transition(label='Texture Scan'),
    Transition(label='Quality Approve'),
    Transition(label='Custom Pack'),
    Transition(label='Cold Ship'),
    Transition(label='Retail Train'),
    Transition(label='Feedback Log'),
    Transition(label='Batch Adjust')
])

root.order.add_edge(Transition(label='Farm Select'), Transition(label='Milk Test'))
root.order.add_edge(Transition(label='Milk Test'), Transition(label='Milk Pasteurize'))
root.order.add_edge(Transition(label='Milk Pasteurize'), Transition(label='Curd Form'))
root.order.add_edge(Transition(label='Curd Form'), Transition(label='Whey Drain'))
root.order.add_edge(Transition(label='Whey Drain'), Transition(label='Cheese Press'))
root.order.add_edge(Transition(label='Cheese Press'), Transition(label='Salt Rub'))
root.order.add_edge(Transition(label='Salt Rub'), Transition(label='Aging Set'))
root.order.add_edge(Transition(label='Aging Set'), Transition(label='Flavor Check'))
root.order.add_edge(Transition(label='Flavor Check'), Transition(label='Texture Scan'))
root.order.add_edge(Transition(label='Texture Scan'), Transition(label='Quality Approve'))
root.order.add_edge(Transition(label='Quality Approve'), Transition(label='Custom Pack'))
root.order.add_edge(Transition(label='Custom Pack'), Transition(label='Cold Ship'))
root.order.add_edge(Transition(label='Cold Ship'), Transition(label='Retail Train'))
root.order.add_edge(Transition(label='Retail Train'), Transition(label='Feedback Log'))
root.order.add_edge(Transition(label='Feedback Log'), Transition(label='Batch Adjust'))