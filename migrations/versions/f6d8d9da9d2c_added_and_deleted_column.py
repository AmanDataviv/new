"""Added and deleted column

Revision ID: f6d8d9da9d2c
Revises: efa73783a694
Create Date: 2025-03-11 11:20:33.696961

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6d8d9da9d2c'
down_revision: Union[str, None] = 'efa73783a694'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("books-author",
                    sa.Column('id',sa.Integer,primary_key=True),
                    sa.Column("Description",sa.String(60),nullable=True))


def downgrade() -> None:
    op.drop_table("books-author")
