"""add content column to posts table

Revision ID: a83427e093e5
Revises: b153e6b6e3ac
Create Date: 2025-11-23 02:49:19.488553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a83427e093e5'
down_revision: Union[str, Sequence[str], None] = 'b153e6b6e3ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
