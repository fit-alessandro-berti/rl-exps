root = StrictPartialOrder(nodes=[
    Transition('Intake Review'),
    Transition('Condition Scan'),
    Transition('Material Test'),
    Transition('Style Match'),
    Transition('Provenance Log'),
    Transition('Forgery Risk'),
    Transition('Legal Audit'),
    Transition('Expert Panel'),
    Transition('Data Crosscheck'),
    Transition('Report Draft'),
    Transition('Blockchain Tag'),
    Transition('Certification'),
    Transition('Client Feedback'),
    Transition('Final Approval'),
    Transition('Release Prep')
])

root.order.add_edge('Intake Review', 'Condition Scan')
root.order.add_edge('Condition Scan', 'Material Test')
root.order.add_edge('Material Test', 'Style Match')
root.order.add_edge('Style Match', 'Provenance Log')
root.order.add_edge('Provenance Log', 'Forgery Risk')
root.order.add_edge('Forgery Risk', 'Legal Audit')
root.order.add_edge('Legal Audit', 'Expert Panel')
root.order.add_edge('Expert Panel', 'Data Crosscheck')
root.order.add_edge('Data Crosscheck', 'Report Draft')
root.order.add_edge('Report Draft', 'Blockchain Tag')
root.order.add_edge('Blockchain Tag', 'Certification')
root.order.add_edge('Certification', 'Client Feedback')
root.order.add_edge('Client Feedback', 'Final Approval')
root.order.add_edge('Final Approval', 'Release Prep')