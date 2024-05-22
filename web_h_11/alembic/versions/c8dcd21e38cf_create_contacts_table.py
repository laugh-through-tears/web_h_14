"""create_contacts_table

Revision ID: c8dcd21e38cf
Revises:
Create Date: 2024-05-06 12:00:00.000000

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8dcd21e38cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'contacts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String),
        sa.Column('last_name', sa.String),
        sa.Column('email', sa.String, index=True, unique=True),
        sa.Column('birthday', sa.DateTime),
    )


def downgrade():
    op.drop_table('contacts')
