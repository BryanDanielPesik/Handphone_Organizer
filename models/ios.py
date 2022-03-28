from odoo import api, fields, models


class Ios(models.Model):
    _name = 'handphone.ios'
    _description = 'Daftar Hp'

    name = fields.Char(string='Name', required=True)
    warna = fields.Selection(string='', selection=[('Merah', 'Merah'), ('Silver', 'Silver'),('Space grey', 'Space grey')])
    tipe = fields.Selection(string='Storage', selection=[('64 Gb','64 Gb'), ('128 Gb','128 Gb'), ('256 Gb', '256 Gb')])
    stok = fields.Integer(string='Stok Handphone Ios')
    harga = fields.Integer(string='Harga')
    img = fields.Binary(string='Image')
    
    
    
