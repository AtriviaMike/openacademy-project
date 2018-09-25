from openerp import models, fields, api

class openacademy(models.Model):
    _name = 'openacademy.source'

    name = fields.Char(string='name',required=True)
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users',ondelete='set null', string="responsible", index=True )
    session_ids = fields.One2many('openacademy.session', 'course_id', string = "Sessions")
    _sql_constraint = [(
        'name_description_check',
        'CHECK(name != description)',
        "The title of the course should not be the description",),
        ('name_unique',
        'UNIQUE(name)',
        "The course title must be unique")
    ]

    @api.one
    def copy(self, default=None):
        default['name'] = self.name + '[COPY]'

        copied_count = self.search_count([('name','=like', u"{} [COPY]".format(self.name))])

        if not copied_count:
            new_name= u"{} [COPY]".format(self.name)
        else:
            new_name= u"{} [COPY]({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(openacademy, self).copy(default)
