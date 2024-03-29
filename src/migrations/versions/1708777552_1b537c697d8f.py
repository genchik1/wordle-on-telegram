"""empty message

Revision ID: 1b537c697d8f
Revises: aeb8bb832155
Create Date: 2024-02-24 12:25:52.994169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1b537c697d8f'
down_revision: Union[str, None] = 'aeb8bb832155'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_words_m2m', sa.Column('is_guessed', sa.Boolean(), nullable=True))
    op.add_column('user_words_m2m', sa.Column('day', sa.Date(), nullable=True))
    op.add_column('user_words_m2m', sa.Column('words', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    op.drop_constraint('user_words_m2m_word_id_fkey', 'user_words_m2m', type_='foreignkey')
    op.drop_table_comment(
        'user_words_m2m',
        existing_comment='Ассоциативная таблица для связи угаданных юзером слов.',
        schema=None
    )
    op.drop_column('user_words_m2m', 'word_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_words_m2m', sa.Column('word_id', sa.UUID(), autoincrement=False, nullable=False))
    op.create_table_comment(
        'user_words_m2m',
        'Ассоциативная таблица для связи угаданных юзером слов.',
        existing_comment=None,
        schema=None
    )
    op.create_foreign_key('user_words_m2m_word_id_fkey', 'user_words_m2m', 'words', ['word_id'], ['id'])
    op.drop_column('user_words_m2m', 'words')
    op.drop_column('user_words_m2m', 'day')
    op.drop_column('user_words_m2m', 'is_guessed')
    # ### end Alembic commands ###
