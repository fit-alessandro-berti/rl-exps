root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Layout'),
    Transition(label='System Build'),
    Transition(label='Install Sensors'),
    Transition(label='Set Controls'),
    Transition(label='Test Modules'),
    Transition(label='Select Crops'),
    Transition(label='Configure Irrigation'),
    Transition(label='Deploy AI'),
    Transition(label='Monitor Pests'),
    Transition(label='Manage Energy'),
    Transition(label='Recycle Waste'),
    Transition(label='Train Staff'),
    Transition(label='Launch Market'),
    Transition(label='Engage Community')
])

# Define dependencies between activities
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Design Layout'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='System Build'))
root.order.add_edge(Transition(label='System Build'), Transition(label='Install Sensors'))
root.order.add_edge(Transition(label='Install Sensors'), Transition(label='Set Controls'))
root.order.add_edge(Transition(label='Set Controls'), Transition(label='Test Modules'))
root.order.add_edge(Transition(label='Test Modules'), Transition(label='Select Crops'))
root.order.add_edge(Transition(label='Select Crops'), Transition(label='Configure Irrigation'))
root.order.add_edge(Transition(label='Configure Irrigation'), Transition(label='Deploy AI'))
root.order.add_edge(Transition(label='Deploy AI'), Transition(label='Monitor Pests'))
root.order.add_edge(Transition(label='Monitor Pests'), Transition(label='Manage Energy'))
root.order.add_edge(Transition(label='Manage Energy'), Transition(label='Recycle Waste'))
root.order.add_edge(Transition(label='Recycle Waste'), Transition(label='Train Staff'))
root.order.add_edge(Transition(label='Train Staff'), Transition(label='Launch Market'))
root.order.add_edge(Transition(label='Launch Market'), Transition(label='Engage Community'))