from openerp import models, fields, api

class openacademy(models.Model):
     _name = 'openacademy.source'

     name = fields.Char(string='name',required=True)
     description = fields.Text(string='Description')
     responsible_id = fields.Many2one('res.users',
                                       ondelete='set null', string="responsible", index=True )
     session_ids = fields.One2many('openacademy.session', 'course_id', string = "Sessions")
