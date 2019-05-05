mock_lines_xml = """
    <xmldata>
        <erreur code="000"/>
        <heure>14:55</heure>
        <date>2019-04-29</date>
        <expire>55200</expire>
        <alss nb="58">
            <als id="1">
                <arret>
                    <code/>
                    <nom/>
                </arret>
                <ligne>
                    <code>T1</code>
                    <nom>T1</nom>
                    <sens>A</sens>
                    <vers>QUETIGNY Centre</vers>
                    <couleur>13369548</couleur>
                </ligne>
                <refs/>
            </als>
            <als id="2">
                <arret>
                    <code/>
                    <nom/>
                </arret>
                <ligne>
                    <code>T1</code>
                    <nom>T1</nom>
                    <sens>R</sens>
                    <vers>DIJON Gare</vers>
                    <couleur>13369548</couleur>
                </ligne>
                <refs/>
            </als>
        </alss>
    </xmldata>
    """

mock_stops_xml = """
    <xmldata>
        <erreur code="000"/>
        <heure>12:17</heure>
        <date>2019-05-04</date>
        <expire>64680</expire>
        <alss nb="17">
            <als id="1">
                <arret>
                    <code>1542</code>
                    <nom>Auditorium</nom>
                </arret>
                <ligne>
                    <code>T1</code>
                    <nom>T1</nom>
                    <sens>A</sens>
                    <vers>QUETIGNY Centre</vers>
                    <couleur>13369548</couleur>
                </ligne>
                <refs>274400518|274399749|274401798</refs>
            </als>
            <als id="2">
                <arret>
                    <code>1545</code>
                    <nom>Cap Vert</nom>
                </arret>
                <ligne>
                    <code>T1</code>
                    <nom>T1</nom>
                    <sens>A</sens>
                    <vers>QUETIGNY Centre</vers>
                    <couleur>13369548</couleur>
                </ligne>
                <refs>274400527|274399758|274401807</refs>
            </als>
        </alss>
    </xmldata>
    """
