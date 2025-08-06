import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
intake = Transition(label='Artifact Intake')
provenance = Transition(label='Provenance Check')
material = Transition(label='Material Testing')
historical = Transition(label='Historical Review')
expert = Transition(label='Expert Interview')
condition = Transition(label='Condition Audit')
catalog = Transition(label='Digital Catalog')
forgery = Transition(label='Forgery Detection')
compliance = Transition(label='Legal Compliance')
restoration = Transition(label='Restoration Plan')
valuation = Transition(label='Valuation Report')
analysis = Transition(label='Market Analysis')
approval = Transition(label='Final Approval')
sale = Transition(label='Sale Preparation')
notification = Transition(label='Client Notification')

# Define the process using POWL
root = StrictPartialOrder(nodes=[
    intake, provenance, material, historical, expert, condition, catalog, forgery, compliance, restoration, valuation, analysis, approval, sale, notification
])

# Define the dependencies between activities
root.order.add_edge(intake, provenance)
root.order.add_edge(provenance, material)
root.order.add_edge(material, historical)
root.order.add_edge(historical, expert)
root.order.add_edge(expert, condition)
root.order.add_edge(condition, catalog)
root.order.add_edge(catalog, forgery)
root.order.add_edge(forgery, compliance)
root.order.add_edge(compliance, restoration)
root.order.add_edge(restoration, valuation)
root.order.add_edge(valuation, analysis)
root.order.add_edge(analysis, approval)
root.order.add_edge(approval, sale)
root.order.add_edge(sale, notification)

print(root)