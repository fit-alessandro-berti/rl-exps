import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
intake = Transition(label='Artifact Intake')
provenance = Transition(label='Provenance Check')
material_test = Transition(label='Material Testing')
historical = Transition(label='Historical Review')
expert = Transition(label='Expert Interview')
condition_audit = Transition(label='Condition Audit')
digital_catalog = Transition(label='Digital Catalog')
forgery_detection = Transition(label='Forgery Detection')
legal_compliance = Transition(label='Legal Compliance')
restoration_plan = Transition(label='Restoration Plan')
valuation_report = Transition(label='Valuation Report')
market_analysis = Transition(label='Market Analysis')
final_approval = Transition(label='Final Approval')
sale_preparation = Transition(label='Sale Preparation')
client_notification = Transition(label='Client Notification')

# Define the POWL model
root = StrictPartialOrder(nodes=[intake, provenance, material_test, historical, expert, condition_audit, digital_catalog, forgery_detection, legal_compliance, restoration_plan, valuation_report, market_analysis, final_approval, sale_preparation, client_notification])

# Define the dependencies (order) between the activities
root.order.add_edge(intake, provenance)
root.order.add_edge(provenance, material_test)
root.order.add_edge(material_test, historical)
root.order.add_edge(historical, expert)
root.order.add_edge(expert, condition_audit)
root.order.add_edge(condition_audit, digital_catalog)
root.order.add_edge(digital_catalog, forgery_detection)
root.order.add_edge(forgery_detection, legal_compliance)
root.order.add_edge(legal_compliance, restoration_plan)
root.order.add_edge(restoration_plan, valuation_report)
root.order.add_edge(valuation_report, market_analysis)
root.order.add_edge(market_analysis, final_approval)
root.order.add_edge(final_approval, sale_preparation)
root.order.add_edge(sale_preparation, client_notification)

print(root)