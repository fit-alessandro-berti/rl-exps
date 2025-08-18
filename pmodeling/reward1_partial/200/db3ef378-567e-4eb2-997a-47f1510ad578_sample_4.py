root = StrictPartialOrder(nodes=[
    Transition(label='Milk Collection'),
    Transition(label='Culture Prep'),
    Transition(label='Curd Formation'),
    Transition(label='Whey Separation'),
    Transition(label='Molding Cheese'),
    Transition(label='Salting Process'),
    Transition(label='Initial Aging'),
    Transition(label='Humidity Control'),
    Transition(label='Temperature Check'),
    Transition(label='Flavor Testing'),
    Transition(label='Final Aging'),
    Transition(label='Packaging Artisanal'),
    Transition(label='Label Printing'),
    Transition(label='Inventory Audit'),
    Transition(label='Order Fulfillment'),
    Transition(label='Subscription Setup'),
    Transition(label='Event Marketing')
])

root.order.add_edge(Transition(label='Milk Collection'), Transition(label='Culture Prep'))
root.order.add_edge(Transition(label='Culture Prep'), Transition(label='Curd Formation'))
root.order.add_edge(Transition(label='Curd Formation'), Transition(label='Whey Separation'))
root.order.add_edge(Transition(label='Whey Separation'), Transition(label='Molding Cheese'))
root.order.add_edge(Transition(label='Molding Cheese'), Transition(label='Salting Process'))
root.order.add_edge(Transition(label='Salting Process'), Transition(label='Initial Aging'))
root.order.add_edge(Transition(label='Initial Aging'), Transition(label='Humidity Control'))
root.order.add_edge(Transition(label='Humidity Control'), Transition(label='Temperature Check'))
root.order.add_edge(Transition(label='Temperature Check'), Transition(label='Flavor Testing'))
root.order.add_edge(Transition(label='Flavor Testing'), Transition(label='Final Aging'))
root.order.add_edge(Transition(label='Final Aging'), Transition(label='Packaging Artisanal'))
root.order.add_edge(Transition(label='Packaging Artisanal'), Transition(label='Label Printing'))
root.order.add_edge(Transition(label='Label Printing'), Transition(label='Inventory Audit'))
root.order.add_edge(Transition(label='Inventory Audit'), Transition(label='Order Fulfillment'))
root.order.add_edge(Transition(label='Order Fulfillment'), Transition(label='Subscription Setup'))
root.order.add_edge(Transition(label='Subscription Setup'), Transition(label='Event Marketing'))