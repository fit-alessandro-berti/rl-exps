import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions based on the activities
initiate_audit = Transition(label='Initiate Audit')
gather_documents = Transition(label='Gather Documents')
verify_suppliers = Transition(label='Verify Suppliers')
screen_transactions = Transition(label='Screen Transactions')
classify_products = Transition(label='Classify Products')
assess_risks = Transition(label='Assess Risks')
check_sanctions = Transition(label='Check Sanctions')
review_tariffs = Transition(label='Review Tariffs')
cross_verify_data = Transition(label='Cross-Verify Data')
conduct_interviews = Transition(label='Conduct Interviews')
analyze_reports = Transition(label='Analyze Reports')
identify_gaps = Transition(label='Identify Gaps')
recommend_actions = Transition(label='Recommend Actions')
implement_changes = Transition(label='Implement Changes')
monitor_compliance = Transition(label='Monitor Compliance')
finalize_report = Transition(label='Finalize Report')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    initiate_audit,
    gather_documents,
    verify_suppliers,
    screen_transactions,
    classify_products,
    assess_risks,
    check_sanctions,
    review_tariffs,
    cross_verify_data,
    conduct_interviews,
    analyze_reports,
    identify_gaps,
    recommend_actions,
    implement_changes,
    monitor_compliance,
    finalize_report
])

# Define the dependencies between nodes
root.order.add_edge(initiate_audit, gather_documents)
root.order.add_edge(initiate_audit, verify_suppliers)
root.order.add_edge(initiate_audit, screen_transactions)
root.order.add_edge(initiate_audit, classify_products)
root.order.add_edge(initiate_audit, assess_risks)
root.order.add_edge(initiate_audit, check_sanctions)
root.order.add_edge(initiate_audit, review_tariffs)
root.order.add_edge(initiate_audit, cross_verify_data)
root.order.add_edge(initiate_audit, conduct_interviews)
root.order.add_edge(initiate_audit, analyze_reports)
root.order.add_edge(initiate_audit, identify_gaps)
root.order.add_edge(initiate_audit, recommend_actions)
root.order.add_edge(initiate_audit, implement_changes)
root.order.add_edge(initiate_audit, monitor_compliance)
root.order.add_edge(initiate_audit, finalize_report)

# The final result is stored in 'root'