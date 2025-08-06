root = StrictPartialOrder(nodes=[
    Transition(label='Assess Structure'),
    Transition(label='Analyze Environment'),
    Transition(label='Design Modules'),
    Transition(label='Procure Materials'),
    Transition(label='Install Irrigation'),
    Transition(label='Set Sensors'),
    Transition(label='Select Seeds'),
    Transition(label='Schedule Planting'),
    Transition(label='Monitor Growth'),
    Transition(label='Collect Data'),
    Transition(label='Manage Pests'),
    Transition(label='Harvest Crops'),
    Transition(label='Coordinate Sales'),
    Transition(label='Compost Waste'),
    Transition(label='Review Feedback')
])
root.order.add_edge(Transition(label='Assess Structure'), Transition(label='Analyze Environment'))
root.order.add_edge(Transition(label='Analyze Environment'), Transition(label='Design Modules'))
root.order.add_edge(Transition(label='Design Modules'), Transition(label='Procure Materials'))
root.order.add_edge(Transition(label='Procure Materials'), Transition(label='Install Irrigation'))
root.order.add_edge(Transition(label='Install Irrigation'), Transition(label='Set Sensors'))
root.order.add_edge(Transition(label='Set Sensors'), Transition(label='Select Seeds'))
root.order.add_edge(Transition(label='Select Seeds'), Transition(label='Schedule Planting'))
root.order.add_edge(Transition(label='Schedule Planting'), Transition(label='Monitor Growth'))
root.order.add_edge(Transition(label='Monitor Growth'), Transition(label='Collect Data'))
root.order.add_edge(Transition(label='Collect Data'), Transition(label='Manage Pests'))
root.order.add_edge(Transition(label='Manage Pests'), Transition(label='Harvest Crops'))
root.order.add_edge(Transition(label='Harvest Crops'), Transition(label='Coordinate Sales'))
root.order.add_edge(Transition(label='Coordinate Sales'), Transition(label='Compost Waste'))
root.order.add_edge(Transition(label='Compost Waste'), Transition(label='Review Feedback'))