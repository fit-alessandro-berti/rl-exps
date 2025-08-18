root = StrictPartialOrder(
    nodes=[
        Transition(label='Seed Select'),
        Transition(label='Germinate Seeds'),
        Transition(label='Transplant Seedlings'),
        Transition(label='Mix Nutrients'),
        Transition(label='Adjust pH'),
        Transition(label='Monitor Climate'),
        Transition(label='Control Humidity'),
        Transition(label='CO2 Regulation'),
        Transition(label='Detect Pests'),
        Transition(label='Deploy Biocontrols'),
        Transition(label='Schedule Harvest'),
        Transition(label='Automate Picking'),
        Transition(label='Package Produce'),
        Transition(label='Compost Waste'),
        Transition(label='Recycle Water'),
        Transition(label='Data Logging'),
        Transition(label='System Maintenance')
    ],
    order={
        ('Seed Select', 'Germinate Seeds'): OperatorPOWL(operator=Operator.XOR, children=['Germinate Seeds', 'Transplant Seedlings']),
        ('Germinate Seeds', 'Transplant Seedlings'): OperatorPOWL(operator=Operator.XOR, children=['Transplant Seedlings', 'Mix Nutrients']),
        ('Transplant Seedlings', 'Mix Nutrients'): OperatorPOWL(operator=Operator.XOR, children=['Mix Nutrients', 'Adjust pH']),
        ('Mix Nutrients', 'Adjust pH'): OperatorPOWL(operator=Operator.XOR, children=['Adjust pH', 'Monitor Climate']),
        ('Adjust pH', 'Monitor Climate'): OperatorPOWL(operator=Operator.XOR, children=['Monitor Climate', 'Control Humidity']),
        ('Monitor Climate', 'Control Humidity'): OperatorPOWL(operator=Operator.XOR, children=['Control Humidity', 'CO2 Regulation']),
        ('Control Humidity', 'CO2 Regulation'): OperatorPOWL(operator=Operator.XOR, children=['CO2 Regulation', 'Detect Pests']),
        ('CO2 Regulation', 'Detect Pests'): OperatorPOWL(operator=Operator.XOR, children=['Detect Pests', 'Deploy Biocontrols']),
        ('Detect Pests', 'Deploy Biocontrols'): OperatorPOWL(operator=Operator.XOR, children=['Deploy Biocontrols', 'Schedule Harvest']),
        ('Deploy Biocontrols', 'Schedule Harvest'): OperatorPOWL(operator=Operator.XOR, children=['Schedule Harvest', 'Automate Picking']),
        ('Schedule Harvest', 'Automate Picking'): OperatorPOWL(operator=Operator.XOR, children=['Automate Picking', 'Package Produce']),
        ('Automate Picking', 'Package Produce'): OperatorPOWL(operator=Operator.XOR, children=['Package Produce', 'Compost Waste']),
        ('Package Produce', 'Compost Waste'): OperatorPOWL(operator=Operator.XOR, children=['Compost Waste', 'Recycle Water']),
        ('Compost Waste', 'Recycle Water'): OperatorPOWL(operator=Operator.XOR, children=['Recycle Water', 'Data Logging']),
        ('Recycle Water', 'Data Logging'): OperatorPOWL(operator=Operator.XOR, children=['Data Logging', 'System Maintenance']),
        ('Data Logging', 'System Maintenance'): OperatorPOWL(operator=Operator.XOR, children=['System Maintenance', 'Seed Select'])
    }
)