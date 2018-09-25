
from datetime import timedelta
from openerp import fields, models, api, exceptions

class Session(models.Model):
        _name = 'openacademy.session'

        name = fields.Char(required=True)
        start_date = fields.Date(default=fields.Date.today)
        duration = fields.Float(digits=(6,2), help="Duration in hours")
        seats = fields.Integer(string="Number of seats")
        active = fields.Boolean(default=True)
        instructor_id = fields.Many2one('res.partner', string="Instructor",
                                        domain=['|' ,
                                            ( "instructor","=", True),
                                            ("category_id.name","ilike","Teacher")])
        course_id = fields.Many2one('openacademy.source',
        ondelete= 'cascade', string= "Course", required=True)
        attendee_ids = fields.Many2many('res.partner', string='Attendees')

        taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')

        end_date = fields.Date(string="End Date", store=True,
                               compute= '_get_end_date', inverse='_set_end_date')

        hours = fields.Float(string="Duration in hours",
                            compute='_get_hours', inverse='_set_hours')

        attendees_count = fields.Integer(
            string="Attendees Count", compute='_get_attendees_count', store=True
        )

        color = fields.Integer()

        state = fields.Selection([
            ('draft',"Draft"),
            ('confirmed',"Confirmed"),
             ('done',"Done")
        ], default='draft', readonly= "True")

        @api.multi
        def action_draft(self):
            self.state = 'draft'

        @api.multi
        def action_confirm(self):
            self.state = 'confirmed'

        @api.multi
        def action_done(self):
            self.state = 'done'

        @api.one #revisa todas las variables
        @api.depends('seats','attendee_ids') #define cuales variables usaremos
        def _taken_seats(self):
            if not self.seats:
                self.taken_seats = 0.0
            else:
                self.taken_seats = 100.0 * len(self.attendee_ids)/ self.seats

        @api.one
        @api.depends('start_date','duration')
        def _get_end_date(self):
            if not (self.start_date and self.duration):
                self.end_date = self.start_date
                return


            start = fields.Datetime.from_string(self.start_date)
            duration = timedelta(days=self.duration, seconds=-1)
            self.end_date = start + duration

        @api.one
        @api.depends('attendee_ids')
        def _get_attendees_count(self):
            self.attendees_count = len(self.attendee_ids)

        @api.depends('duration')
        def _get_hours(self):
            for r in self:
                r.hours = r.duration * 24

        def _set_hours(self):
             for r in self:
                r.duration = r.hours / 24

        @api.one
        def _set_end_date(self):

            if not (self.start_date and self.end_date):
                return

            start_date = fields.Datetime.from_string(self.start_date)
            end_date = fields.Datetime.from_string(self.end_date)
            self.duration = (end_date - start_date).days + 1

        @api.onchange('seats','attendee_ids')
        def _verify_valid_seats(self):
            if self.seats < 0:
                return{
                    'warning':{
                        'title':"incorrect 'seats' value",
                        'message': "the number of available seat may not be negative",
                    },
                }
            if self.seats < len(self.attendee_ids):
                return{
                    'warning':{
                        'title':"Too many attendees",
                        'message':"Increase seats or remove excess attendees",
                    },
                }
        @api.one
        @api.constrains('instructor_id','attendee_ids')
        def _check_instructor_not_in_attendees(self):
            if self.instructor_id and self.instructor_id in self.attendee_ids:
                raise exceptions.ValidationError("A session's instructor can't be an attendee")
