"""Initial

Revision ID: 6785e9067208
Revises: bd574bfde8a2
Create Date: 2024-07-02 11:35:22.877649

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '6785e9067208'
down_revision: Union[str, None] = 'bd574bfde8a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=60),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
    # ### end Alembic commands ###
