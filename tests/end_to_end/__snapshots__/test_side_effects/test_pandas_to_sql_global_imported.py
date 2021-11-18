import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

source_1 = SourceCode(
    code="""from lineapy import save, db
import pandas as pd
import sqlite3

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
conn = sqlite3.connect(\':memory:\')
df.to_sql(name="test", con=conn,index=False)

save(db, "db")
""",
    location=PosixPath("[source file path]"),
)
import_1 = ImportNode(
    source_location=SourceLocation(
        lineno=1,
        col_offset=0,
        end_lineno=1,
        end_col_offset=28,
        source_code=source_1.id,
    ),
    library=Library(
        name="lineapy",
    ),
)
call_14 = CallNode(
    source_location=SourceLocation(
        lineno=9,
        col_offset=0,
        end_lineno=9,
        end_col_offset=14,
        source_code=source_1.id,
    ),
    function_id=CallNode(
        function_id=LookupNode(
            name="getattr",
        ).id,
        positional_args=[
            import_1.id,
            LiteralNode(
                value="save",
            ).id,
        ],
    ).id,
    positional_args=[
        MutateNode(
            source_id=CallNode(
                function_id=LookupNode(
                    name="getattr",
                ).id,
                positional_args=[
                    import_1.id,
                    LiteralNode(
                        value="db",
                    ).id,
                ],
            ).id,
            call_id=CallNode(
                source_location=SourceLocation(
                    lineno=7,
                    col_offset=0,
                    end_lineno=7,
                    end_col_offset=44,
                    source_code=source_1.id,
                ),
                function_id=CallNode(
                    source_location=SourceLocation(
                        lineno=7,
                        col_offset=0,
                        end_lineno=7,
                        end_col_offset=9,
                        source_code=source_1.id,
                    ),
                    function_id=LookupNode(
                        name="getattr",
                    ).id,
                    positional_args=[
                        CallNode(
                            source_location=SourceLocation(
                                lineno=5,
                                col_offset=5,
                                end_lineno=5,
                                end_col_offset=51,
                                source_code=source_1.id,
                            ),
                            function_id=CallNode(
                                source_location=SourceLocation(
                                    lineno=5,
                                    col_offset=5,
                                    end_lineno=5,
                                    end_col_offset=17,
                                    source_code=source_1.id,
                                ),
                                function_id=LookupNode(
                                    name="getattr",
                                ).id,
                                positional_args=[
                                    ImportNode(
                                        source_location=SourceLocation(
                                            lineno=2,
                                            col_offset=0,
                                            end_lineno=2,
                                            end_col_offset=19,
                                            source_code=source_1.id,
                                        ),
                                        library=Library(
                                            name="pandas",
                                        ),
                                    ).id,
                                    LiteralNode(
                                        value="DataFrame",
                                    ).id,
                                ],
                            ).id,
                            positional_args=[
                                CallNode(
                                    source_location=SourceLocation(
                                        lineno=5,
                                        col_offset=18,
                                        end_lineno=5,
                                        end_col_offset=50,
                                        source_code=source_1.id,
                                    ),
                                    function_id=LookupNode(
                                        name="l_dict",
                                    ).id,
                                    positional_args=[
                                        CallNode(
                                            function_id=LookupNode(
                                                name="l_tuple",
                                            ).id,
                                            positional_args=[
                                                LiteralNode(
                                                    source_location=SourceLocation(
                                                        lineno=5,
                                                        col_offset=19,
                                                        end_lineno=5,
                                                        end_col_offset=22,
                                                        source_code=source_1.id,
                                                    ),
                                                    value="a",
                                                ).id,
                                                CallNode(
                                                    source_location=SourceLocation(
                                                        lineno=5,
                                                        col_offset=24,
                                                        end_lineno=5,
                                                        end_col_offset=33,
                                                        source_code=source_1.id,
                                                    ),
                                                    function_id=LookupNode(
                                                        name="l_list",
                                                    ).id,
                                                    positional_args=[
                                                        LiteralNode(
                                                            source_location=SourceLocation(
                                                                lineno=5,
                                                                col_offset=25,
                                                                end_lineno=5,
                                                                end_col_offset=26,
                                                                source_code=source_1.id,
                                                            ),
                                                            value=1,
                                                        ).id,
                                                        LiteralNode(
                                                            source_location=SourceLocation(
                                                                lineno=5,
                                                                col_offset=28,
                                                                end_lineno=5,
                                                                end_col_offset=29,
                                                                source_code=source_1.id,
                                                            ),
                                                            value=2,
                                                        ).id,
                                                        LiteralNode(
                                                            source_location=SourceLocation(
                                                                lineno=5,
                                                                col_offset=31,
                                                                end_lineno=5,
                                                                end_col_offset=32,
                                                                source_code=source_1.id,
                                                            ),
                                                            value=3,
                                                        ).id,
                                                    ],
                                                ).id,
                                            ],
                                        ).id,
                                        CallNode(
                                            function_id=LookupNode(
                                                name="l_tuple",
                                            ).id,
                                            positional_args=[
                                                LiteralNode(
                                                    source_location=SourceLocation(
                                                        lineno=5,
                                                        col_offset=35,
                                                        end_lineno=5,
                                                        end_col_offset=38,
                                                        source_code=source_1.id,
                                                    ),
                                                    value="b",
                                                ).id,
                                                CallNode(
                                                    source_location=SourceLocation(
                                                        lineno=5,
                                                        col_offset=40,
                                                        end_lineno=5,
                                                        end_col_offset=49,
                                                        source_code=source_1.id,
                                                    ),
                                                    function_id=LookupNode(
                                                        name="l_list",
                                                    ).id,
                                                    positional_args=[
                                                        LiteralNode(
                                                            source_location=SourceLocation(
                                                                lineno=5,
                                                                col_offset=41,
                                                                end_lineno=5,
                                                                end_col_offset=42,
                                                                source_code=source_1.id,
                                                            ),
                                                            value=4,
                                                        ).id,
                                                        LiteralNode(
                                                            source_location=SourceLocation(
                                                                lineno=5,
                                                                col_offset=44,
                                                                end_lineno=5,
                                                                end_col_offset=45,
                                                                source_code=source_1.id,
                                                            ),
                                                            value=5,
                                                        ).id,
                                                        LiteralNode(
                                                            source_location=SourceLocation(
                                                                lineno=5,
                                                                col_offset=47,
                                                                end_lineno=5,
                                                                end_col_offset=48,
                                                                source_code=source_1.id,
                                                            ),
                                                            value=6,
                                                        ).id,
                                                    ],
                                                ).id,
                                            ],
                                        ).id,
                                    ],
                                ).id
                            ],
                        ).id,
                        LiteralNode(
                            value="to_sql",
                        ).id,
                    ],
                ).id,
                keyword_args={
                    "con": CallNode(
                        source_location=SourceLocation(
                            lineno=6,
                            col_offset=7,
                            end_lineno=6,
                            end_col_offset=34,
                            source_code=source_1.id,
                        ),
                        function_id=CallNode(
                            source_location=SourceLocation(
                                lineno=6,
                                col_offset=7,
                                end_lineno=6,
                                end_col_offset=22,
                                source_code=source_1.id,
                            ),
                            function_id=LookupNode(
                                name="getattr",
                            ).id,
                            positional_args=[
                                ImportNode(
                                    source_location=SourceLocation(
                                        lineno=3,
                                        col_offset=0,
                                        end_lineno=3,
                                        end_col_offset=14,
                                        source_code=source_1.id,
                                    ),
                                    library=Library(
                                        name="sqlite3",
                                    ),
                                ).id,
                                LiteralNode(
                                    value="connect",
                                ).id,
                            ],
                        ).id,
                        positional_args=[
                            LiteralNode(
                                source_location=SourceLocation(
                                    lineno=6,
                                    col_offset=23,
                                    end_lineno=6,
                                    end_col_offset=33,
                                    source_code=source_1.id,
                                ),
                                value=":memory:",
                            ).id
                        ],
                    ).id,
                    "index": LiteralNode(
                        source_location=SourceLocation(
                            lineno=7,
                            col_offset=38,
                            end_lineno=7,
                            end_col_offset=43,
                            source_code=source_1.id,
                        ),
                        value=False,
                    ).id,
                    "name": LiteralNode(
                        source_location=SourceLocation(
                            lineno=7,
                            col_offset=15,
                            end_lineno=7,
                            end_col_offset=21,
                            source_code=source_1.id,
                        ),
                        value="test",
                    ).id,
                },
            ).id,
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=9,
                col_offset=9,
                end_lineno=9,
                end_col_offset=13,
                source_code=source_1.id,
            ),
            value="db",
        ).id,
    ],
)