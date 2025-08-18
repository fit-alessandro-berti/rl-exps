from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
inq = Transition(label='Inquiry Review')
c_onb = Transition(label='Client Onboard')
con_d = Transition(label='Concept Draft')
f_cycle = Transition(label='Feedback Cycle')
con_set = Transition(label='Contract Setup')
pay_sch = Transition(label='Payment Schedule')
mat_src = Transition(label='Material Sourcing')
art_crt = Transition(label='Artwork Create')
qual_chk = Transition(label='Quality Check')
frm_sel = Transition(label='Frame Selection')
pack_prep = Transition(label='Packaging Prep')
ship_arr = Transition(label='Shipment Arrange')
del_conf = Transition(label='Delivery Confirm')
psu = Transition(label='Post-Sale Support')
rev_man = Transition(label='Revision Manage')
delay_mit = Transition(label='Delay Mitigate')

# Define silent transition for skip
skip = SilentTransition()

# Define loop for feedback cycle
f_cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[con_d, f_cycle])

# Define xor for contract setup
xor = OperatorPOWL(operator=Operator.XOR, children=[con_set, skip])

# Define xor for payment schedule
xor_pay = OperatorPOWL(operator=Operator.XOR, children=[pay_sch, skip])

# Define xor for material sourcing
xor_mat = OperatorPOWL(operator=Operator.XOR, children=[mat_src, skip])

# Define xor for artwork creation
xor_art = OperatorPOWL(operator=Operator.XOR, children=[art_crt, skip])

# Define xor for quality check
xor_qual = OperatorPOWL(operator=Operator.XOR, children=[qual_chk, skip])

# Define xor for frame selection
xor_frm = OperatorPOWL(operator=Operator.XOR, children=[frm_sel, skip])

# Define xor for packaging preparation
xor_pack = OperatorPOWL(operator=Operator.XOR, children=[pack_prep, skip])

# Define xor for shipment arrangement
xor_ship = OperatorPOWL(operator=Operator.XOR, children=[ship_arr, skip])

# Define xor for delivery confirmation
xor_del = OperatorPOWL(operator=Operator.XOR, children=[del_conf, skip])

# Define xor for post-sale support
xor_psu = OperatorPOWL(operator=Operator.XOR, children=[psu, skip])

# Define xor for revision management
xor_rev = OperatorPOWL(operator=Operator.XOR, children=[rev_man, skip])

# Define xor for delay mitigation
xor_delay = OperatorPOWL(operator=Operator.XOR, children=[delay_mit, skip])

# Define root node with all activities
root = StrictPartialOrder(nodes=[inq, c_onb, f_cycle_loop, xor, xor_pay, xor_mat, xor_art, xor_qual, xor_frm, xor_pack, xor_ship, xor_del, xor_psu, xor_rev, xor_delay])

# Define dependencies
root.order.add_edge(inq, c_onb)
root.order.add_edge(c_onb, f_cycle_loop)
root.order.add_edge(f_cycle_loop, xor)
root.order.add_edge(xor, xor_pay)
root.order.add_edge(xor_pay, xor_mat)
root.order.add_edge(xor_mat, xor_art)
root.order.add_edge(xor_art, xor_qual)
root.order.add_edge(xor_qual, xor_frm)
root.order.add_edge(xor_frm, xor_pack)
root.order.add_edge(xor_pack, xor_ship)
root.order.add_edge(xor_ship, xor_del)
root.order.add_edge(xor_del, xor_psu)
root.order.add_edge(xor_psu, xor_rev)
root.order.add_edge(xor_rev, xor_delay)