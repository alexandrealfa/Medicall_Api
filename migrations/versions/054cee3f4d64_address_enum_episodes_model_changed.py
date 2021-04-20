"""address, enum, episodes model changed

Revision ID: 054cee3f4d64
Revises: 3977aa95b1c9
Create Date: 2021-04-19 14:17:04.128551

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '054cee3f4d64'
down_revision = '3977aa95b1c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('zip_code', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('complement', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('state', sa.Enum('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MS', 'MT', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO', name='enumstate'), server_default='PR', nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('addresss')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresss',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('zip_code', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('address_complement', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('state', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('country', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('episode_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['episode_id'], ['episodes.id'], name='addresss_episode_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='addresss_pkey')
    )
    op.drop_table('address')
    # ### end Alembic commands ###