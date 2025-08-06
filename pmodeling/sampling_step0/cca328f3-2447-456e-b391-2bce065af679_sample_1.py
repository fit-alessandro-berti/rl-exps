root = StrictPartialOrder(nodes=[
    Transition(label='Artifact Intake'),
    Transition(label='Provenance Check'),
    Transition(label='Material Scan'),
    Transition(label='Style Compare'),
    Transition(label='Digital Capture'),
    Transition(label='Expert Review'),
    Transition(label='Database Search'),
    Transition(label='Legal Audit'),
    Transition(label='Cultural Assess'),
    Transition(label='Data Synthesis'),
    Transition(label='Report Draft'),
    Transition(label='Archival Store'),
    Transition(label='Display Approve'),
    Transition(label='Lender Notify'),
    Transition(label='Investigation Flag')
])

root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Material Scan'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Style Compare'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Digital Capture'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Expert Review'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Database Search'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Legal Audit'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Cultural Assess'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Data Synthesis'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Archival Store'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Display Approve'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Lender Notify'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Investigation Flag'))

root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Material Scan'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Style Compare'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Digital Capture'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Expert Review'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Database Search'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Legal Audit'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Cultural Assess'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Data Synthesis'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Archival Store'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Display Approve'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Lender Notify'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Investigation Flag'))

root.order.add_edge(Transition(label='Material Scan'), Transition(label='Style Compare'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Digital Capture'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Expert Review'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Database Search'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Legal Audit'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Cultural Assess'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Data Synthesis'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Archival Store'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Display Approve'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Lender Notify'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Investigation Flag'))

root.order.add_edge(Transition(label='Style Compare'), Transition(label='Digital Capture'))
root.order.add_edge(Transition(label='Style Compare'), Transition(label='Expert Review'))
root.order.add_edge(Transition(label='Style Compare'), Transition(label='Database Search'))
root.order.add_edge(Transition(label='Style Compare'), Transition(label='Legal Audit'))
root.order.add_edge(Transition(label='Style Compare'), Transition(label='Cultural Assess'))
root.order.add_edge(Transition(label='Style Compare'), Transition(label='Data Synthesis'))
root.order.add_edge(Transition(label='Style Compare'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Style Compare'), Transition(label='Archival Store'))
root.order.add_edge(Transition(label='Style Compare'), Transition(label='Display Approve'))
root.order.add_edge(Transition(label='Style Compare'), Transition(label='Lender Notify'))
root.order.add_edge(Transition(label='Style Compare'), Transition(label='Investigation Flag'))

root.order.add_edge(Transition(label='Digital Capture'), Transition(label='Expert Review'))
root.order.add_edge(Transition(label='Digital Capture'), Transition(label='Database Search'))
root.order.add_edge(Transition(label='Digital Capture'), Transition(label='Legal Audit'))
root.order.add_edge(Transition(label='Digital Capture'), Transition(label='Cultural Assess'))
root.order.add_edge(Transition(label='Digital Capture'), Transition(label='Data Synthesis'))
root.order.add_edge(Transition(label='Digital Capture'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Digital Capture'), Transition(label='Archival Store'))
root.order.add_edge(Transition(label='Digital Capture'), Transition(label='Display Approve'))
root.order.add_edge(Transition(label='Digital Capture'), Transition(label='Lender Notify'))
root.order.add_edge(Transition(label='Digital Capture'), Transition(label='Investigation Flag'))

root.order.add_edge(Transition(label='Expert Review'), Transition(label='Database Search'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Legal Audit'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Cultural Assess'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Data Synthesis'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Archival Store'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Display Approve'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Lender Notify'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Investigation Flag'))

root.order.add_edge(Transition(label='Database Search'), Transition(label='Legal Audit'))
root.order.add_edge(Transition(label='Database Search'), Transition(label='Cultural Assess'))
root.order.add_edge(Transition(label='Database Search'), Transition(label='Data Synthesis'))
root.order.add_edge(Transition(label='Database Search'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Database Search'), Transition(label='Archival Store'))
root.order.add_edge(Transition(label='Database Search'), Transition(label='Display Approve'))
root.order.add_edge(Transition(label='Database Search'), Transition(label='Lender Notify'))
root.order.add_edge(Transition(label='Database Search'), Transition(label='Investigation Flag'))

root.order.add_edge(Transition(label='Legal Audit'), Transition(label='Cultural Assess'))
root.order.add_edge(Transition(label='Legal Audit'), Transition(label='Data Synthesis'))
root.order.add_edge(Transition(label='Legal Audit'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Legal Audit'), Transition(label='Archival Store'))
root.order.add_edge(Transition(label='Legal Audit'), Transition(label='Display Approve'))
root.order.add_edge(Transition(label='Legal Audit'), Transition(label='Lender Notify'))
root.order.add_edge(Transition(label='Legal Audit'), Transition(label='Investigation Flag'))

root.order.add_edge(Transition(label='Cultural Assess'), Transition(label='Data Synthesis'))
root.order.add_edge(Transition(label='Cultural Assess'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Cultural Assess'), Transition(label='Archival Store'))
root.order.add_edge(Transition(label='Cultural Assess'), Transition(label='Display Approve'))
root.order.add_edge(Transition(label='Cultural Assess'), Transition(label='Lender Notify'))
root.order.add_edge(Transition(label='Cultural Assess'), Transition(label='Investigation Flag'))

root.order.add_edge(Transition(label='Data Synthesis'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Data Synthesis'), Transition(label='Archival Store'))
root.order.add_edge(Transition(label='Data Synthesis'), Transition(label='Display Approve'))
root.order.add_edge(Transition(label='Data Synthesis'), Transition(label='Lender Notify'))
root.order.add_edge(Transition(label='Data Synthesis'), Transition(label='Investigation Flag'))

root.order.add_edge(Transition(label='Report Draft'), Transition(label='Archival Store'))
root.order.add_edge(Transition(label='Report Draft'), Transition(label='Display Approve'))
root.order.add_edge(Transition(label='Report Draft'), Transition(label='Lender Notify'))
root.order.add_edge(Transition(label='Report Draft'), Transition(label='Investigation Flag'))

root.order.add_edge(Transition(label='Archival Store'), Transition(label='Display Approve'))
root.order.add_edge(Transition(label='Archival Store'), Transition(label='Lender Notify'))
root.order.add_edge(Transition(label='Archival Store'), Transition(label='Investigation Flag'))

root.order.add_edge(Transition(label='Display Approve'), Transition(label='Lender Notify'))
root.order.add_edge(Transition(label='Display Approve'), Transition(label='Investigation Flag'))

root.order.add_edge(Transition(label='Lender Notify'), Transition(label='Investigation Flag'))