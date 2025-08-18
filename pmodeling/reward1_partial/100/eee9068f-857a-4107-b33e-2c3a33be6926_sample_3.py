root = StrictPartialOrder(nodes=[
    Transition(label='Artifact Intake'),
    Transition(label='Provenance Check'),
    Transition(label='Archive Search'),
    Transition(label='Expert Interview'),
    Transition(label='Material Scan'),
    Transition(label='Age Analysis'),
    Transition(label='Stylistic Review'),
    Transition(label='Context Mapping'),
    Transition(label='Legal Clearance'),
    Transition(label='Data Compilation'),
    Transition(label='Report Drafting'),
    Transition(label='Peer Review'),
    Transition(label='Final Assessment'),
    Transition(label='Acquisition Plan'),
    Transition(label='Restoration Prep'),
    Transition(label='Documentation'),
    Transition(label='Data Backup')
])

# Define the partial order
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Archive Search'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Expert Interview'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Material Scan'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Age Analysis'))
root.order.add_edge(Transition(label='Archive Search'), Transition(label='Stylistic Review'))
root.order.add_edge(Transition(label='Expert Interview'), Transition(label='Context Mapping'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Legal Clearance'))
root.order.add_edge(Transition(label='Age Analysis'), Transition(label='Data Compilation'))
root.order.add_edge(Transition(label='Stylistic Review'), Transition(label='Report Drafting'))
root.order.add_edge(Transition(label='Context Mapping'), Transition(label='Peer Review'))
root.order.add_edge(Transition(label='Legal Clearance'), Transition(label='Final Assessment'))
root.order.add_edge(Transition(label='Data Compilation'), Transition(label='Acquisition Plan'))
root.order.add_edge(Transition(label='Report Drafting'), Transition(label='Restoration Prep'))
root.order.add_edge(Transition(label='Peer Review'), Transition(label='Documentation'))
root.order.add_edge(Transition(label='Final Assessment'), Transition(label='Data Backup'))