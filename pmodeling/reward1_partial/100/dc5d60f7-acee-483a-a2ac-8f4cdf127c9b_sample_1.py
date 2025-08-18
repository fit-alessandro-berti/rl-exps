root = StrictPartialOrder(nodes=[
    Transition(label='Intake Review'),
    Transition(label='Condition Scan'),
    Transition(label='Material Test'),
    Transition(label='Style Match'),
    Transition(label='Provenance Log'),
    Transition(label='Forgery Risk'),
    Transition(label='Legal Audit'),
    Transition(label='Expert Panel'),
    Transition(label='Data Crosscheck'),
    Transition(label='Report Draft'),
    Transition(label='Blockchain Tag'),
    Transition(label='Certification'),
    Transition(label='Client Feedback'),
    Transition(label='Final Approval'),
    Transition(label='Release Prep')
])

root.order.add_edge(Transition(label='Intake Review'), Transition(label='Condition Scan'))
root.order.add_edge(Transition(label='Condition Scan'), Transition(label='Material Test'))
root.order.add_edge(Transition(label='Material Test'), Transition(label='Style Match'))
root.order.add_edge(Transition(label='Style Match'), Transition(label='Provenance Log'))
root.order.add_edge(Transition(label='Provenance Log'), Transition(label='Forgery Risk'))
root.order.add_edge(Transition(label='Forgery Risk'), Transition(label='Legal Audit'))
root.order.add_edge(Transition(label='Legal Audit'), Transition(label='Expert Panel'))
root.order.add_edge(Transition(label='Expert Panel'), Transition(label='Data Crosscheck'))
root.order.add_edge(Transition(label='Data Crosscheck'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Report Draft'), Transition(label='Blockchain Tag'))
root.order.add_edge(Transition(label='Blockchain Tag'), Transition(label='Certification'))
root.order.add_edge(Transition(label='Certification'), Transition(label='Client Feedback'))
root.order.add_edge(Transition(label='Client Feedback'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Final Approval'), Transition(label='Release Prep'))