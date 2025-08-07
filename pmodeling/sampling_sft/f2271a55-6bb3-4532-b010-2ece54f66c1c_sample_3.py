import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
provenance = Transition(label='Provenance Check')
spectroscopy = Transition(label='Spectroscopy Test')
carbon = Transition(label='Carbon Dating')
style = Transition(label='Style Analysis')
image = Transition(label='Image Scanning')
restoration = Transition(label='Restoration Scan')
appraiser = Transition(label='Appraiser Review')
database = Transition(label='Database Match')
forgery = Transition(label='Forgery Detect')
report = Transition(label='Report Compilation')
blockchain = Transition(label='Blockchain Entry')
certificate = Transition(label='Certificate Issue')
client = Transition(label='Client Briefing')
storage = Transition(label='Secure Storage')
approval = Transition(label='Final Approval')

# Silent transition for loop exit
skip = SilentTransition()

# Loop: repeat forgery detection until no more forgery is detected
loop = OperatorPOWL(operator=Operator.LOOP, children=[forgery, skip])

# Build the partial order
root = StrictPartialOrder(nodes=[
    provenance,
    spectroscopy,
    carbon,
    style,
    image,
    restoration,
    appraiser,
    database,
    loop,
    report,
    blockchain,
    certificate,
    client,
    storage,
    approval
])

# Sequence: Provenance -> spectroscopy -> carbon -> style -> image -> restoration
root.order.add_edge(provenance, spectroscopy)
root.order.add_edge(spectroscopy, carbon)
root.order.add_edge(carbon, style)
root.order.add_edge(style, image)
root.order.add_edge(image, restoration)

# Sequence: Restoration -> appraiser -> database -> forgery loop -> report
root.order.add_edge(restoration, appraiser)
root.order.add_edge(appraiser, database)
root.order.add_edge(database, loop)

# Sequence: Forgery loop -> report
root.order.add_edge(loop, report)

# Sequence: Report -> blockchain -> certificate -> client -> storage -> approval
root.order.add_edge(report, blockchain)
root.order.add_edge(blockchain, certificate)
root.order.add_edge(certificate, client)
root.order.add_edge(client, storage)
root.order.add_edge(storage, approval)

print(root)