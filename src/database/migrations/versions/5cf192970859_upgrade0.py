"""upgrade0

Revision ID: 5cf192970859
Revises: 
Create Date: 2023-09-29 15:26:07.515190

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5cf192970859'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Название города', sa.String(length=100), nullable=False),
    sa.Column('Абривиатура страны', sa.String(length=5), nullable=True),
    sa.Column('Широта', sa.Float(), nullable=False),
    sa.Column('Долгота', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weather',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Тип погоды', sa.String(length=100), nullable=False),
    sa.Column('Температура в *C', sa.Float(), nullable=False),
    sa.Column('Ощущается как', sa.Float(), nullable=False),
    sa.Column('Скорость ветра', sa.Float(), nullable=False),
    sa.Column('Описание погоды', sa.String(length=225), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather')
    op.drop_table('cities')
    # ### end Alembic commands ###