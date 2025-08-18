root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Permit Check'),
    Transition(label='Hive Setup'),
    Transition(label='Community Meet'),
    Transition(label='Hive Monitor'),
    Transition(label='Pest Control'),
    Transition(label='Honey Harvest'),
    Transition(label='Data Logging'),
    Transition(label='Workshop Plan'),
    Transition(label='Supply Order'),
    Transition(label='Volunteer Coord'),
    Transition(label='Regulation Review'),
    Transition(label='Pollination Map'),
    Transition(label='Apiary Audit'),
    Transition(label='Feedback Gather'),
    Transition(label='Waste Manage'),
    OperatorPOWL(operator=Operator.LOOP, children=[
        Transition(label='Hive Setup'),
        Transition(label='Community Meet')
    ])
])
root.order.add_edge(Transition(label='Hive Setup'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Hive Monitor'))
root.order.add_edge(Transition(label='Hive Monitor'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Honey Harvest'))
root.order.add_edge(Transition(label='Honey Harvest'), Transition(label='Data Logging'))
root.order.add_edge(Transition(label='Data Logging'), Transition(label='Workshop Plan'))
root.order.add_edge(Transition(label='Workshop Plan'), Transition(label='Supply Order'))
root.order.add_edge(Transition(label='Supply Order'), Transition(label='Volunteer Coord'))
root.order.add_edge(Transition(label='Volunteer Coord'), Transition(label='Regulation Review'))
root.order.add_edge(Transition(label='Regulation Review'), Transition(label='Pollination Map'))
root.order.add_edge(Transition(label='Pollination Map'), Transition(label='Apiary Audit'))
root.order.add_edge(Transition(label='Apiary Audit'), Transition(label='Feedback Gather'))
root.order.add_edge(Transition(label='Feedback Gather'), Transition(label='Waste Manage'))
root.order.add_edge(Transition(label='Waste Manage'), Transition(label='Hive Setup'))