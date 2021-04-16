"""upgrade model patient

Revision ID: fca8f62100ce
Revises: 41b8a7172e0a
Create Date: 2021-04-15 23:35:06.406006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fca8f62100ce'
down_revision = '41b8a7172e0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'patients', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'patients', type_='unique')
    # ### end Alembic commands ###
