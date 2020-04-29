import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import orm


association_table = sqlalchemy.Table('mangas_to_genres', SqlAlchemyBase.metadata,
                                     sqlalchemy.Column('mangas', sqlalchemy.Integer,
                                                       sqlalchemy.ForeignKey('mangas.id')),
                                     sqlalchemy.Column('genres', sqlalchemy.Integer,
                                                       sqlalchemy.ForeignKey('genres.id'))
                                     )


class Genre(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'genres'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name_of_genre = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    mangas = orm.relation("Manga", secondary="mangas_to_genres", backref="genres")