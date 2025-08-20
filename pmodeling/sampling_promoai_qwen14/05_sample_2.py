import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
Begin_contract_negotiations = Transition(label='Begin contract negotiations')
Conduct_interview = Transition(label='Conduct interview')
Conduct_site_visit = Transition(label='Conduct site visit')
Evaluate_proposal = Transition(label='Evaluate proposal')
Execute_contract = Transition(label='Execute contract')
Identify_need_for_new_supplier_or_vendor = Transition(label='Identify need for new supplier or vendor')
Issue_request_for_proposals_RFP = Transition(label='Issue request for proposals (RFP)')
Onboard_supplier = Transition(label='Onboard supplier')
Receive_supplier_proposals = Transition(label='Receive supplier proposals')
Select_supplier = Transition(label='Select supplier')
Sign_contract = Transition(label='Sign contract')

# Define the choice of site visit and interview
site_visit_or_interview = OperatorPOWL(operator=Operator.XOR, children=[Conduct_site_visit, Conduct_interview])

# Define the choice of evaluating proposals and selecting a supplier
evaluate_and_select = OperatorPOWL(operator=Operator.XOR, children=[Evaluate_proposal, Select_supplier])

# Define the loop for evaluating proposals and selecting a supplier
evaluate_and_select_loop = OperatorPOWL(operator=Operator.LOOP, children=[evaluate_and_select])

# Define the process
root = StrictPartialOrder(nodes=[Identify_need_for_new_supplier_or_vendor, Issue_request_for_proposals_RFP, Receive_supplier_proposals, evaluate_and_select_loop, site_visit_or_interview, Begin_contract_negotiations, Sign_contract, Execute_contract, Onboard_supplier])

# Define the order of the transitions
root.order.add_edge(Identify_need_for_new_supplier_or_vendor, Issue_request_for_proposals_RFP)
root.order.add_edge(Issue_request_for_proposals_RFP, Receive_supplier_proposals)
root.order.add_edge(Receive_supplier_proposals, evaluate_and_select_loop)
root.order.add_edge(evaluate_and_select_loop, site_visit_or_interview)
root.order.add_edge(site_visit_or_interview, Begin_contract_negotiations)
root.order.add_edge(Begin_contract_negotiations, Sign_contract)
root.order.add_edge(Sign_contract, Execute_contract)
root.order.add_edge(Execute_contract, Onboard_supplier)