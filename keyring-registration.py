# coding=utf-8
import yagmail
import keyring
import config as cfg

yagmail.register(cfg.email['email'], password=cfg.email['passwd'])
