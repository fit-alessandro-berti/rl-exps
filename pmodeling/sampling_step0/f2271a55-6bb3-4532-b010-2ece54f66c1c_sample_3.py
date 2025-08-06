root = StrictPartialOrder(nodes=[
    Transition(label='Provenance Check'),
    Transition(label='Spectroscopy Test'),
    Transition(label='Carbon Dating'),
    Transition(label='Style Analysis'),
    Transition(label='Image Scanning'),
    Transition(label='Restoration Scan'),
    Transition(label='Appraiser Review'),
    Transition(label='Database Match'),
    Transition(label='Blockchain Entry'),
    Transition(label='Certificate Issue'),
    Transition(label='Forgery Detect'),
    Transition(label='Report Compilation'),
    Transition(label='Client Briefing'),
    Transition(label='Secure Storage'),
    Transition(label='Final Approval')
])
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Spectroscopy Test'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Carbon Dating'))
root.order.add_edge(Transition(label='Spectroscopy Test'), Transition(label='Style Analysis'))
root.order.add_edge(Transition(label='Spectroscopy Test'), Transition(label='Database Match'))
root.order.add_edge(Transition(label='Carbon Dating'), Transition(label='Style Analysis'))
root.order.add_edge(Transition(label='Style Analysis'), Transition(label='Database Match'))
root.order.add_edge(Transition(label='Image Scanning'), Transition(label='Restoration Scan'))
root.order.add_edge(Transition(label='Restoration Scan'), Transition(label='Appraiser Review'))
root.order.add_edge(Transition(label='Appraiser Review'), Transition(label='Database Match'))
root.order.add_edge(Transition(label='Database Match'), Transition(label='Blockchain Entry'))
root.order.add_edge(Transition(label='Blockchain Entry'), Transition(label='Certificate Issue'))
root.order.add_edge(Transition(label='Certificate Issue'), Transition(label='Forgery Detect'))
root.order.add_edge(Transition(label='Forgery Detect'), Transition(label='Report Compilation'))
root.order.add_edge(Transition(label='Report Compilation'), Transition(label='Client Briefing'))
root.order.add_edge(Transition(label='Client Briefing'), Transition(label='Secure Storage'))
root.order.add_edge(Transition(label='Secure Storage'), Transition(label='Final Approval'))