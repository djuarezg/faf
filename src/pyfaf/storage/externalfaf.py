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

from sqlalchemy.sql.schema import Column
from sqlalchemy.types import Integer, String

from .generic_table import GenericTable


class ExternalFafInstance(GenericTable):
    __tablename__ = "externalfafinstances"

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, index=True)
    baseurl = Column(String(1024), nullable=False)
