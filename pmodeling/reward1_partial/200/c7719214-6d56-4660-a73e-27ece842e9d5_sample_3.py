root = StrictPartialOrder(nodes=[
    Transition(label='Milk Sourcing'),
    Transition(label='Diet Monitoring'),
    Transition(label='Culture Selection'),
    Transition(label='Milk Pasteurize'),
    Transition(label='Curd Cutting'),
    Transition(label='Whey Draining'),
    Transition(label='Mold Inoculate'),
    Transition(label='Press Forming'),
    Transition(label='Salt Application'),
    Transition(label='Aging Setup'),
    Transition(label='Humidity Control'),
    Transition(label='Flavor Testing'),
    Transition(label='Packaging Design'),
    Transition(label='Order Processing'),
    Transition(label='Retail Delivery'),
    Transition(label='Event Coordination'),
    Transition(label='Feedback Review')
])

root.order.add_edge(Transition(label='Milk Sourcing'), Transition(label='Diet Monitoring'))
root.order.add_edge(Transition(label='Diet Monitoring'), Transition(label='Culture Selection'))
root.order.add_edge(Transition(label='Culture Selection'), Transition(label='Milk Pasteurize'))
root.order.add_edge(Transition(label='Milk Pasteurize'), Transition(label='Curd Cutting'))
root.order.add_edge(Transition(label='Curd Cutting'), Transition(label='Whey Draining'))
root.order.add_edge(Transition(label='Whey Draining'), Transition(label='Mold Inoculate'))
root.order.add_edge(Transition(label='Mold Inoculate'), Transition(label='Press Forming'))
root.order.add_edge(Transition(label='Press Forming'), Transition(label='Salt Application'))
root.order.add_edge(Transition(label='Salt Application'), Transition(label='Aging Setup'))
root.order.add_edge(Transition(label='Aging Setup'), Transition(label='Humidity Control'))
root.order.add_edge(Transition(label='Humidity Control'), Transition(label='Flavor Testing'))
root.order.add_edge(Transition(label='Flavor Testing'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Packaging Design'), Transition(label='Order Processing'))
root.order.add_edge(Transition(label='Order Processing'), Transition(label='Retail Delivery'))
root.order.add_edge(Transition(label='Retail Delivery'), Transition(label='Event Coordination'))
root.order.add_edge(Transition(label='Event Coordination'), Transition(label='Feedback Review'))