"""empty message

Revision ID: f6f9bb3e2f05
Revises: 7f00a119938e
Create Date: 2019-07-31 14:05:27.376419

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f6f9bb3e2f05'
down_revision = '7f00a119938e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('salescosts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=20), nullable=True),
    sa.Column('sales_type', sa.String(length=20), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('eggcosts')
    op.drop_table('croptypes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('croptypes',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('crop_type', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('cost', mysql.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('eggcosts',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('size', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('cost', mysql.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('salescosts')
    # ### end Alembic commands ###