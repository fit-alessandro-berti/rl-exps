root = StrictPartialOrder(nodes=[
    Transition(label='Milk Sourcing'),
    Transition(label='Quality Testing'),
    Transition(label='Milk Pasteurize'),
    Transition(label='Culture Inoculate'),
    Transition(label='Coagulation'),
    Transition(label='Curd Cutting'),
    Transition(label='Whey Drain'),
    Transition(label='Pressing'),
    Transition(label='Salting'),
    Transition(label='Aging Control'),
    Transition(label='Sensory Audit'),
    Transition(label='Packaging Design'),
    Transition(label='Label Approval'),
    Transition(label='Order Customization'),
    Transition(label='Logistics Plan'),
    Transition(label='Market Delivery'),
    Transition(label='Customer Feedback'),
    Transition(label='Regulatory Check')
])

# Define the edges based on the dependencies
root.order.add_edge(Transition(label='Milk Sourcing'), Transition(label='Quality Testing'))
root.order.add_edge(Transition(label='Quality Testing'), Transition(label='Milk Pasteurize'))
root.order.add_edge(Transition(label='Milk Pasteurize'), Transition(label='Culture Inoculate'))
root.order.add_edge(Transition(label='Culture Inoculate'), Transition(label='Coagulation'))
root.order.add_edge(Transition(label='Coagulation'), Transition(label='Curd Cutting'))
root.order.add_edge(Transition(label='Curd Cutting'), Transition(label='Whey Drain'))
root.order.add_edge(Transition(label='Whey Drain'), Transition(label='Pressing'))
root.order.add_edge(Transition(label='Pressing'), Transition(label='Salting'))
root.order.add_edge(Transition(label='Salting'), Transition(label='Aging Control'))
root.order.add_edge(Transition(label='Aging Control'), Transition(label='Sensory Audit'))
root.order.add_edge(Transition(label='Sensory Audit'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Packaging Design'), Transition(label='Label Approval'))
root.order.add_edge(Transition(label='Label Approval'), Transition(label='Order Customization'))
root.order.add_edge(Transition(label='Order Customization'), Transition(label='Logistics Plan'))
root.order.add_edge(Transition(label='Logistics Plan'), Transition(label='Market Delivery'))
root.order.add_edge(Transition(label='Market Delivery'), Transition(label='Customer Feedback'))
root.order.add_edge(Transition(label='Customer Feedback'), Transition(label='Regulatory Check'))