root = StrictPartialOrder(nodes=[
    Transition('Provenance Check'),
    Transition('Radiocarbon Test'),
    Transition('Material Analysis'),
    Transition('Microscopic Scan'),
    Transition('Expert Review'),
    Transition('Context Validation'),
    Transition('Legal Audit'),
    Transition('Export Verify'),
    Transition('Digital Imaging'),
    Transition('3D Modeling'),
    Transition('Consensus Meeting'),
    Transition('Final Approval'),
    Transition('Catalog Entry'),
    Transition('Virtual Setup'),
    Transition('Archival Backup'),
    Transition('Archival Backup')
])

root.order.add_edge(Transition('Provenance Check'), Transition('Radiocarbon Test'))
root.order.add_edge(Transition('Radiocarbon Test'), Transition('Material Analysis'))
root.order.add_edge(Transition('Material Analysis'), Transition('Microscopic Scan'))
root.order.add_edge(Transition('Microscopic Scan'), Transition('Expert Review'))
root.order.add_edge(Transition('Expert Review'), Transition('Context Validation'))
root.order.add_edge(Transition('Context Validation'), Transition('Legal Audit'))
root.order.add_edge(Transition('Legal Audit'), Transition('Export Verify'))
root.order.add_edge(Transition('Export Verify'), Transition('Digital Imaging'))
root.order.add_edge(Transition('Digital Imaging'), Transition('3D Modeling'))
root.order.add_edge(Transition('3D Modeling'), Transition('Consensus Meeting'))
root.order.add_edge(Transition('Consensus Meeting'), Transition('Final Approval'))
root.order.add_edge(Transition('Final Approval'), Transition('Catalog Entry'))
root.order.add_edge(Transition('Catalog Entry'), Transition('Virtual Setup'))
root.order.add_edge(Transition('Virtual Setup'), Transition('Archival Backup'))
root.order.add_edge(Transition('Archival Backup'), Transition('Archival Backup'))