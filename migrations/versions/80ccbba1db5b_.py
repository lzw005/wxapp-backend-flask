"""empty message

Revision ID: 80ccbba1db5b
Revises: 
Create Date: 2019-04-19 15:10:48.429033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80ccbba1db5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_info',
    sa.Column('openid', sa.String(length=50), nullable=False),
    sa.Column('nickName', sa.String(length=20), nullable=True),
    sa.Column('gender', sa.String(length=5), nullable=True),
    sa.Column('city', sa.String(length=20), nullable=True),
    sa.Column('province', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('openid'),
    mysql_collate='utf8_general_ci'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_info')
    # ### end Alembic commands ###
