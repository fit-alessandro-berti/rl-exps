root = StrictPartialOrder(nodes=[
    Transition(label='Artifact Intake'),
    Transition(label='Document Check'),
    Transition(label='Provenance Search'),
    Transition(label='Ownership Validate'),
    Transition(label='Radiocarbon Test'),
    Transition(label='Spectroscopy Scan'),
    Transition(label='Material Analysis'),
    Transition(label='Style Assessment'),
    Transition(label='Context Review'),
    Transition(label='Expert Panel'),
    Transition(label='Report Draft'),
    Transition(label='Quality Review'),
    Transition(label='Catalog Entry'),
    Transition(label='Insurance Setup'),
    Transition(label='Archive Data'),
    Transition(label='Reevaluation Trigger')
])

root.order.add_edge('Artifact Intake', 'Document Check')
root.order.add_edge('Document Check', 'Provenance Search')
root.order.add_edge('Provenance Search', 'Ownership Validate')
root.order.add_edge('Ownership Validate', 'Radiocarbon Test')
root.order.add_edge('Radiocarbon Test', 'Spectroscopy Scan')
root.order.add_edge('Spectroscopy Scan', 'Material Analysis')
root.order.add_edge('Material Analysis', 'Style Assessment')
root.order.add_edge('Style Assessment', 'Context Review')
root.order.add_edge('Context Review', 'Expert Panel')
root.order.add_edge('Expert Panel', 'Report Draft')
root.order.add_edge('Report Draft', 'Quality Review')
root.order.add_edge('Quality Review', 'Catalog Entry')
root.order.add_edge('Catalog Entry', 'Insurance Setup')
root.order.add_edge('Insurance Setup', 'Archive Data')
root.order.add_edge('Archive Data', 'Reevaluation Trigger')