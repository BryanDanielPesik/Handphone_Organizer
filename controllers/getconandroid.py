from odoo import http, fields, models
from odoo.http import request
import json


class AndroidCon(http.Controller):
    @http.route(['/android','/android/<int:idnya>'], auth='public', methods=['GET'], csrf=True)
    def getAndroid(self, idnya=None, **kwargs):
        value = []
        if not idnya:
            kursi = request.env['handphone.android'].search([])            
            for k in kursi:
                value.append({"id": k.id,
                            "namakursi"     : k.name,
                            "warna_hp"      : k.warna,
                            "tipe_hp"       : k.tipe,
                            "stok_tersedia" : k.stok,
                            "harga_beli"    : k.harga,
                            })
            return json.dumps(value)
        else:
            androidid = request.env['handphone.android'].search([('id','=',idnya)])
            for k in androidid:
                value.append({"id": k.id,
                            "namakursi"     : k.name,
                            "warna_hp"      : k.warna,
                            "tipe_hp"       : k.tipe,
                            "stok_tersedia" : k.stok,
                            "harga_beli"    : k.harga,
                            })
            return json.dumps(value)
    
    @http.route('/createandroid',auth='user', type='json', methods=['POST'])
    def createAndroid(self, **kw):    
        if request.jsonrequest:    
            if kw['name']:
                vals={
                    'name' : kw['name'], 
                    'warna': kw['warna'],
                    'tipe' : kw['tipe'],
                    'stok' : kw['stok'],
                    'harga': kw['harga'],
                }
                androidbaru = request.env['handphone.android'].create(vals)
                args = {'success': True, 'ID':androidbaru.id}
                return args