root = StrictPartialOrder(
    nodes=[
        Transition(label='Milk Sourcing'),
        Transition(label='Quality Testing'),
        Transition(label='Culture Prep'),
        Transition(label='Milk Pasteurize'),
        Transition(label='Curd Cutting'),
        Transition(label='Whey Draining'),
        Transition(label='Molding Cheese'),
        Transition(label='Pressing Blocks'),
        Transition(label='Salting Process'),
        Transition(label='Aging Monitoring'),
        Transition(label='Flavor Profiling'),
        Transition(label='Packaging Design'),
        Transition(label='Compliance Check'),
        Transition(label='Market Research'),
        Transition(label='Direct Shipping'),
        Transition(label='Customer Feedback'),
        Transition(label='Recipe Adjust')
    ],
    order=[
        (Transition(label='Milk Sourcing'), Transition(label='Quality Testing')),
        (Transition(label='Quality Testing'), Transition(label='Culture Prep')),
        (Transition(label='Culture Prep'), Transition(label='Milk Pasteurize')),
        (Transition(label='Milk Pasteurize'), Transition(label='Curd Cutting')),
        (Transition(label='Curd Cutting'), Transition(label='Whey Draining')),
        (Transition(label='Whey Draining'), Transition(label='Molding Cheese')),
        (Transition(label='Molding Cheese'), Transition(label='Pressing Blocks')),
        (Transition(label='Pressing Blocks'), Transition(label='Salting Process')),
        (Transition(label='Salting Process'), Transition(label='Aging Monitoring')),
        (Transition(label='Aging Monitoring'), Transition(label='Flavor Profiling')),
        (Transition(label='Flavor Profiling'), Transition(label='Packaging Design')),
        (Transition(label='Packaging Design'), Transition(label='Compliance Check')),
        (Transition(label='Compliance Check'), Transition(label='Market Research')),
        (Transition(label='Market Research'), Transition(label='Direct Shipping')),
        (Transition(label='Direct Shipping'), Transition(label='Customer Feedback')),
        (Transition(label='Customer Feedback'), Transition(label='Recipe Adjust'))
    ]
)