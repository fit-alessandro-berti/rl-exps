root = StrictPartialOrder(nodes=[
    Transition(label='Source Materials'),
    Transition(label='Vet Suppliers'),
    Transition(label='Design Modules'),
    Transition(label='Prototype Build'),
    Transition(label='Test Durability'),
    Transition(label='Secure Permits'),
    Transition(label='Map Habitats'),
    Transition(label='Micro Warehouse'),
    Transition(label='Inventory Sync'),
    Transition(label='Pack Sustainably'),
    Transition(label='Route Optimize'),
    Transition(label='Engage Community'),
    Transition(label='Collect Feedback'),
    Transition(label='Adjust Production'),
    Transition(label='Partner NGOs'),
    Transition(label='Launch Campaign'),
    Transition(label='Monitor Sensors'),
    Transition(label='Report Impact')
])

# Define dependencies between activities
root.order.add_edge(Transition(label='Source Materials'), Transition(label='Vet Suppliers'))
root.order.add_edge(Transition(label='Vet Suppliers'), Transition(label='Design Modules'))
root.order.add_edge(Transition(label='Design Modules'), Transition(label='Prototype Build'))
root.order.add_edge(Transition(label='Prototype Build'), Transition(label='Test Durability'))
root.order.add_edge(Transition(label='Test Durability'), Transition(label='Secure Permits'))
root.order.add_edge(Transition(label='Secure Permits'), Transition(label='Map Habitats'))
root.order.add_edge(Transition(label='Map Habitats'), Transition(label='Micro Warehouse'))
root.order.add_edge(Transition(label='Micro Warehouse'), Transition(label='Inventory Sync'))
root.order.add_edge(Transition(label='Inventory Sync'), Transition(label='Pack Sustainably'))
root.order.add_edge(Transition(label='Pack Sustainably'), Transition(label='Route Optimize'))
root.order.add_edge(Transition(label='Route Optimize'), Transition(label='Engage Community'))
root.order.add_edge(Transition(label='Engage Community'), Transition(label='Collect Feedback'))
root.order.add_edge(Transition(label='Collect Feedback'), Transition(label='Adjust Production'))
root.order.add_edge(Transition(label='Adjust Production'), Transition(label='Partner NGOs'))
root.order.add_edge(Transition(label='Partner NGOs'), Transition(label='Launch Campaign'))
root.order.add_edge(Transition(label='Launch Campaign'), Transition(label='Monitor Sensors'))
root.order.add_edge(Transition(label='Monitor Sensors'), Transition(label='Report Impact'))