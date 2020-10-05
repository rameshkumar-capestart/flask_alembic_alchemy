"""empty message

Revision ID: b9cd33a040f5
Revises: 372da1df23f8
Create Date: 2020-10-05 14:41:57.418190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9cd33a040f5'
down_revision = '372da1df23f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars_company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('request_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['request_id'], ['cars.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cars_company')
    # ### end Alembic commands ###
