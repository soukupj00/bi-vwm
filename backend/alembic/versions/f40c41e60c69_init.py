"""init

Revision ID: f40c41e60c69
Revises: 
Create Date: 2023-05-11 23:00:00.452244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f40c41e60c69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.createTable(
        'songs',
        sa.column('id', sa.Integer),
        sa.column('artist', sa.String),
        sa.column('album', sa.String),
        sa.column('song', sa.String),
        sa.column('year', sa.Integer),
        sa.column('lyrics', sa.String),
    )


def downgrade():
    op.drop_table('songs')
