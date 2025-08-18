root = StrictPartialOrder(nodes=[
    Transition(label='Milk Sourcing'),
    Transition(label='Culture Selection'),
    Transition(label='Milk Testing'),
    Transition(label='Fermentation Start'),
    Transition(label='Temperature Control'),
    Transition(label='pH Monitoring'),
    Transition(label='Curd Cutting'),
    Transition(label='Whey Draining'),
    Transition(label='Molding Cheese'),
    Transition(label='Salting Process'),
    Transition(label='Aging Setup'),
    Transition(label='Quality Check'),
    Transition(label='Packaging Prep'),
    Transition(label='Label Design'),
    Transition(label='Distribution Plan'),
    Transition(label='Retail Delivery'),
    Transition(label='Customer Feedback')
])
root.order.add_edge(Transition(label='Milk Sourcing'), Transition(label='Culture Selection'))
root.order.add_edge(Transition(label='Culture Selection'), Transition(label='Milk Testing'))
root.order.add_edge(Transition(label='Milk Testing'), Transition(label='Fermentation Start'))
root.order.add_edge(Transition(label='Fermentation Start'), Transition(label='Temperature Control'))
root.order.add_edge(Transition(label='Temperature Control'), Transition(label='pH Monitoring'))
root.order.add_edge(Transition(label='pH Monitoring'), Transition(label='Curd Cutting'))
root.order.add_edge(Transition(label='Curd Cutting'), Transition(label='Whey Draining'))
root.order.add_edge(Transition(label='Whey Draining'), Transition(label='Molding Cheese'))
root.order.add_edge(Transition(label='Molding Cheese'), Transition(label='Salting Process'))
root.order.add_edge(Transition(label='Salting Process'), Transition(label='Aging Setup'))
root.order.add_edge(Transition(label='Aging Setup'), Transition(label='Quality Check'))
root.order.add_edge(Transition(label='Quality Check'), Transition(label='Packaging Prep'))
root.order.add_edge(Transition(label='Packaging Prep'), Transition(label='Label Design'))
root.order.add_edge(Transition(label='Label Design'), Transition(label='Distribution Plan'))
root.order.add_edge(Transition(label='Distribution Plan'), Transition(label='Retail Delivery'))
root.order.add_edge(Transition(label='Retail Delivery'), Transition(label='Customer Feedback'))