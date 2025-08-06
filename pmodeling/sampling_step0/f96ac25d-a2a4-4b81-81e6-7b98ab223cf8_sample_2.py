root = StrictPartialOrder(
    nodes=[
        Transition(label='Client Brief'),
        Transition(label='Concept Sketch'),
        Transition(label='Design Review'),
        Transition(label='Material Sourcing'),
        Transition(label='Prototype Build'),
        Transition(label='Vendor Coordination'),
        Transition(label='Quality Check'),
        Transition(label='Client Approval'),
        Transition(label='Packaging Prep'),
        Transition(label='Shipping Arrange'),
        Transition(label='Feedback Collect'),
        Transition(label='Portfolio Update'),
        Transition(label='Contract Sign'),
        Transition(label='IP Management'),
        Transition(label='Future Schedule'),
        Transition(label='Maintenance Plan'),
        OperatorPOWL(operator=Operator.LOOP, children=[
            Transition(label='Quality Check'),
            Transition(label='Feedback Collect'),
            Transition(label='Maintenance Plan'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            OperatorPOWL(operator=Operator.LOOP, children=[
                Transition(label='Packaging Prep'),
                Transition(label='Shipping Arrange'),
            ]),
            Transition(label='Client Approval'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Client Brief'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Concept Sketch'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Design Review'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Material Sourcing'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Prototype Build'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Vendor Coordination'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Quality Check'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Packaging Prep'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Shipping Arrange'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Feedback Collect'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Portfolio Update'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Contract Sign'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='IP Management'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Future Schedule'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Maintenance Plan'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Concept Sketch'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Design Review'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Material Sourcing'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Prototype Build'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Vendor Coordination'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Quality Check'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Packaging Prep'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Shipping Arrange'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Feedback Collect'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Portfolio Update'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Contract Sign'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='IP Management'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Future Schedule'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Maintenance Plan'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Concept Sketch'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Design Review'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Material Sourcing'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Prototype Build'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Vendor Coordination'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Quality Check'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Packaging Prep'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Shipping Arrange'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Feedback Collect'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Portfolio Update'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Contract Sign'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='IP Management'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Future Schedule'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Maintenance Plan'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Concept Sketch'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Design Review'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Material Sourcing'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Prototype Build'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Vendor Coordination'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Quality Check'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Packaging Prep'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Shipping Arrange'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Feedback Collect'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Portfolio Update'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Contract Sign'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='IP Management'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Future Schedule'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Maintenance Plan'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Concept Sketch'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Design Review'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Material Sourcing'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Prototype Build'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Vendor Coordination'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Quality Check'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Packaging Prep'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Shipping Arrange'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Feedback Collect'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Portfolio Update'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Contract Sign'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='IP Management'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Future Schedule'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Maintenance Plan'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Concept Sketch'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Design Review'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Material Sourcing'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Prototype Build'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Vendor Coordination'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Quality Check'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Packaging Prep'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Shipping Arrange'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Feedback Collect'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Portfolio Update'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Contract Sign'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='IP Management'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Future Schedule'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Maintenance Plan'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Concept Sketch'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Design Review'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Material Sourcing'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Prototype Build'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Vendor Coordination'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Quality Check'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Packaging Prep'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Shipping Arrange'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Feedback Collect'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Portfolio Update'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Contract Sign'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='IP Management'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Future Schedule'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Maintenance Plan'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Concept Sketch'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Design Review'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Material Sourcing'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Prototype Build'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Vendor Coordination'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Quality Check'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Packaging Prep'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Shipping Arrange'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Feedback Collect'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Portfolio Update'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Contract Sign'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='IP Management'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Future Schedule'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Maintenance Plan'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Concept Sketch'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Design Review'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Material Sourcing'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Prototype Build'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Vendor Coordination'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Quality Check'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Packaging Prep'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Shipping Arrange'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Feedback Collect'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Portfolio Update'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Contract Sign'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='IP Management'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Future Schedule'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Maintenance Plan'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Concept Sketch'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Design Review'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Material Sourcing'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Prototype Build'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Vendor Coordination'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Quality Check'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Packaging Prep'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Shipping Arrange'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Feedback Collect'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),
            Transition(label='Portfolio Update'),
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Client Approval'),