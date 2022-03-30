from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Order(models.Model):
    _name = 'handphone.order'
    _description = 'New Description'

    orderandroiddetail_ids = fields.One2many(
        comodel_name='handphone.orderandroiddetail', 
        inverse_name='order_id', 
        string='Order Hp Android')

    orderiosdetail_ids = fields.One2many(
        comodel_name='handphone.orderiosdetail', 
        inverse_name='orderk_id', 
        string='Order Hp Ios')

    name = fields.Char(string='Kode Order', required=True)
    tanggal_pesan = fields.Datetime('Tanggal Pemesanan',default=fields.Datetime.now())
    tanggal_pengiriman = fields.Date(string='Tanggal Pengiriman', default=fields.Date.today())
    pemesan = fields.Many2one(
        comodel_name='res.partner', 
        string='Pemesan', 
        domain=[('is_customernya','=', True)],store=True)


    total = fields.Integer(compute='_compute_total', string='Total', store=True)

    @api.depends('orderandroiddetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['handphone.orderandroiddetail'].search([('order_id', '=', record.id)]).mapped('harga'))
            b = sum(self.env['handphone.orderiosdetail'].search([('orderk_id', '=', record.id)]).mapped('harga'))
            record.total = a + b

    sudah_kembali = fields.Boolean(string='Sudah Dikembalikan', default=False)

     
class OrderAndroidDetail(models.Model):
        _name = 'handphone.orderandroiddetail'
        _description = 'New Description'
    
        order_id = fields.Many2one(comodel_name='handphone.order', string='Order')
        android_id = fields.Many2one(comodel_name='handphone.android', string='Android')
     

    

        name = fields.Char(string='Name')
        harga = fields.Integer(compute='_compute_harga', string='harga')
        qty = fields.Integer(string='Quantity')
        harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')

        tipe = fields.Char(compute='_compute_tipe', string='Tipe Storage')
    
        @api.depends('android_id')
        def _compute_tipe(self):
            for record in self:
                record.tipe = record.android_id.tipe
    
        
        @api.depends('android_id')
        def _compute_harga_satuan(self):
            for record in self:
                record.harga_satuan = record.android_id.harga

        @api.depends('qty','harga_satuan')
        def _compute_harga(self):
            for record in self:
                record.harga = record.harga_satuan * record.qty

        @api.model
        def create(self,vals):
            record = super(OrderAndroidDetail, self).create(vals) 
            if record.qty:
                self.env['handphone.android'].search([('id','=',record.android_id.id)]).write({'stok':record.android_id.stok-record.qty})
                return record

class OrderIosDetail(models.Model):
        _name = 'handphone.orderiosdetail'
        _description = 'New Description'
    
        orderk_id = fields.Many2one(comodel_name='handphone.order', string='Order Hp')
        ios_id = fields.Many2one(
            comodel_name='handphone.ios', 
            string='Hp Ios',
            domain=[('stok','>','100')])
    
        name = fields.Char(string='Name')
        harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')\
        
        tipe = fields.Char(compute='_compute_tipe', string='Tipe Storage')
    
        @api.depends('ios_id')
        def _compute_tipe(self):
            for record in self:
                record.tipe = record.ios_id.tipe
    
        @api.depends('ios_id')
        def _compute_harga_satuan(self):
            for record in self:
                record.harga_satuan = record.ios_id.harga
    
        qty = fields.Integer(string='Quantity')
    
        @api.constrains('qty')
        def _check_stok(self):
            for record in self:
                bahan = self.env['handphone.ios'].search([('stok', '<',record.qty)])
                if bahan:
                    raise ValidationError("Stok Tidak Cukup")
    
        harga = fields.Integer(compute='_compute_harga', string='harga')
    
        @api.depends('harga_satuan','qty')
        def _compute_harga(self):
            for record in self:
               record.harga = record.harga_satuan * record.qty
               
    
        @api.model
        def create(self,vals):
            record = super(OrderIosDetail, self).create(vals) 
            if record.qty:
                self.env['handphone.ios'].search([('id','=',record.ios_id.id)]).write({'stok':record.ios_id.stok-record.qty})
                return record
    
        
    
