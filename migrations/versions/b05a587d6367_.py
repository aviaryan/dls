"""empty message

Revision ID: b05a587d6367
Revises: bb6430bdeea2
Create Date: 2016-05-15 09:19:16.657777

"""

# revision identifiers, used by Alembic.
revision = 'b05a587d6367'
down_revision = 'bb6430bdeea2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('data', sa.Column('filesize', sa.Integer(), nullable=True))
    op.add_column('data', sa.Column('filetime', sa.DateTime(), nullable=True))
    op.add_column('data', sa.Column('texttime', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('data', 'texttime')
    op.drop_column('data', 'filetime')
    op.drop_column('data', 'filesize')
    ### end Alembic commands ###