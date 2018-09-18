# -*- coding: utf-8 -*-

from openerp import models, fields, api

class openacademy(models.Model):
     _name = 'openacademy.source'

     name = fields.Char(string='name',required=True)
     description = fields.Text(string='Description')
