"""added relationships

Revision ID: 41b8a7172e0a
Revises: 282357c9d63c
Create Date: 2021-04-13 20:57:10.847523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41b8a7172e0a'
down_revision = '282357c9d63c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('episodes', sa.Column('emergency_status', sa.String(), nullable=False))
    op.drop_column('episodes', 'urgency')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('episodes', sa.Column('urgency', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('episodes', 'emergency_status')
    # ### end Alembic commands ###
