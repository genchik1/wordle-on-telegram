"""empty message

Revision ID: 92da04d0453e
Revises: f60d097494da
Create Date: 2024-02-29 12:03:11.916399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92da04d0453e'
down_revision: Union[str, None] = 'f60d097494da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_words', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('user_words', sa.Column('modified_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_words', 'created_at')
    op.drop_column('user_words', 'modified_at')
    # ### end Alembic commands ###