# Copyright (C) 2014  ABRT Team
# Copyright (C) 2014  Red Hat, Inc.
#
# This file is part of faf.
#
# faf is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# faf is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with faf.  If not, see <http://www.gnu.org/licenses/>.

"""
Assigning release to repository

Revision ID: 17d4911132f8
Revises: 13557f1962e6
Create Date: 2016-09-08 08:49:52.450697
"""

from alembic.op import create_table, drop_table
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '17d4911132f8'
down_revision = '13557f1962e6'


def upgrade():
    create_table('opsysreleaserepo',
                 sa.Column('opsysrelease_id', sa.Integer(), nullable=False),
                 sa.Column('repo_id', sa.Integer(), nullable=False),
                 sa.ForeignKeyConstraint(['opsysrelease_id'], ['opsysreleases.id'], ),
                 sa.ForeignKeyConstraint(['repo_id'], ['repo.id'], ),
                 sa.PrimaryKeyConstraint('opsysrelease_id', 'repo_id'),
                )


def downgrade():
    drop_table('opsysreleaserepo')
