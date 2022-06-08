# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fw_odoo_social_media(models.Model):
    _name="social_media"

    twitter= fields.Many2many("fw_odoo_twitter_post")
    facebook = fields.Many2many("fw_odoo_facebook_post")
    mailing = fields.Many2many("mailing.mailing")

    state = fields.Char(compute="_fstate", store=True)
    mailing_type = fields.Char(compute="_fstate", store=True)
    name = fields.Char(compute="_fstate", store=True)

    @api.depends("twitter", "facebook", "mailing")
    def _fstate(self):
        for record in self:
            if not self.twitter:
                if not self.facebook:
                    record.state=self.mailing.state
                    record.mailing_type=self.mailing.mailing_type
                    record.name=self.mailing.name
                else:
                    record.state=self.facebook.state
                    record.mailing_type=self.facebook.mailing_type
                    record.name=self.mailing.name
            else :
                record.state=self.twitter.state
                record.mailing_type=self.twitter.mailing_type
                record.name=self.mailing.name
            if record.state=="C-done":
                record.state="done"
            elif record.state=="A-draft":
                record.state="draft"
            elif record.state=="B-schedule":
                record.state="schedule"
            elif record.state=="D-cancel":
                record.state="cancel"


