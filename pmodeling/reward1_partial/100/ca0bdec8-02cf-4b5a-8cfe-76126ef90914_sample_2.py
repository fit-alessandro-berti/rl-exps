root = StrictPartialOrder(nodes=[
    Transition(label='Milk Sourcing'),
    Transition(label='Quality Testing'),
    Transition(label='Culture Prep'),
    Transition(label='Milk Pasteurize'),
    Transition(label='Curd Cutting'),
    Transition(label='Whey Draining'),
    Transition(label='Molding Cheese'),
    Transition(label='Pressing Blocks'),
    Transition(label='Salting Process'),
    Transition(label='Aging Monitoring'),
    Transition(label='Flavor Profiling'),
    Transition(label='Packaging Design'),
    Transition(label='Compliance Check'),
    Transition(label='Market Research'),
    Transition(label='Direct Shipping'),
    Transition(label='Customer Feedback'),
    Transition(label='Recipe Adjust')
])

# Define the dependencies between the activities
root.order.add_edge(Transition(label='Milk Sourcing'), Transition(label='Quality Testing'))
root.order.add_edge(Transition(label='Quality Testing'), Transition(label='Culture Prep'))
root.order.add_edge(Transition(label='Culture Prep'), Transition(label='Milk Pasteurize'))
root.order.add_edge(Transition(label='Milk Pasteurize'), Transition(label='Curd Cutting'))
root.order.add_edge(Transition(label='Curd Cutting'), Transition(label='Whey Draining'))
root.order.add_edge(Transition(label='Whey Draining'), Transition(label='Molding Cheese'))
root.order.add_edge(Transition(label='Molding Cheese'), Transition(label='Pressing Blocks'))
root.order.add_edge(Transition(label='Pressing Blocks'), Transition(label='Salting Process'))
root.order.add_edge(Transition(label='Salting Process'), Transition(label='Aging Monitoring'))
root.order.add_edge(Transition(label='Aging Monitoring'), Transition(label='Flavor Profiling'))
root.order.add_edge(Transition(label='Flavor Profiling'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Packaging Design'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Market Research'))
root.order.add_edge(Transition(label='Market Research'), Transition(label='Direct Shipping'))
root.order.add_edge(Transition(label='Direct Shipping'), Transition(label='Customer Feedback'))
root.order.add_edge(Transition(label='Customer Feedback'), Transition(label='Recipe Adjust'))

# Define the loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Transition(label='Quality Testing'), Transition(label='Culture Prep')])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Transition(label='Milk Pasteurize'), Transition(label='Curd Cutting')])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Transition(label='Whey Draining'), Transition(label='Molding Cheese')])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Transition(label='Pressing Blocks'), Transition(label='Salting Process')])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Transition(label='Aging Monitoring'), Transition(label='Flavor Profiling')])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Transition(label='Packaging Design'), Transition(label='Compliance Check')])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[Transition(label='Market Research'), Transition(label='Direct Shipping')])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[Transition(label='Customer Feedback'), Transition(label='Recipe Adjust')])
root.order.add_edge(loop1, Transition(label='Quality Testing'))
root.order.add_edge(loop2, Transition(label='Curd Cutting'))
root.order.add_edge(loop3, Transition(label='Whey Draining'))
root.order.add_edge(loop4, Transition(label='Pressing Blocks'))
root.order.add_edge(loop5, Transition(label='Salting Process'))
root.order.add_edge(loop6, Transition(label='Aging Monitoring'))
root.order.add_edge(loop7, Transition(label='Flavor Profiling'))
root.order.add_edge(loop8, Transition(label='Packaging Design'))

# Define the choices
choice1 = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Quality Testing'), Transition(label='Culture Prep')])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Milk Pasteurize'), Transition(label='Curd Cutting')])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Whey Draining'), Transition(label='Molding Cheese')])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Pressing Blocks'), Transition(label='Salting Process')])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Aging Monitoring'), Transition(label='Flavor Profiling')])
choice6 = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Packaging Design'), Transition(label='Compliance Check')])
choice7 = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Market Research'), Transition(label='Direct Shipping')])
choice8 = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Customer Feedback'), Transition(label='Recipe Adjust')])
root.order.add_edge(Transition(label='Quality Testing'), choice1)
root.order.add_edge(Transition(label='Culture Prep'), choice1)
root.order.add_edge(Transition(label='Milk Pasteurize'), choice2)
root.order.add_edge(Transition(label='Curd Cutting'), choice2)
root.order.add_edge(Transition(label='Whey Draining'), choice3)
root.order.add_edge(Transition(label='Molding Cheese'), choice3)
root.order.add_edge(Transition(label='Pressing Blocks'), choice4)
root.order.add_edge(Transition(label='Salting Process'), choice4)
root.order.add_edge(Transition(label='Aging Monitoring'), choice5)
root.order.add_edge(Transition(label='Flavor Profiling'), choice5)
root.order.add_edge(Transition(label='Packaging Design'), choice6)
root.order.add_edge(Transition(label='Compliance Check'), choice6)
root.order.add_edge(Transition(label='Market Research'), choice7)
root.order.add_edge(Transition(label='Direct Shipping'), choice7)
root.order.add_edge(Transition(label='Customer Feedback'), choice8)
root.order.add_edge(Transition(label='Recipe Adjust'), choice8)