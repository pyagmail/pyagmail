# coding=utf-8
import yagmail
import keyring
import virtualconfig as cfg

yagmail.register(cfg.email['email'], password=cfg.email['passwd'])
