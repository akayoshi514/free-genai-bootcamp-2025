from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

WordDbModel = Table(
    "words",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("kanji", String, nullable=False),
    Column("romaji", String, nullable=False),
    Column("english", String, nullable=False),
#    parts = Column(JSON, nullable=False)
    
#    groups = relationship('Group', secondary='word_groups', back_populates='words')
#    review_items = relationship('WordReviewItem', back_populates='word') 

)
