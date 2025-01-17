# -*- coding: utf-8 -*-
#
# django-agpl -- tools to aid releasing Django projects under the AGPL
# Copyright (C) 2008, 2009, 2016 Chris Lamb <chris@chris-lamb.co.uk>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.urls import re_path

from . import views


urlpatterns = (
    re_path(r'^tar$', views.tar,
        name='download-tar'),
    re_path(r'^zip$', views.zip,
        name='download-zip'),
    re_path(r'^targz$', views.targz,
        name='download-targz'),
    re_path(r'^tarbz2$', views.tarbz2,
        name='download-tarbz2'),
)
