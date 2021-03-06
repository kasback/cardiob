# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import Date


class Cardiologieb(models.Model):
    _name = 'cardiologieb.cardiologieb'


class Resident(models.Model):
    _name = 'cardiologieb.resident'

    nom = fields.Char()
    prenom = fields.Char()
    secteur = fields.Many2one('cardiologieb.secteur')
    chambre = fields.Many2one('cardiologieb.chambre')
    gardes = fields.One2many('cardiologieb.garde','resident')

    def _secteur_onchange(self):
          res = {}
          res['domain'] = {'chambre': [('secteur_id', '=', self.secteur.id)]}
          return res


class Secteur(models.Model):
    _name = 'cardiologieb.secteur'

    nom = fields.Char()
    chambres = fields.One2many('cardiologieb.chambre', 'secteur_id')


class Chambre(models.Model):
    _name = 'cardiologieb.chambre'

    nom = fields.Char()
    secteur_id = fields.Many2one('cardiologieb.secteur')

class Garde(models.Model):
    _name = 'cardiologieb.garde'
    today = Date.today()
    nom = fields.Char()
    date_garde = fields.Date(today)
    resident = fields.Many2one('cardiologieb.resident')


