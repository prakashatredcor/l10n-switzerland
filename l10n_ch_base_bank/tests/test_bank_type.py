# -*- coding: utf-8 -*-
# © 2015 Yannick Vaucher (Camptocamp SA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp.tests import common


class TestBankType(common.TransactionCase):

    def test_is_bank_account_with_post(self):
        bank = self.env['res.bank'].create({
            'name': 'BCV',
            'ccp': '01-1234-1',
            'bic': '234234',
            'clearing': '234234',
        })
        bank_account = self.env['res.partner.bank'].create({
            'partner_id': self.partner.id,
            'bank_id': bank.id,
            'bank_name': bank.name,
            'bank_bic': bank.bic,
            'acc_number': 'Bank/CCP 01-1234-1',
        })
        self.assertEqual(bank_account.acc_type, 'bank')

    def test_is_postal_account(self):
        bank = self.env['res.bank'].create({
            'name': 'BCV',
            'bic': '234234',
            'clearing': '234234',
        })
        bank_account = self.env['res.partner.bank'].create({
            'partner_id': self.partner.id,
            'bank_id': bank.id,
            'bank_name': bank.name,
            'bank_bic': bank.bic,
            'acc_number': '01-1234-1',
        })
        self.assertEqual(bank_account.acc_type, 'postal')

    def setUp(self):
        super(TestBankType, self).setUp()
        self.company = self.env.ref('base.main_company')
        self.partner = self.env.ref('base.main_partner')
