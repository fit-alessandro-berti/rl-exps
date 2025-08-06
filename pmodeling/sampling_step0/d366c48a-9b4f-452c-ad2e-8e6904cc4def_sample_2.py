root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Climate Scan'),
    Transition(label='Module Setup'),
    Transition(label='Crop Choice'),
    Transition(label='Nutrient Feed'),
    Transition(label='Pest Control'),
    Transition(label='Energy Audit'),
    Transition(label='Waste Cycle'),
    Transition(label='Growth Track'),
    Transition(label='Demand Plan'),
    Transition(label='Community Link'),
    Transition(label='Regulation Check'),
    Transition(label='Supply Sync'),
    Transition(label='System Upgrade'),
    Transition(label='Data Backup'),
    OperatorPOWL(operator=Operator.XOR, children=[
        OperatorPOWL(operator=Operator.LOOP, children=[
            Transition(label='Site Survey'),
            Transition(label='Climate Scan'),
            Transition(label='Module Setup'),
            Transition(label='Crop Choice'),
            Transition(label='Nutrient Feed'),
            Transition(label='Pest Control'),
            Transition(label='Energy Audit'),
            Transition(label='Waste Cycle'),
            Transition(label='Growth Track'),
            Transition(label='Demand Plan'),
            Transition(label='Community Link'),
            Transition(label='Regulation Check'),
            Transition(label='Supply Sync'),
            Transition(label='System Upgrade'),
            Transition(label='Data Backup'),
        ])
    ])
])

root.order.add_edge(root.children[0], root.children[1])
root.order.add_edge(root.children[1], root.children[2])
root.order.add_edge(root.children[2], root.children[3])
root.order.add_edge(root.children[3], root.children[4])
root.order.add_edge(root.children[4], root.children[5])
root.order.add_edge(root.children[5], root.children[6])
root.order.add_edge(root.children[6], root.children[7])
root.order.add_edge(root.children[7], root.children[8])
root.order.add_edge(root.children[8], root.children[9])
root.order.add_edge(root.children[9], root.children[10])
root.order.add_edge(root.children[10], root.children[11])
root.order.add_edge(root.children[11], root.children[12])
root.order.add_edge(root.children[12], root.children[13])
root.order.add_edge(root.children[13], root.children[14])
root.order.add_edge(root.children[14], root.children[15])
root.order.add_edge(root.children[15], root.children[16])