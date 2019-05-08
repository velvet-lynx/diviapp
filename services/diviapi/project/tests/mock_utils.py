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

mock_stop_xml = """
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
        </alss>
    </xmldata>
    """

mock_times_xml = """
    <xmldata>
        <erreur code="000"/>
        <heure>14:53</heure>
        <date>2019-05-08</date>
        <reseau>
            <titre/>
            <texte/>
            <bloquant>false</bloquant>
        </reseau>
        <horaires nb="3">
            <horaire id="1">
                <description>
                    <code>1542</code>
                    <arret>Auditorium</arret>
                    <ligne>T1</ligne>
                    <ligne_nom>T1</ligne_nom>
                    <sens>A</sens>
                    <vers>QUETIGNY Centre</vers>
                    <couleur>#cc00cc</couleur>
                </description>
                <passages nb="0"></passages>
                <messages nb="0"></messages>
            </horaire>
            <horaire id="2">
                <description>
                    <code>1542</code>
                    <arret>Auditorium</arret>
                    <ligne>T1</ligne>
                    <ligne_nom>T1</ligne_nom>
                    <sens>A</sens>
                    <vers>QUETIGNY Centre</vers>
                    <couleur>#cc00cc</couleur>
                </description>
                <passages nb="2">
                    <passage id="1">
                        <duree>14:58</duree>
                        <destination>QUETIGNY</destination>
                    </passage>
                    <passage id="2">
                        <duree>15:05</duree>
                        <destination>QUETIGNY</destination>
                    </passage>
                </passages>
                <messages nb="0"></messages>
            </horaire>
            <horaire id="3">
                <description>
                    <code/>
                    <arret/>
                    <ligne/>
                    <ligne_nom/>
                    <sens/>
                    <vers/>
                    <couleur>#000000</couleur>
                </description>
                <passages nb="0"/>
                <messages nb="0"></messages>
            </horaire>
        </horaires>
    </xmldata>
    """
