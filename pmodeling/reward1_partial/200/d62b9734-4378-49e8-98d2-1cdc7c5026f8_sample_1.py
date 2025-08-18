root = StrictPartialOrder(nodes=[
    Transition(label='Provenance Check'),
    Transition(label='Image Capture'),
    Transition(label='Material Scan'),
    Transition(label='Expert Review'),
    Transition(label='Historical Cross'),
    Transition(label='Legal Verify'),
    Transition(label='Registry Search'),
    Transition(label='Customs Clear'),
    Transition(label='Condition Assess'),
    Transition(label='Data Log'),
    Transition(label='Chain Custody'),
    Transition(label='Report Draft'),
    Transition(label='Certification'),
    Transition(label='Secure Archive'),
    Transition(label='Auction Prep')
])

root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Image Capture'))
root.order.add_edge(Transition(label='Image Capture'), Transition(label='Material Scan'))
root.order.add_edge(Transition(label='Material Scan'), Transition(label='Expert Review'))
root.order.add_edge(Transition(label='Expert Review'), Transition(label='Historical Cross'))
root.order.add_edge(Transition(label='Historical Cross'), Transition(label='Legal Verify'))
root.order.add_edge(Transition(label='Legal Verify'), Transition(label='Registry Search'))
root.order.add_edge(Transition(label='Registry Search'), Transition(label='Customs Clear'))
root.order.add_edge(Transition(label='Customs Clear'), Transition(label='Condition Assess'))
root.order.add_edge(Transition(label='Condition Assess'), Transition(label='Data Log'))
root.order.add_edge(Transition(label='Data Log'), Transition(label='Chain Custody'))
root.order.add_edge(Transition(label='Chain Custody'), Transition(label='Report Draft'))
root.order.add_edge(Transition(label='Report Draft'), Transition(label='Certification'))
root.order.add_edge(Transition(label='Certification'), Transition(label='Secure Archive'))
root.order.add_edge(Transition(label='Secure Archive'), Transition(label='Auction Prep'))