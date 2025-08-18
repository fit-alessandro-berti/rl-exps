root = StrictPartialOrder(nodes=[
    Transition(label='Milk Sourcing'),
    Transition(label='Culture Prep'),
    Transition(label='Milk Pasteurize'),
    Transition(label='Milk Inoculate'),
    Transition(label='Curd Formation'),
    Transition(label='Curd Cut'),
    Transition(label='Whey Drain'),
    Transition(label='Mold Inoculate'),
    Transition(label='Press Cheese'),
    Transition(label='Aging Setup'),
    Transition(label='Humidity Control'),
    Transition(label='Temperature Monitor'),
    Transition(label='Quality Test'),
    Transition(label='Packaging'),
    Transition(label='Order Fulfill'),
    Transition(label='Retail Deliver'),
    Transition(label='Feedback Collect')
])

root.order.add_edge(Transition(label='Milk Sourcing'), Transition(label='Culture Prep'))
root.order.add_edge(Transition(label='Culture Prep'), Transition(label='Milk Pasteurize'))
root.order.add_edge(Transition(label='Milk Pasteurize'), Transition(label='Milk Inoculate'))
root.order.add_edge(Transition(label='Milk Inoculate'), Transition(label='Curd Formation'))
root.order.add_edge(Transition(label='Curd Formation'), Transition(label='Curd Cut'))
root.order.add_edge(Transition(label='Curd Cut'), Transition(label='Whey Drain'))
root.order.add_edge(Transition(label='Whey Drain'), Transition(label='Mold Inoculate'))
root.order.add_edge(Transition(label='Mold Inoculate'), Transition(label='Press Cheese'))
root.order.add_edge(Transition(label='Press Cheese'), Transition(label='Aging Setup'))
root.order.add_edge(Transition(label='Aging Setup'), Transition(label='Humidity Control'))
root.order.add_edge(Transition(label='Humidity Control'), Transition(label='Temperature Monitor'))
root.order.add_edge(Transition(label='Temperature Monitor'), Transition(label='Quality Test'))
root.order.add_edge(Transition(label='Quality Test'), Transition(label='Packaging'))
root.order.add_edge(Transition(label='Packaging'), Transition(label='Order Fulfill'))
root.order.add_edge(Transition(label='Order Fulfill'), Transition(label='Retail Deliver'))
root.order.add_edge(Transition(label='Retail Deliver'), Transition(label='Feedback Collect'))