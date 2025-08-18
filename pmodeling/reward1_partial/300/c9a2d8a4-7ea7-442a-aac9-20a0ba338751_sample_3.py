from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loop for cross-functional collaboration
cross_functional_loop = OperatorPOWL(operator=Operator.LOOP, children=[
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
    monitor_compliance
])

# Define partial order with sequential activities
audit_process = StrictPartialOrder(nodes=[
    cross_functional_loop,
    finalize_report
])
audit_process.order.add_edge(cross_functional_loop, finalize_report)

# Set root to the final partial order
root = audit_process