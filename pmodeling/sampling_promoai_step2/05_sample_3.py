from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
begin_contract_negotiations = Transition(label='Begin contract negotiations')
conduct_interview = Transition(label='Conduct interview')
conduct_site_visit = Transition(label='Conduct site visit')
evaluate_proposal = Transition(label='Evaluate proposal')
execute_contract = Transition(label='Execute contract')
identify_need_for_new_supplier_or_vendor = Transition(label='Identify need for new supplier or vendor')
issue_request_for_proposals_RFP = Transition(label='Issue request for proposals (RFP)')
onboard_supplier = Transition(label='Onboard supplier')
receive_supplier_proposals = Transition(label='Receive supplier proposals')
select_supplier = Transition(label='Select supplier')
sign_contract = Transition(label='Sign contract')

# Define the partial order
root = StrictPartialOrder(nodes=[
    identify_need_for_new_supplier_or_vendor,
    issue_request_for_proposals_RFP,
    receive_supplier_proposals,
    evaluate_proposal,
    conduct_interview,
    conduct_site_visit,
    select_supplier,
    begin_contract_negotiations,
    sign_contract,
    onboard_supplier
])

# Define the dependencies between nodes
root.order.add_edge(identify_need_for_new_supplier_or_vendor, issue_request_for_proposals_RFP)
root.order.add_edge(issue_request_for_proposals_RFP, receive_supplier_proposals)
root.order.add_edge(receive_supplier_proposals, evaluate_proposal)
root.order.add_edge(evaluate_proposal, conduct_interview)
root.order.add_edge(evaluate_proposal, conduct_site_visit)
root.order.add_edge(conduct_interview, select_supplier)
root.order.add_edge(conduct_site_visit, select_supplier)
root.order.add_edge(select_supplier, begin_contract_negotiations)
root.order.add_edge(begin_contract_negotiations, sign_contract)
root.order.add_edge(sign_contract, onboard_supplier)

print(root)