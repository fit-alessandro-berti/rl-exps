import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
brand_audit = Transition(label='Brand Audit')
equity_review = Transition(label='Equity Review')
market_analysis = Transition(label='Market Analysis')
legal_clearance = Transition(label='Legal Clearance')
trademark_check = Transition(label='Trademark Check')
portfolio_merge = Transition(label='Portfolio Merge')
customer_sync = Transition(label='Customer Sync')
cultural_align = Transition(label='Cultural Align')
internal_brief = Transition(label='Internal Brief')
campaign_design = Transition(label='Campaign Design')
resource_plan = Transition(label='Resource Plan')
stakeholder_meet = Transition(label='Stakeholder Meet')
launch_prep = Transition(label='Launch Prep')
feedback_loop = Transition(label='Feedback Loop')
performance_track = Transition(label='Performance Track')

# Define transitions
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, trademark_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, equity_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[brand_audit, xor2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[xor1, xor3])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[cultural_align, internal_brief, campaign_design, resource_plan, stakeholder_meet, launch_prep])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, performance_track])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])

# Define root
root = StrictPartialOrder(nodes=[xor5])
root.order.add_edge(xor5, loop1)
root.order.add_edge(xor5, loop2)
root.order.add_edge(loop1, loop2)

# Print the root
print(root)