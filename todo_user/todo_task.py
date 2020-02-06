#-*- coding: utf-8 -*-
from openerp import models, fields, api
class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task','mail.thread']
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help="Breve descripcion de la tarea.")

    @api.one
    def do_marcar(self):
        if self.user_id != self.env.user:
            raise Exception('Solo el responsable ha de marcarla como hecha!')
        else:
            return super(TodoTask, self).do_marcar()

    @api.multi
    def do_limpiar(self):
        domain = [('is_done', '=', True), '|', ('user_id', '=', self.env.uid), ('user_id', '=', False)]
        done_recs = self.search(domain)
        done_recs.write({'active': False})
        return True
