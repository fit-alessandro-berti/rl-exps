import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
begin_contract_negotiations = Transition(label='Begin contract negotiations')
conduct_interview = Transition(label='Conduct interview')
conduct_site_visit = Transition(label='Conduct site visit')
evaluate_proposal = Transition(label='Evaluate proposal')
execute_contract = Transition(label='Execute contract')
identify_need = Transition(label='Identify need for new supplier or vendor')
issue_rfp = Transition(label='Issue request for proposals (RFP)')
onboard_supplier = Transition(label='Onboard supplier')
receive_proposals = Transition(label='Receive supplier proposals')
select_supplier = Transition(label='Select supplier')
sign_contract = Transition(label='Sign contract')

# Define the loop for contract negotiations
contract_negotiation_loop = OperatorPOWL(operator=Operator.LOOP, children=[begin_contract_negotiations, conduct_interview, conduct_site_visit, evaluate_proposal, sign_contract])

# Define the choice for site visit or interview
site_visit_or_interview = OperatorPOWL(operator=Operator.XOR, children=[conduct_site_visit, conduct_interview])

# Define the loop for proposal evaluation
proposal_evaluation_loop = OperatorPOWL(operator=Operator.LOOP, children=[evaluate_proposal, site_visit_or_interview])

# Define the overall process tree
root = StrictPartialOrder(nodes=[identify_need, issue_rfp, receive_proposals, proposal_evaluation_loop, select_supplier, contract_negotiation_loop, execute_contract, onboard_supplier])

# Define the order of the nodes
root.order.add_edge(identify_need, issue_rfp)
root.order.add_edge(issue_rfp, receive_proposals)
root.order.add_edge(receive_proposals, proposal_evaluation_loop)
root.order.add_edge(proposal_evaluation_loop, select_supplier)
root.order.add_edge(select_supplier, contract_negotiation_loop)
root.order.add_edge(contract_negotiation_loop, execute_contract)
root.order.add_edge(execute_contract, onboard_supplier)