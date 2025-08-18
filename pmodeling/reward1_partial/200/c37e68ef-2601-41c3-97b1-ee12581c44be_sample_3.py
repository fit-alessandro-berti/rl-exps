root = StrictPartialOrder(nodes=[
    Transition(label='Milk Sourcing'),
    Transition(label='Quality Testing'),
    Transition(label='Starter Prep'),
    Transition(label='Curd Cutting'),
    Transition(label='Whey Draining'),
    Transition(label='Molding Press'),
    Transition(label='Fermentation Control'),
    Transition(label='Aging Setup'),
    Transition(label='Humidity Check'),
    Transition(label='Packaging Design'),
    Transition(label='Label Approval'),
    Transition(label='Inventory Audit'),
    Transition(label='Order Scheduling'),
    Transition(label='Market Delivery'),
    Transition(label='Feedback Review'),
    Transition(label='Compliance Check'),
    Transition(label='Marketing Sync')
])

root.order.add_edge(Transition(label='Milk Sourcing'), Transition(label='Quality Testing'))
root.order.add_edge(Transition(label='Quality Testing'), Transition(label='Starter Prep'))
root.order.add_edge(Transition(label='Starter Prep'), Transition(label='Curd Cutting'))
root.order.add_edge(Transition(label='Curd Cutting'), Transition(label='Whey Draining'))
root.order.add_edge(Transition(label='Whey Draining'), Transition(label='Molding Press'))
root.order.add_edge(Transition(label='Molding Press'), Transition(label='Fermentation Control'))
root.order.add_edge(Transition(label='Fermentation Control'), Transition(label='Aging Setup'))
root.order.add_edge(Transition(label='Aging Setup'), Transition(label='Humidity Check'))
root.order.add_edge(Transition(label='Humidity Check'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Packaging Design'), Transition(label='Label Approval'))
root.order.add_edge(Transition(label='Label Approval'), Transition(label='Inventory Audit'))
root.order.add_edge(Transition(label='Inventory Audit'), Transition(label='Order Scheduling'))
root.order.add_edge(Transition(label='Order Scheduling'), Transition(label='Market Delivery'))
root.order.add_edge(Transition(label='Market Delivery'), Transition(label='Feedback Review'))
root.order.add_edge(Transition(label='Feedback Review'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Marketing Sync'))