# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import datetime

from odoo import http, _
from odoo.addons.phone_validation.tools import phone_validation
from odoo.http import request, Response


class MailingLineController(http.Controller):

    @http.route(['/set/line-marketing-bot-group'], type='json', auth='none', methods=['POST'], csrf=False, save_session=False)
    def line_web_hook(self, **post):        
        d = request.jsonrequest
        err = ''
        if d.get('type',False) == 'join':
           botpool = request.env['fw_bot_group']
           
           gid = d.get('source',{}).get('groupId',False)
           if not gid:
               err = 'no groupid'
           else:
                bid = botpool.search([('group_id','=', gid)])
                
                if not bid.id:
                    botpool.create({
                        'date_join': datetime.datetime.fromtimestamp(d.get('timestamp', 0) / 1000),
                        'name': d.get('groupName'),
                        'group_id': gid
                    })
                    err = 'group recorded'
                else:
                    err = 'groupid already exist'  

        else:
           err = 'type %s' % d.get('type') 
        return {'status': err}

