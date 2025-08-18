root = StrictPartialOrder(nodes=[
    Transition(label='Farm Selection'),
    Transition(label='Milk Testing'),
    Transition(label='Starter Culture'),
    Transition(label='Curd Formation'),
    Transition(label='Pressing Cheese'),
    Transition(label='Microbial Profiling'),
    Transition(label='Aging Control'),
    Transition(label='Hand Wrapping'),
    Transition(label='Quality Audit'),
    Transition(label='Packaging Prep'),
    Transition(label='Climate Shipping'),
    Transition(label='Retail Coordination'),
    Transition(label='Seasonal Review'),
    Transition(label='Consumer Survey'),
    Transition(label='Feedback Analysis'),
    Transition(label='Market Adjustment')
])

root.order.add_edge(Transition(label='Farm Selection'), Transition(label='Milk Testing'))
root.order.add_edge(Transition(label='Milk Testing'), Transition(label='Starter Culture'))
root.order.add_edge(Transition(label='Starter Culture'), Transition(label='Curd Formation'))
root.order.add_edge(Transition(label='Curd Formation'), Transition(label='Pressing Cheese'))
root.order.add_edge(Transition(label='Pressing Cheese'), Transition(label='Microbial Profiling'))
root.order.add_edge(Transition(label='Microbial Profiling'), Transition(label='Aging Control'))
root.order.add_edge(Transition(label='Aging Control'), Transition(label='Hand Wrapping'))
root.order.add_edge(Transition(label='Hand Wrapping'), Transition(label='Quality Audit'))
root.order.add_edge(Transition(label='Quality Audit'), Transition(label='Packaging Prep'))
root.order.add_edge(Transition(label='Packaging Prep'), Transition(label='Climate Shipping'))
root.order.add_edge(Transition(label='Climate Shipping'), Transition(label='Retail Coordination'))
root.order.add_edge(Transition(label='Retail Coordination'), Transition(label='Seasonal Review'))
root.order.add_edge(Transition(label='Seasonal Review'), Transition(label='Consumer Survey'))
root.order.add_edge(Transition(label='Consumer Survey'), Transition(label='Feedback Analysis'))
root.order.add_edge(Transition(label='Feedback Analysis'), Transition(label='Market Adjustment'))