def mock_all_tables(dal):
    mock_links(dal)

def mock_lines(dal):
    lines = [
        {
            "line_id": 1,
            "line_ref": "T1",
            "line_name": "T1",
            "line_dest": "QUETIGNY Centre",
            "line_way": "A"
        },
        {
            "line_id": 2,
            "line_ref": "T1",
            "line_name": "T1",
            "line_dest": "DIJON Gare",
            "line_way": "R"
        }
    ]
    dal.connection.execute(dal.lines.insert(), lines)

def mock_stops(dal):
    stops = [
        { "stop_id": 1, "stop_name": "Poincaré" },
        { "stop_id": 2, "stop_name": "Auditorium" },
        { "stop_id": 3, "stop_name": "République" },
        { "stop_id": 4, "stop_name": "Godrans" },
        { "stop_id": 5, "stop_name": "Darcy" },
    ]
    dal.connection.execute(dal.stops.insert(), stops)

def mock_links(dal):
    mock_lines(dal)
    mock_stops(dal)
    links = [
        {
            "link_id": 1,
            "stop_id": 1,
            "line_id": 1,
            "stop_ref": "7854"
        },
        {
            "link_id": 2,
            "stop_id": 2,
            "line_id": 1,
            "stop_ref": "4568"
        },
        {
            "link_id": 3,
            "stop_id": 3,
            "line_id": 2,
            "stop_ref": "4986"
        },
        {
            "link_id": 4,
            "stop_id": 4,
            "line_id": 2,
            "stop_ref": "9974"
        },
        {
            "link_id": 5,
            "stop_id": 1,
            "line_id": 2,
            "stop_ref": "7946"
        },
    ]
    dal.connection.execute(dal.links.insert(), links)
