root = StrictPartialOrder(nodes=[
    Transition(label='Concept Ideation'),
    Transition(label='Sponsor Alignment'),
    Transition(label='Participant SignUp'),
    Transition(label='Team Formation'),
    Transition(label='Workshop Setup'),
    Transition(label='Workshop Delivery'),
    Transition(label='Progress Monitor'),
    Transition(label='Live Support'),
    Transition(label='Feedback Loop'),
    Transition(label='Submission Check'),
    Transition(label='Plagiarism Scan'),
    Transition(label='Jury Evaluation'),
    Transition(label='Result Compilation'),
    Transition(label='Winner Announcement'),
    Transition(label='Post Analytics')
])

root.order.add_edge(Transition(label='Concept Ideation'), Transition(label='Sponsor Alignment'))
root.order.add_edge(Transition(label='Sponsor Alignment'), Transition(label='Participant SignUp'))
root.order.add_edge(Transition(label='Participant SignUp'), Transition(label='Team Formation'))
root.order.add_edge(Transition(label='Team Formation'), Transition(label='Workshop Setup'))
root.order.add_edge(Transition(label='Workshop Setup'), Transition(label='Workshop Delivery'))
root.order.add_edge(Transition(label='Workshop Delivery'), Transition(label='Progress Monitor'))
root.order.add_edge(Transition(label='Progress Monitor'), Transition(label='Live Support'))
root.order.add_edge(Transition(label='Live Support'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Feedback Loop'), Transition(label='Submission Check'))
root.order.add_edge(Transition(label='Submission Check'), Transition(label='Plagiarism Scan'))
root.order.add_edge(Transition(label='Plagiarism Scan'), Transition(label='Jury Evaluation'))
root.order.add_edge(Transition(label='Jury Evaluation'), Transition(label='Result Compilation'))
root.order.add_edge(Transition(label='Result Compilation'), Transition(label='Winner Announcement'))
root.order.add_edge(Transition(label='Winner Announcement'), Transition(label='Post Analytics'))