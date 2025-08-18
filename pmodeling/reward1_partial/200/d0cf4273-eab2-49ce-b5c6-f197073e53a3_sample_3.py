root = StrictPartialOrder(nodes=[
    Transition('Material Sourcing'),
    Transition('Cultural Verify'),
    Transition('Eco Transport'),
    Transition('Batch Storytelling'),
    Transition('Craftsman Assignment'),
    Transition('Product Creation'),
    Transition('Provenance Catalog'),
    Transition('Community Marketing'),
    Transition('Collector Targeting'),
    Transition('Package Assembly'),
    Transition('Local Cooperatives'),
    Transition('Environmental Audit'),
    Transition('Ethical Logistics'),
    Transition('Global Shipping'),
    Transition('Feedback Collection')
])

root.order.add_edge(Transition('Material Sourcing'), Transition('Cultural Verify'))
root.order.add_edge(Transition('Cultural Verify'), Transition('Eco Transport'))
root.order.add_edge(Transition('Eco Transport'), Transition('Batch Storytelling'))
root.order.add_edge(Transition('Batch Storytelling'), Transition('Craftsman Assignment'))
root.order.add_edge(Transition('Craftsman Assignment'), Transition('Product Creation'))
root.order.add_edge(Transition('Product Creation'), Transition('Provenance Catalog'))
root.order.add_edge(Transition('Provenance Catalog'), Transition('Community Marketing'))
root.order.add_edge(Transition('Community Marketing'), Transition('Collector Targeting'))
root.order.add_edge(Transition('Collector Targeting'), Transition('Package Assembly'))
root.order.add_edge(Transition('Package Assembly'), Transition('Local Cooperatives'))
root.order.add_edge(Transition('Local Cooperatives'), Transition('Environmental Audit'))
root.order.add_edge(Transition('Environmental Audit'), Transition('Ethical Logistics'))
root.order.add_edge(Transition('Ethical Logistics'), Transition('Global Shipping'))
root.order.add_edge(Transition('Global Shipping'), Transition('Feedback Collection'))