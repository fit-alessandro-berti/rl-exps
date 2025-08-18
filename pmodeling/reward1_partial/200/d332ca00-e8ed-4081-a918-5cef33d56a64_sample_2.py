root = StrictPartialOrder(nodes=[
    Transition(label='Intake Document'),
    Transition(label='Visual Inspect'),
    Transition(label='Imaging Scan'),
    Transition(label='Material Test'),
    Transition(label='Database Cross'),
    Transition(label='Provenance Check'),
    Transition(label='Expert Consult'),
    Transition(label='Carbon Dating'),
    Transition(label='Forensic Analyze'),
    Transition(label='Anomaly Review'),
    Transition(label='Risk Assess'),
    Transition(label='Report Draft'),
    Transition(label='Insurance Quote'),
    Transition(label='Storage Plan'),
    Transition(label='Final Approval')
])
root.order.add_edge(Transition(label='Intake Document'), Transition(label='Visual Inspect'))
root.order.add_edge(Transition(label='Intake Document'), Transition(label='Imaging Scan'))
root.order.add_edge(Transition(label='Intake Document'), Transition(label='Material Test'))
root.order.add_edge(Transition(label='Intake Document'), Transition(label='Database Cross'))
root.order.add_edge(Transition(label='Visual Inspect'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Visual Inspect'), Transition(label='Expert Consult'))
root.order.add_edge(Transition(label='Imaging Scan'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Imaging Scan'), Transition(label='Expert Consult'))
root.order.add_edge(Transition(label='Material Test'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Material Test'), Transition(label='Expert Consult'))
root.order.add_edge(Transition(label='Database Cross'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Database Cross'), Transition(label='Expert Consult'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Carbon Dating'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Forensic Analyze'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Anomaly Review'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Risk Assess'))
root.order.add_edge(Transition(label='Expert Consult'), Transition(label='Carbon Dating'))
root.order.add_edge(Transition(label='Expert Consult'), Transition(label='Forensic Analyze'))
root.order.add_edge(Transition(label='Expert Consult'), Transition(label='Anomaly Review'))
root.order.add_edge(Transition(label='Expert Consult'), Transition(label='Risk Assess'))
root.order.add_edge(Transition(label='Carbon Dating'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Carbon Dating'), Transition(label='Insurance Quote'))
root.order.add_edge(Transition(label='Carbon Dating'), Transition(label='Storage Plan'))
root.order.add_edge(Transition(label='Carbon Dating'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Forensic Analyze'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Forensic Analyze'), Transition(label='Insurance Quote'))
root.order.add_edge(Transition(label='Forensic Analyze'), Transition(label='Storage Plan'))
root.order.add_edge(Transition(label='Forensic Analyze'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Anomaly Review'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Anomaly Review'), Transition(label='Insurance Quote'))
root.order.add_edge(Transition(label='Anomaly Review'), Transition(label='Storage Plan'))
root.order.add_edge(Transition(label='Anomaly Review'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Risk Assess'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Risk Assess'), Transition(label='Insurance Quote'))
root.order.add_edge(Transition(label='Risk Assess'), Transition(label='Storage Plan'))
root.order.add_edge(Transition(label='Risk Assess'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Report Draft'), Transition(label='Insurance Quote'))
root.order.add_edge(Transition(label='Report Draft'), Transition(label='Storage Plan'))
root.order.add_edge(Transition(label='Report Draft'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Insurance Quote'), Transition(label='Storage Plan'))
root.order.add_edge(Transition(label='Insurance Quote'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Storage Plan'), Transition(label='Final Approval'))