import datetime
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    file_name="[source file path]",
    code="import pandas as pd\nimport matplotlib.pyplot as plt\n\ndf = pd.read_csv('tests/simple_data.csv')\nplt.imsave('simple_data.png', df)\n",
    working_directory="dummy_linea_repo/",
    libraries=[
        Library(
            id=get_new_id(),
            name="matplotlib.pyplot",
        ),
        Library(
            id=get_new_id(),
            name="pandas",
        ),
    ],
)
call_4 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    lineno=5,
    col_offset=0,
    end_lineno=5,
    end_col_offset=33,
    arguments=[
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=0,
            value_node_id=LiteralNode(
                id=get_new_id(),
                session_id=session.id,
                lineno=5,
                col_offset=11,
                end_lineno=5,
                end_col_offset=28,
                value="simple_data.png",
            ).id,
        ).id,
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=1,
            value_node_id=VariableNode(
                id=get_new_id(),
                session_id=session.id,
                source_node_id=CallNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=4,
                    col_offset=0,
                    end_lineno=4,
                    end_col_offset=41,
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                lineno=4,
                                col_offset=17,
                                end_lineno=4,
                                end_col_offset=40,
                                value="tests/simple_data.csv",
                            ).id,
                        ).id
                    ],
                    function_id=CallNode(
                        id=get_new_id(),
                        session_id=session.id,
                        lineno=4,
                        col_offset=5,
                        end_lineno=4,
                        end_col_offset=16,
                        arguments=[
                            ArgumentNode(
                                id=get_new_id(),
                                session_id=session.id,
                                positional_order=0,
                                value_node_id=ImportNode(
                                    id=get_new_id(),
                                    session_id=session.id,
                                    lineno=1,
                                    col_offset=0,
                                    end_lineno=1,
                                    end_col_offset=19,
                                    library=Library(
                                        id=get_new_id(),
                                        name="pandas",
                                    ),
                                    alias="pd",
                                ).id,
                            ).id,
                            ArgumentNode(
                                id=get_new_id(),
                                session_id=session.id,
                                positional_order=1,
                                value_node_id=LiteralNode(
                                    id=get_new_id(),
                                    session_id=session.id,
                                    value="read_csv",
                                ).id,
                            ).id,
                        ],
                        function_id=LookupNode(
                            id=get_new_id(),
                            session_id=session.id,
                            name="getattr",
                        ).id,
                    ).id,
                ).id,
                assigned_variable_name="df",
            ).id,
        ).id,
    ],
    function_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        lineno=5,
        col_offset=0,
        end_lineno=5,
        end_col_offset=10,
        arguments=[
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=0,
                value_node_id=ImportNode(
                    id=get_new_id(),
                    session_id=session.id,
                    lineno=2,
                    col_offset=0,
                    end_lineno=2,
                    end_col_offset=31,
                    library=Library(
                        id=get_new_id(),
                        name="matplotlib.pyplot",
                    ),
                    alias="plt",
                ).id,
            ).id,
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=1,
                value_node_id=LiteralNode(
                    id=get_new_id(),
                    session_id=session.id,
                    value="imsave",
                ).id,
            ).id,
        ],
        function_id=LookupNode(
            id=get_new_id(),
            session_id=session.id,
            name="getattr",
        ).id,
    ).id,
)