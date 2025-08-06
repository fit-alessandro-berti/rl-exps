root = StrictPartialOrder(nodes=[
    Transition(label='Milk Collection'),
    Transition(label='Quality Testing'),
    Transition(label='Milk Blending'),
    Transition(label='Starter Culture'),
    Transition(label='Fermentation Check'),
    Transition(label='Curd Cutting'),
    Transition(label='Whey Separation'),
    Transition(label='Molding Press'),
    Transition(label='Salting Stage'),
    Transition(label='Aging Control'),
    Transition(label='Packaging Design'),
    Transition(label='Cold Shipping'),
    Transition(label='Compliance Audit'),
    Transition(label='Blockchain Log'),
    Transition(label='Market Pricing'),
    Transition(label='Order Fulfillment'),
    Transition(label='Feedback Review')
])

root.order.add_edge(Transition(label='Milk Collection'), Transition(label='Quality Testing'))
root.order.add_edge(Transition(label='Quality Testing'), Transition(label='Milk Blending'))
root.order.add_edge(Transition(label='Milk Blending'), Transition(label='Starter Culture'))
root.order.add_edge(Transition(label='Starter Culture'), Transition(label='Fermentation Check'))
root.order.add_edge(Transition(label='Fermentation Check'), Transition(label='Curd Cutting'))
root.order.add_edge(Transition(label='Curd Cutting'), Transition(label='Whey Separation'))
root.order.add_edge(Transition(label='Whey Separation'), Transition(label='Molding Press'))
root.order.add_edge(Transition(label='Molding Press'), Transition(label='Salting Stage'))
root.order.add_edge(Transition(label='Salting Stage'), Transition(label='Aging Control'))
root.order.add_edge(Transition(label='Aging Control'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Packaging Design'), Transition(label='Cold Shipping'))
root.order.add_edge(Transition(label='Cold Shipping'), Transition(label='Compliance Audit'))
root.order.add_edge(Transition(label='Compliance Audit'), Transition(label='Blockchain Log'))
root.order.add_edge(Transition(label='Blockchain Log'), Transition(label='Market Pricing'))
root.order.add_edge(Transition(label='Market Pricing'), Transition(label='Order Fulfillment'))
root.order.add_edge(Transition(label='Order Fulfillment'), Transition(label='Feedback Review'))