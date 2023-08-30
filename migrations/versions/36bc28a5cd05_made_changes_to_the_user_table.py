"""Made changes to the user table

Revision ID: 36bc28a5cd05
Revises: f7dd3cda60e7
Create Date: 2023-08-25 21:04:21.326375

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '36bc28a5cd05'
down_revision = 'f7dd3cda60e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('combined_table')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('users_username_key', type_='unique')
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
        batch_op.create_unique_constraint('users_username_key', ['username'])

    op.create_table('combined_table',
    sa.Column('abrv', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('uid', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('abbreviation', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('productionStartYear', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('productionEndYear', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('originalRunStartDate', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('originalRunEndDate', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('seasonsCount', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('episodesCount', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('featureLengthEpisodesCount', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('productionCompany', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('originalBroadcaster', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('companies_uid', sa.VARCHAR(), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###